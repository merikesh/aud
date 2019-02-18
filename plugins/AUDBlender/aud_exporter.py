import logging
from dataclasses import dataclass
from typing import *

import bpy

from . import aud
from .aud import audGeom, audLux
from .aud import utils as aud_utils

logging.basicConfig()
logger = logging.getLogger('aud-blender')
logger.setLevel(aud_utils.get_logger_verbosity())


@dataclass
class AnimatedNode(object):
    """
    Store information about the animated data node
    """
    node: bpy.types.Object
    start: int
    end: int
    channels: Set[str]


class AUDExporter(object):
    """Exporter for USDA files from blender"""

    def __init__(self,
                 context=None,
                 selected=False,
                 animation=False,
                 geocache=False,
                 cameras=True,
                 lights=False,
                 materials=False,
                 skeletons=False):
        super(AUDExporter, self).__init__()

        # Exporter options
        self.only_selected = selected
        self.context = context
        self.animation = animation
        self.geocache = geocache and animation
        self.export_cameras = cameras
        self.export_lights = lights
        self.export_materials = materials
        self.export_skeletons = skeletons

        # Exporter state variables
        self.stage = None
        self.animated_objects: Dict[aud.Prim:AnimatedNode] = {}
        self.geocache_objects: Dict[aud.base.Prim: bpy.types.Object] = {}
        self.material_scope = None
        self.material_objects = {}

        # TODO: Remove these temporary variables
        self.animation = True
        self.export_materials = True
        self.geocache = True

    def write(self, filepath):
        """Wrapped function to set up the write mode and change the frames before writing"""
        # Exit edit mode before exporting, so current object states are exported properly.
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')

        scene = self.context.scene
        current_frame = scene.frame_current

        if self.animation:
            # If we're exporting animation, then we need to go to the start first
            scene.frame_set(scene.frame_start)

        try:
            self._write()
        finally:
            if self.stage:
                self.stage.save(location=filepath)
            self.stage = None  # clear it out when we're done writing
            scene.frame_set(current_frame)

        logger.debug("Finished writing to %s", filepath)
        return {'FINISHED'}

    def _write(self):
        """
        Perform the actual write out of the stage
        """

        self.stage: aud.base.Stage = aud.Stage()

        self.configure_stage()
        self.write_hierarchy()
        if self.animation:
            self.write_animation()

        if self.material_scope and not self.material_objects:
            self.stage.remove_child(self.material_scope)

    def configure_stage(self):
        """Setup all the stage variables"""
        if not self.stage:
            return

        scene = self.context.scene

        self.stage.set_up_axis('Z')  # Blender is hardcoded to Z up

        if self.animation:
            self.stage.set_frame_range(scene.frame_start, scene.frame_end)
            self.stage.set_framerate(scene.render.fps)

        if self.export_materials:
            mat_scope = aud.Prim('Materials', as_type='Scope')
            self.stage.add_child(mat_scope)
            self.material_scope = mat_scope

    def write_hierarchy(self):
        """Create the initial hierarchy  of the USD file"""
        if self.only_selected:
            objects = self.context.selected_objects
        else:
            objects = self.context.scene.objects

        for obj in objects:
            self.add_node(obj, parent=self.stage)

    def add_node(self, node: bpy.types.Object, parent: aud.AbstractData):
        """Add an abstract node to the hierarchy and loop over its children"""
        ntype = node.type

        # For different node types, create the appropriate prims
        data_node = None
        add_prim = False

        if ntype == 'MESH':
            data_node = self.mesh(node)
        elif ntype == 'LIGHT':
            data_node = self.light(node)
        elif ntype == 'CAMERA':
            data_node = self.camera(node)
        elif ntype == 'EMPTY':
            add_prim = True
        else:
            logger.error('Object "%s" of type "%s" is not supported', node.name, ntype)
            return

        if not data_node and not add_prim:
            return

        prim = self.xform(node)
        if data_node:
            prim.add_child(data_node)

        # Add the prim to the parent
        parent.add_child(prim)
        # Now iterate over the children of this node
        for child in node.children:
            self.add_node(child, prim)

    def check_animation(self, node, prim, main_node=None, force=False):
        if not self.animation and not force:
            return False

        if not main_node:
            main_node = node

        anim_data = node.animation_data
        if not anim_data:
            return False

        action: bpy.types.Action = anim_data.action
        channels = set({str(c.data_path) for c in action.fcurves if c.data_path})

        anim_node = self.animated_objects.get(prim)
        if anim_node:
            anim_node.start = min(anim_node.start, action.frame_range[0])
            anim_node.end = max(anim_node.end, action.frame_range[1])
            anim_node.channels.update(channels)

        else:
            anim_node = AnimatedNode(
                main_node,
                action.frame_range[0],
                action.frame_range[1],
                channels
            )

        self.animated_objects[prim] = anim_node

    def write_animation(self):
        """If there's any animation we'll now write it out"""
        if not (self.animated_objects or self.geocache_objects):
            return

        scene = self.context.scene

        for frame in range(scene.frame_start, scene.frame_end + 1):
            scene.frame_set(frame)
            for prim, animnode in self.animated_objects.items():
                if frame < animnode.start or frame > animnode.end:
                    continue

                node = animnode.node
                ntype = node.type
                channels = animnode.channels.copy()

                self.apply_transforms(node, frame=frame, prim=prim,
                                      channels=channels)

                if ntype == 'CAMERA':
                    self.camera(node, frame=frame, prim=prim, channels=channels)
                elif ntype == 'LIGHT':
                    self.light(node, frame=frame, prim=prim, channels=channels)

            for prim, node in self.geocache_objects.items():
                self.mesh(node, frame=frame, prim=prim)

    def xform(self, node, frame=None):
        prim = audGeom.Xform(node.name)
        if frame is None:
            self.apply_transforms(node, prim)
            self.check_animation(node, prim)
        return prim

    def mesh(self, node, frame=None, prim=None):
        """Setup mesh prims"""

        if frame is not None and not self.geocache:
            return

        name = node.data.name
        prim = prim or audGeom.Mesh(name)
        depsgraph = self.context.depsgraph
        mesh = node.to_mesh(depsgraph, apply_modifiers=True)

        vertices = mesh.vertices[:]
        polygons = mesh.polygons[:]
        loops = mesh.loops[:]

        positions = []
        normals = []

        for vert in vertices:
            pos = vert.co
            norm = vert.normal
            positions.append((pos.x, pos.y, pos.z))
            normals.append((norm.x, norm.y, norm.z))

        if frame is None:
            prim.set_attribute('points', positions, as_type='point3f[]')
        else:
            attr = prim.get_attribute('points')
            attr.set_keyframe(frame, positions)
            return prim

        self.geocache_objects[prim] = node

        vertCounts = []
        vertIndices = []
        for poly in polygons:
            verts = poly.vertices
            vertCounts.append(len(verts))

            for l in poly.loop_indices:
                loop = loops[l]
                vertIndices.append(loop.vertex_index)

        prim.set_attribute('faceVertexCounts', vertCounts, as_type='int[]')
        prim.set_attribute('faceVertexIndices', vertIndices, as_type='int[]')

        normAttr = prim.set_attribute('primvars:normals', normals, as_type='normal3f[]')
        normAttr.set_property('interpolation', 'faceVarying')

        return prim

    def light(self, node, frame=None, prim=None, channels=()):
        """setup light prims"""
        if not self.export_lights:
            return

        light = bpy.data.lights.get(node.name)

        prim = prim or {
            'SUN': audLux.DistantLight
        }.get(light.type, audLux.Light)(node.data.name)

        if not prim.as_type:
            prim.as_type = 'Light'  # Technically incorrect but just as a fallback

        if frame:
            logger.warning("Light type doesn't support animated write outs")
            return prim

        prim.set_attribute('color',
                           (light.color.r, light.color.g, light.color.b),
                           as_type='color3f')
        prim.set_attribute('intensity', light.energy, as_type='float')
        return prim

    def camera(self, node: bpy.types.Object, frame=None, prim=None, channels=()):
        """setup camera prims"""
        if not self.export_cameras:
            return

        cam: bpy.types.Camera = bpy.data.cameras.get(node.name)
        prim = prim or audGeom.Camera(node.name)
        if frame is None:
            self.check_animation(cam, prim, main_node=node)

            projection = {
                'PERSP': 'perspective',
                'ORTHO': 'orthographic'
            }.get(cam.type)
            prim.set_property("kind", "assembly")
            prim.set_attribute('projection', projection, as_type="token")

            prim.set_attribute('horizontalAperture', cam.sensor_width)
            prim.set_attribute('horizontalApertureOffset', cam.shift_x)
            prim.set_attribute('verticalAperture', cam.sensor_height)
            prim.set_attribute('verticalApertureOffset', cam.shift_y)

        attr_map = (
            ('clippingRange', 'clip_start', 'clip_end', 'float2'),
            ('focalLength', 'lens', 'float'),
            ('focusDistance', 'dof_distance', 'float')
        )

        for attr, *chans, attr_type in attr_map:

            if not (frame is None or any(c for c in chans if c in channels)):
                continue

            val = [getattr(cam, c) for c in chans]
            if len(val) == 1:
                val = val[0]

            if frame is None:
                prim.set_attribute(attr, val, as_type=attr_type)
            else:
                attr = prim.get_attribute(attr)
                attr.set_keyframe(frame, val)

        return prim

    def apply_transforms(self, node: bpy.types.Object, prim: aud.Prim,
                         frame=None, channels=()):
        """apply transforms for an abstract prim type"""
        xform_channels = ('location', 'rotation_euler', 'scale')
        if frame and not any([c for c in channels if c in xform_channels]):
            return

        attrMap = (
            ('xformOp:translate', 'location', xform_channels[0]),
            ('xformOp:rotateXYZ', 'rotation', xform_channels[1]),
            ('xformOp:scale', 'scale', xform_channels[2])
        )

        if frame is None:
            prim.set_xform_order()

        for attr, val, channel in attrMap:
            if frame is not None and channel not in channels:
                continue

            if val == 'location':
                location = node.location
                val = (location.x, location.y, location.z)
            elif val == 'rotation':
                rotation = node.rotation_euler
                val = (rotation.x, rotation.y, rotation.z)
            elif val == 'scale':
                scale = node.scale
                val = (scale.x, scale.y, scale.z)
            else:
                logger.error("Unknown Xform channel: %s", val)
                continue

            if frame is None:
                prim.set_attribute(attr, val, as_type='double3')
            else:
                attr = prim.get_attribute(attr)
                attr.set_keyframe(frame, val)
