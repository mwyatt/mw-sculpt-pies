import bpy
from bpy.types import Menu, Operator
from . bl_info import *
from . rotation_copy import copyRotation

class pie_modifier(Menu):
    bl_label = "Modifier"
    bl_idname = "mw_sculpt_pie.modifier"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("pie.pie_modifier_decimate_05", icon='MOD_DECIM')
        pie.operator("pie.pie_modifier_mirror_over", icon='MOD_MIRROR')
        pie.operator("pie.pie_modifier_hard_surface", icon='MOD_BEVEL')
        pie.operator("pie.pie_mask_slice_new_object", icon='MOD_BEVEL')

        # wip
        # pie.operator("pie.pie_modifier_array_curve", icon='MOD_ARRAY')


class pie_modifier_decimate_05(Operator):
    bl_label = "decimate05"
    bl_idname = "pie.pie_modifier_decimate_05"
    bl_description = "Decimates object by 0.5 then applies."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False)
        bpy.ops.object.modifier_add(type='DECIMATE')
        bpy.context.object.modifiers["Decimate"].show_viewport = False
        bpy.context.object.modifiers["Decimate"].ratio = 0.5
        bpy.ops.object.modifier_apply(modifier="Decimate")
        self.report({'INFO'}, bl_info.get('name') + ': Decimated in half')
        return {'FINISHED'}

class pie_modifier_mirror_over(Operator):
    bl_label = "mirror_over"
    bl_idname = "pie.pie_modifier_mirror_over"
    bl_description = "Mirrors selected object over another."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        if len(bpy.context.selected_objects) != 2:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select two objects first')
            return {'FINISHED'}

        bpy.context.selected_objects[1].modifiers.new(name='MIRROR', type='MIRROR')
        bpy.context.selected_objects[1].modifiers['MIRROR'].mirror_object = bpy.context.selected_objects[0]

        self.report({'INFO'}, bl_info.get('name') + ': Mirrored over object')
        return {'FINISHED'}

class pie_modifier_hard_surface(Operator):
    bl_label = "hard_surface"
    bl_idname = "pie.pie_modifier_hard_surface"
    bl_description = "Adds bevel then a subsurface modifier."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        bpy.context.active_object.modifiers.new(name='BEVEL', type='BEVEL')
        bpy.context.active_object.modifiers['BEVEL'].width = 0.3
        bpy.context.active_object.modifiers['BEVEL'].segments = 2

        bpy.context.active_object.modifiers.new(name='SUBSURF', type='SUBSURF')
        bpy.context.active_object.modifiers["SUBSURF"].levels = 2

        self.report({'INFO'}, bl_info.get('name') + ': Bevelled and subdivided')
        return {'FINISHED'}

class pie_mask_slice_new_object(Operator):
    bl_label = "mask_slice_new_object"
    bl_idname = "pie.pie_mask_slice_new_object"
    bl_description = "Mask slices and fills holes, clears masks"

    def execute(self, context):
        og_object = bpy.context.active_object

        if bpy.context.active_object.mode != 'SCULPT':
            self.report({'ERROR'}, bl_info.get('name') + ': Please enter sculpt mode first and mask something')
            return {'FINISHED'}

        bpy.ops.object.mode_set(mode='OBJECT')

        # Duplicates object.
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})

        bpy.ops.object.mode_set(mode='SCULPT')

        # Flip mask.
        bpy.ops.paint.mask_flood_fill(mode='INVERT')

        # Mask slice and fill holes.
        bpy.ops.mesh.paint_mask_slice(new_object=False)

        # Clear mask.
        bpy.ops.paint.mask_flood_fill(mode='VALUE', value=0)

        bpy.ops.object.mode_set(mode='OBJECT')

        # Select first object
        bpy.context.active_object = og_object

        bpy.ops.object.mode_set(mode='SCULPT')

        # Mask slice and fill holes.
        bpy.ops.mesh.paint_mask_slice(new_object=False)

        # Clear mask.
        bpy.ops.paint.mask_flood_fill(mode='VALUE', value=0)

        bpy.ops.object.mode_set(mode='OBJECT')

        self.report({'INFO'}, bl_info.get('name') + ': Mask sliced and holes filled, masks cleared')
        return {'FINISHED'}

class pie_modifier_array_curve(Operator):
    bl_label = "array"
    bl_idname = "pie.pie_modifier_array_curve"
    bl_description = "Creates curve then arrays the selected object over that curve."

    def execute(self, context):
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')


        mesh_obj = bpy.context.active_object

        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.curve.primitive_nurbs_path_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.ops.view3d.snap_selected_to_cursor()
        curve_obj = bpy.context.active_object

        mesh_obj.modifiers.new(name='ARRAY', type='ARRAY')
        mesh_obj.modifiers['ARRAY'].fit_type = 'FIT_CURVE'
        mesh_obj.modifiers['ARRAY'].curve = curve_obj

        mesh_obj.modifiers.new(name='CURVE', type='CURVE')
        mesh_obj.modifiers["CURVE"].object = curve_obj

        mesh_obj.select_set(True)

        bpy.ops.object.select_all(action='DESELECT')
        for o in bpy.data.objects:
            if o.name in (curve_obj.name, mesh_obj.name):
                o.select_set(True)

        bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

        copyRotation(curve_obj, mesh_obj, context)

        bpy.ops.object.select_all(action='DESELECT')
        mesh_obj.select_set(True)
        
        self.report({'INFO'}, bl_info.get('name') + ': Arrayed and following new curve')
        return {'FINISHED'}
