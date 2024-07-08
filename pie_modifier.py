import bpy
from bpy.types import Menu, Operator
from . bl_info import *
from . rotation_copy import copyRotation
from . common import *

class MWSCULPTPIES_MT_PIE_MODIFIER(Menu):
    bl_label = "Modifier"
    bl_idname = "MWSCULPTPIES_MT_PIE_MODIFIER"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("pie.pie_modifier_decimate_05", icon='MOD_DECIM')
        pie.operator("pie.pie_modifier_decimate_nudge", icon='GRID')
        pie.operator("pie.pie_modifier_mirror_over", icon='MOD_MIRROR')
        pie.operator("pie.pie_modifier_sub_division_1", icon='MESH_GRID')
        pie.operator("pie.pie_modifier_bool_union", icon='ADD')
        pie.operator("pie.pie_modifier_bool_diff", icon='REMOVE')

        # Unused
        # pie.operator("pie.pie_modifier_hard_surface", icon='MOD_BEVEL')

        # wip
        # pie.operator("pie.pie_modifier_array_curve", icon='MOD_ARRAY')


class pie_modifier_decimate_05(Operator):
    bl_label = "Decimate"
    bl_idname = "pie.pie_modifier_decimate_05"
    bl_description = "Decimates object by 0.5 then applies."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        bpy.ops.object.modifier_add(type='DECIMATE')
        bpy.context.object.modifiers["Decimate"].show_viewport = False
        bpy.context.object.modifiers["Decimate"].ratio = 0.5
        bpy.ops.object.modifier_apply(modifier="Decimate")
        self.report({'INFO'}, bl_info.get('name') + ': Decimated in half')
        return {'FINISHED'}

class pie_modifier_decimate_nudge(Operator):
    bl_label = "Decimate Nudge"
    bl_idname = "pie.pie_modifier_decimate_nudge"
    bl_description = "Decimates slightly to help boolean operations"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        bpy.ops.object.modifier_add(type='DECIMATE')
        bpy.context.object.modifiers["Decimate"].show_viewport = False
        bpy.context.object.modifiers["Decimate"].ratio = 0.95
        bpy.ops.object.modifier_apply(modifier="Decimate")
        self.report({'INFO'}, bl_info.get('name') + ': Decimate nudged 0.95')
        return {'FINISHED'}

class pie_modifier_mirror_over(Operator):
    bl_label = "Mirror Over"
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

class pie_modifier_sub_division_1(Operator):
    bl_label = "Subdivide"
    bl_idname = "pie.pie_modifier_sub_division_1"
    bl_description = "Adds a subsurface modifier and applies."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        bpy.context.active_object.modifiers.new(name='SUBSURF', type='SUBSURF')
        bpy.context.active_object.modifiers["SUBSURF"].levels = 1
        bpy.ops.object.convert(target='MESH')

        self.report({'INFO'}, bl_info.get('name') + ': Subdivided')
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

class pie_modifier_bool_union(Operator):
    bl_label = "Union"
    bl_idname = "pie.pie_modifier_bool_union"
    bl_description = "Bool union objects together."

    def execute(self, context):
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.convert(target='MESH')
        apply_scale()
        bpy.ops.object.modifier_apply(modifier="Auto Boolean")
        bpy.ops.object.booltool_auto_union()

        self.report({'INFO'}, bl_info.get('name') + ': Bool unioned objects together')
        return {'FINISHED'}

class pie_modifier_bool_diff(Operator):
    bl_label = "Diff"
    bl_idname = "pie.pie_modifier_bool_diff"
    bl_description = "Bool diff objects."

    def execute(self, context):
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.convert(target='MESH')
        apply_scale()
        bpy.ops.object.modifier_apply(modifier="Auto Boolean")
        bpy.ops.object.booltool_auto_difference()

        self.report({'INFO'}, bl_info.get('name') + ': Bool diffed objects')
        return {'FINISHED'}
