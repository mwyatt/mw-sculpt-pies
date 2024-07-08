import bpy
from . bl_info import *
from . pie_create import *
from . pie_misc import *
from . pie_flip import *
from . pie_align_active import *
from . pie_symmetry import *
from . pie_modifier import *
from . pie_mask_slice import *
# from . pie_dyntopo import *

classes = [
    MWSCULPTPIES_MT_PIE_CREATE,
    pie_create_cube,
    pie_create_sphere,
    pie_create_cylinder,
    pie_create_cone,

    MWSCULPTPIES_MT_PIE_MISC,
    pie_misc_make_single_user,
    pie_misc_parent_keep_transform,
    pie_misc_unparent_keep_transform,
    pie_misc_center_origin,
    pie_misc_link_object_data,
    pie_misc_apply_scale,
    pie_misc_recalculate_outside,
    pie_misc_convert_to_mesh,

    MWSCULPTPIES_MT_PIE_FLIP,
    pie_flip_x,
    pie_flip_y,
    pie_flip_z,

    MWSCULPTPIES_MT_PIE_ALIGN_ACTIVE,
    pie_align_active_top,
    pie_align_active_right,
    pie_align_active_bottom,
    pie_align_active_left,
    pie_align_active_front,
    pie_align_active_back,
    pie_align_active_perspective,

    MWSCULPTPIES_MT_PIE_MODIFIER,
    pie_modifier_decimate_05,
    pie_modifier_decimate_nudge,
    pie_modifier_mirror_over,
    pie_modifier_hard_surface,
    pie_modifier_sub_division_1,
    pie_modifier_array_curve,
    pie_modifier_bool_union,
    pie_modifier_bool_diff,

    MWSCULPTPIES_MT_PIE_SYMMETRY,
    pie_symmetry_x,
    pie_symmetry_xx,
    pie_symmetry_y,
    pie_symmetry_yy,
    pie_symmetry_z,
    pie_symmetry_zz,
    pie_symmetry_reset_radial,

    MWSCULPTPIES_MT_PIE_MASK_SLICE,
    pie_mask_slice_fill_holes,
    pie_mask_slice_new_object_overlap,
    pie_mask_slice_new_object_clear_mask,

    # MWSCULPTPIES_MT_PIE_DYNTOPO,
    # pie_dyntopo_enable,
    # pie_dyntopo_disable,
    # pie_dyntopo_flood,
    # pie_dyntopo_res_1,
    # pie_dyntopo_res_3,
    # pie_dyntopo_res_5,
    # pie_dyntopo_res_7,
    # pie_dyntopo_res_9,
]

def register():
    # print('register >>>>>>>>>>>>>>>>')
    for clas in classes:
        bpy.utils.register_class(clas)

def unregister():
    # print('<<<<<<<<<<<<<<< unregister')
    for clas in classes:
        bpy.utils.unregister_class(clas)

if __name__ == "__main__":
    register()
