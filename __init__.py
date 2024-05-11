import bpy
from . pie_create import *
from . pie_misc import *
from . pie_remesh import *
from . pie_flip import *
from . pie_align_active import *
from . pie_symmetry import *
from . pie_modifier import *

bl_info = {
    "name": "MW Sculpt Pies",
    "author": "Martin Wyatt",
    "version": (2, 1, 0, 0),
    "description": "Helper pies for sculpting faster!",
    "location": "View 3D",
    "blender": (4, 1, 1),
    "category": "Object",
}

classes = [
    pie_create,
    pie_create_cube,
    pie_create_sphere,
    pie_create_cylinder,
    pie_create_cone,

    pie_misc,
    pie_misc_make_single_user,
    pie_misc_parent_keep_transform,
    pie_misc_unparent_keep_transform,
    pie_misc_center_origin,
    pie_misc_link_object_data,
    pie_misc_apply_scale,
    pie_misc_recalculate_outside,
    pie_misc_convert_to_mesh,

    pie_remesh,
    pie_remesh_06,
    pie_remesh_04,
    pie_remesh_03,
    pie_remesh_02,
    pie_remesh_015,
    pie_remesh_01,
    pie_remesh_0075,
    pie_remesh_005,

    pie_flip,
    pie_flip_x,
    pie_flip_y,
    pie_flip_z,

    pie_align_active,
    pie_align_active_top,
    pie_align_active_right,
    pie_align_active_bottom,
    pie_align_active_left,
    pie_align_active_front,
    pie_align_active_back,
    pie_align_active_perspective,

    pie_modifier,
    pie_modifier_decimate_05,
    pie_modifier_mirror_over,
    pie_modifier_hard_surface,
    pie_modifier_array_curve,
    pie_mask_slice_new_object,

    pie_symmetry,
    pie_symmetry_x,
    pie_symmetry_xx,
    pie_symmetry_y,
    pie_symmetry_yy,
    pie_symmetry_z,
    pie_symmetry_zz,
    pie_symmetry_reset_radial,
]

def register():
    print('register >>>>>>>>>>>>>>>>')
    for clas in classes:
        bpy.utils.register_class(clas)

def unregister():
    print('<<<<<<<<<<<<<<< unregister')
    for clas in classes:
        bpy.utils.unregister_class(clas)

if __name__ == "__main__":
    register()
