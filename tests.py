import aud
import os
from aud import audGeom


root_directory = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(root_directory, 'sample_data', 'test.usda')

stage = aud.Stage()
stage.set_frame_range(1, 200)
stage.set_framerate(24)
stage.set_up_axis('Y')

root = aud.Prim('root')
stage.add_child(root)

cyl = root.add_child(audGeom.Cylinder('cylinder'))
cube = root.add_child(audGeom.Cube('Cube'))
attr = cyl.set_attribute('height', 10)
cyl.set_attribute('axis', 'Y')

translate = cyl.set_attribute('xformOp:translate', (-1.99, 0, 2), as_type='double3')
translate.set_keyframe(1, (1,2,3))
translate.set_keyframe(2, (5,4,3))
translate.set_keyframe(100, (10,10,10))

cyl.set_xform_order()


xf = root.add_child(audGeom.Xform('foo'))
xf.add_inherit(cyl, mode='add')

xf.add_variant("lodVariant")

lodVariant = xf.add_child(aud.VariantSet("lodVariant"))
hiLOD = lodVariant.add_child(aud.Variant("hi"))

hiLOD.add_child(audGeom.Xform('HiGeometry'))



stage.save(output_file)