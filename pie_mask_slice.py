import bpy
from bpy.types import Menu, Operator
from . bl_info import *
from . rotation_copy import copyRotation

class MWSCULPTPIES_MT_PIE_MASK_SLICE(Menu):
    bl_label = "Mask"
    bl_idname = "MWSCULPTPIES_MT_PIE_MASK_SLICE"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("pie.pie_mask_slice_fill_holes", icon='MOD_BEVEL')
        pie.operator("pie.pie_mask_slice_new_object_overlap", icon='MOD_BEVEL')
        pie.operator("pie.pie_mask_slice_new_object_clear_mask", icon='MOD_BEVEL')

class pie_mask_slice_fill_holes(Operator):
    bl_label = "Mask Slice Fill"
    bl_idname = "pie.pie_mask_slice_fill_holes"
    bl_description = "Mask slices and fills holes, clears masks"

    def execute(self, context):

        # Must be in sculpt mode.
        if bpy.context.active_object.mode != 'SCULPT':
            self.report({'ERROR'}, bl_info.get('name') + ': Please enter sculpt mode first and mask something')
            return {'FINISHED'}

        bpy.ops.mesh.paint_mask_slice(new_object=False)

        # Clear mask.
        bpy.ops.paint.mask_flood_fill(mode='VALUE', value=0)

        self.report({'INFO'}, bl_info.get('name') + ': Sliced mask, filled holes and mask cleared')
        return {'FINISHED'}

class pie_mask_slice_new_object_overlap(Operator):
    bl_label = "Mask Slice Overlap"
    bl_idname = "pie.pie_mask_slice_new_object_overlap"
    bl_description = "Mask slices and fills holes, clears masks"

    def execute(self, context):
        og_object = bpy.context.active_object

        # Must be in sculpt mode.
        if bpy.context.active_object.mode != 'SCULPT':
            self.report({'ERROR'}, bl_info.get('name') + ': Please enter sculpt mode first and mask something')
            return {'FINISHED'}

        # Check for existing mask data.
        # May not need this check.

        # Switch to object mode.
        bpy.ops.object.mode_set(mode='OBJECT')

        # Duplicates object.
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.context.active_object.select_set(True)
        new_object = bpy.context.active_object

        # Enter sculpt mode.
        # bpy.context.active_object.select_set(True)
        bpy.ops.object.mode_set(mode='SCULPT')

        # Flip mask.
        bpy.ops.paint.mask_flood_fill(mode='INVERT')

        # Mask slice and fill holes.
        bpy.ops.mesh.paint_mask_slice(new_object=False)

        # Clear mask.
        bpy.ops.paint.mask_flood_fill(mode='VALUE', value=0)

        # Recalculate normals
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent(inside=False)
        bpy.ops.object.editmode_toggle()

        bpy.ops.object.mode_set(mode='OBJECT')

        # Select first object
        og_object.select_set(True)
        bpy.context.view_layer.objects.active = og_object

        bpy.ops.object.mode_set(mode='SCULPT')

        # Clear mask.
        bpy.ops.paint.mask_flood_fill(mode='VALUE', value=0)

        #  Back to object mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Back into sculpt mode for new object.
        new_object.select_set(True)
        bpy.context.view_layer.objects.active = new_object
        bpy.ops.object.mode_set(mode='SCULPT')

        self.report({'INFO'}, bl_info.get('name') + ': Duplicated object and sliced mask, masks cleared')
        return {'FINISHED'}

class pie_mask_slice_new_object_clear_mask(Operator):
    bl_label = "Mask Slice New Object"
    bl_idname = "pie.pie_mask_slice_new_object_clear_mask"
    bl_description = "Mask slice new object fills holes, clears masks, enters sculpt mode on new object"

    def execute(self, context):
        og_object = bpy.context.active_object

        # Must be in sculpt mode.
        if bpy.context.active_object.mode != 'SCULPT':
            self.report({'ERROR'}, bl_info.get('name') + ': Please enter sculpt mode first and mask something')
            return {'FINISHED'}

        # Unparent, make single user and apply scale on original object.
        bpy.ops.object.mode_set(mode='OBJECT')
        og_object.select_set(True)
        bpy.context.view_layer.objects.active = og_object
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent(inside=False)
        bpy.ops.object.editmode_toggle()

        bpy.ops.object.mode_set(mode='SCULPT')

        # Mask slice to new object.
        bpy.ops.mesh.paint_mask_slice()

        new_object = bpy.context.active_object

        # Will have sliced to new object.
        # Deselect all objects.
        bpy.ops.object.select_all(action='DESELECT')

        # Select og object.
        og_object.select_set(True)
        bpy.context.view_layer.objects.active = og_object

        # Clear mask in sculpt mode.
        bpy.ops.object.mode_set(mode='SCULPT')
        bpy.ops.paint.mask_flood_fill(mode='VALUE', value=0)

        # Switch back to object mode.
        bpy.ops.object.mode_set(mode='OBJECT')

        # Select new object.
        bpy.ops.object.select_all(action='DESELECT')
        new_object.select_set(True)
        bpy.context.view_layer.objects.active = new_object

        # Finish in sculpt mode of new object.
        bpy.ops.object.mode_set(mode='SCULPT')

        self.report({'INFO'}, bl_info.get('name') + ': Mask sliced, masks cleared')
        return {'FINISHED'}
