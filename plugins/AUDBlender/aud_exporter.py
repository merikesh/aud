import logging
from dataclasses import dataclass
from typing import Dict, List, Set

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
                 cameras=False,
                 lights=False):
        super(AUDExporter, self).__init__()
        self.only_selected = selected
        self.context = context
        self.stage = None
        self.animation = animation
        self.geocache = geocache and animation
        self.export_cameras = cameras
        self.export_lights = lights
        self.animated_objects: Dict[aud.Prim:AnimatedNode] = {}

        self.animation = True

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

        self.stage = aud.Stage()

        self.configure_stage()
        self.write_hierarchy()
        if self.animation:
            self.write_animation()

    def configure_stage(self):
        """Setup all the stage variables"""
        if not self.stage:
            return

        scene = self.context.scene

        self.stage.set_up_axis('Z')  # Blender is hardcoded to Z up

        if self.animation:
            self.stage.set_frame_range(scene.frame_start, scene.frame_end)
            self.stage.set_framerate(scene.render.fps)

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
        nname = node.name
        ntype = node.type

        # For different node types, create the appropriate prims
        prim = None
        if ntype == 'MESH':
            prim = self.mesh(node)
        elif ntype == 'LIGHT':
            if self.export_lights:
                prim = self.light(node)
        elif ntype == 'CAMERA':
            if self.export_cameras:  # Put this deeper so we can still have the error below
                prim = self.camera(node)
        elif ntype == 'EMPTY':
            prim = audGeom.Xform(node.name)
        else:
            logger.error('Object "%s" of type "%s" is not supported', nname, ntype)
            return

        # If we don't have a prim, then it means we can't process it
        if not prim:
            return

        # Add the prim to the parent
        parent.add_child(prim)

        # And save any transformation values
        self.apply_transforms(node, prim)

        # Check if there are animations associated and hold on to it for later
        if self.animation and node.animation_data:
            animdata = node.animation_data
            action: bpy.types.Action = animdata.action
            channels = {str(c.data_path) for c in action.fcurves if c.data_path}
            self.animated_objects[prim] = AnimatedNode(
                node,
                action.frame_range[0],
                action.frame_range[1],
                channels
            )

        # Now iterate over the children of this node
        for child in node.children:
            self.add_node(child, prim)

    def write_animation(self):
        """If there's any animation we'll now write it out"""
        if not self.animated_objects:
            return

        scene = self.context.scene

        for frame in range(scene.frame_start, scene.frame_end + 1):
            scene.frame_set(frame)
            for prim, animnode in self.animated_objects.items():
                if frame < animnode.start or frame > animnode.end:
                    continue

                node = animnode.node
                ntype = node.type
                channels = animnode.channels

                if ntype == 'MESH':
                    if self.geocache:
                        self.mesh(node, frame=frame, prim=prim, channels=channels)
                elif ntype == 'LIGHT':
                    self.light(node, frame=frame, prim=prim, channels=channels)
                elif ntype == 'CAMERA':
                    self.camera(node, frame=frame, prim=prim, channels=channels)

                self.apply_transforms(node, frame=frame, prim=prim,
                                      channels=channels)

    def mesh(self, node, frame=None, prim=None, channels=()):
        """Setup mesh prims"""
        prim = prim or audGeom.Mesh(node.name)
        if frame:
            logger.warning("Mesh type doesn't support animated write outs")

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

        prim.set_attribute('points', positions, as_type='point3f[]')
        normAttr = prim.set_attribute('primvars:normals', normals, as_type='normal3f[]')
        normAttr.set_property('interpolation', 'faceVarying')

        return prim

    def light(self, node, frame=None, prim=None, channels=()):
        """setup light prims"""
        light = bpy.data.lights.get(node.name)

        prim = prim or {
            'SUN': audLux.DistantLight
        }.get(light.type, audLux.Light)(node.name)

        if not prim.as_type:
            prim.as_type = 'Light'  # Technically incorrect but just as a fallback

        if frame:
            logger.warning("Light type doesn't support animated write outs")
        prim.set_attribute('color',
                           (light.color.r, light.color.g, light.color.b),
                           as_type='color3f')
        prim.set_attribute('intensity', light.energy, as_type='float')
        return prim

    def camera(self, node: bpy.types.Object, frame=None, prim=None, channels=()):
        """setup camera prims"""
        cam: bpy.types.Camera = bpy.data.cameras.get(node.name)
        prim = prim or audGeom.Camera(node.name)
        if frame:
            logger.warning("Camera type doesn't support animated write outs")

        projection = {
            'PERSP': 'perspective',
            'ORTHO': 'orthographic'
        }.get(cam.type)
        prim.set_attribute('projection', projection)
        prim.set_attribute('clippingRange',
                           (cam.clip_start, cam.clip_end))
        prim.set_attribute('horizontalAperture', cam.sensor_width)
        prim.set_attribute('horizontalApertureOffset', cam.shift_x)
        prim.set_attribute('verticalAperture', cam.sensor_height)
        prim.set_attribute('verticalApertureOffset', cam.shift_y)
        prim.set_attribute('focalLength', cam.lens)

        return prim

    def apply_transforms(self, node: bpy.types.Object, prim: aud.Prim,
                         frame=None, channels=()):
        """apply transforms for an abstract prim type"""
        location = node.location
        location = (location.x, location.y, location.z)

        rotation = node.rotation_euler
        rotation = (rotation.x, rotation.y, rotation.z)

        scale = node.scale
        scale = (scale.x, scale.y, scale.z)

        attrMap = (
            ('xformOp:translate', location, 'location'),
            ('xformOp:rotateXYZ', rotation, 'rotation_euler'),
            ('xformOp:scale', scale, 'scale')
        )

        if frame is None:
            prim.set_xform_order()

        for attr, val, channel in attrMap:
            if frame is None:
                prim.set_attribute(attr, val, as_type='double3')
                continue

            if channel not in channels:
                continue

            attr = prim.get_attribute(attr)
            attr.set_keyframe(frame, val)
