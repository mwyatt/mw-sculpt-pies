import bpy
from bpy.types import Menu, Operator
from . bl_info import *

class pie_misc(Menu):
    bl_label = "Misc"
    bl_idname = "mw_sculpt_pie.misc"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("pie.pie_misc_make_single_user", icon='UNLINKED')
        pie.operator("pie.pie_misc_link_object_data", icon='LINKED')
        pie.operator("pie.pie_misc_convert_to_mesh", icon='MESH_GRID')
        pie.operator("pie.pie_misc_center_origin", icon='CLIPUV_DEHLT')
        pie.operator("pie.pie_misc_unparent_keep_transform", icon='KEYFRAME')
        pie.operator("pie.pie_misc_parent_keep_transform", icon='KEYFRAME_HLT')
        pie.operator("pie.pie_misc_recalculate_outside", icon='NORMALS_FACE')
        pie.operator("pie.pie_misc_apply_scale", icon='SHADING_BBOX')

class pie_misc_make_single_user(Operator):
    bl_label = "Make Single User"
    bl_idname = "pie.pie_misc_make_single_user"
    bl_description = "Gives selected object a unique mesh."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False)
        self.report({'INFO'}, bl_info.get('name') + ': Converted to single user')
        return {'FINISHED'}

class pie_misc_parent_keep_transform(Operator):
    bl_label = "Parent"
    bl_idname = "pie.pie_misc_parent_keep_transform"
    bl_description = "Parents object(s) and keeps transform."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if len(bpy.context.selected_objects) < 2:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select at least two objects first')
            return {'FINISHED'}

        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
        self.report({'INFO'}, bl_info.get('name') + ': Parented together and kept transform')
        return {'FINISHED'}

class pie_misc_unparent_keep_transform(Operator):
    bl_label = "UnParent"
    bl_idname = "pie.pie_misc_unparent_keep_transform"
    bl_description = "Un Parents object(s) and keeps transform."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        self.report({'INFO'}, bl_info.get('name') + ': Unparented and kept transform')
        return {'FINISHED'}

class pie_misc_center_origin(Operator):
    bl_label = "Center Origin Geometry"
    bl_idname = "pie.pie_misc_center_origin"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='MEDIAN')
        self.report({'INFO'}, bl_info.get('name') + ': Centered origin to geometry')
        return {'FINISHED'}

class pie_misc_link_object_data(Operator):
    bl_label = "Link Object Data"
    bl_idname = "pie.pie_misc_link_object_data"
    bl_description = "Shares the mesh of selected object(s)"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)
        if len(bpy.context.selected_objects) < 2:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select at least two objects first')
            return {'FINISHED'}
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.make_links_data(type='OBDATA')
        self.report({'INFO'}, bl_info.get('name') + ': Linked object data')
        return {'FINISHED'}

class pie_misc_apply_scale(Operator):
    bl_label = "Apply Scale"
    bl_idname = "pie.pie_misc_apply_scale"
    bl_description = "Makes object a single user, applies scale and recalculates normals to outside."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        bpy.ops.object.make_single_user(object=True, obdata=True, material=False, animation=False)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent(inside=False)
        bpy.ops.object.editmode_toggle()
        self.report({'INFO'}, bl_info.get('name') + ': Made single user, applied scale, recalculated normals')
        return {'FINISHED'}

class pie_misc_recalculate_outside(Operator):
    bl_label = "Recalculate Outside"
    bl_idname = "pie.pie_misc_recalculate_outside"
    bl_description = "Recalculates all normals to outside."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent(inside=False)
        bpy.ops.object.editmode_toggle()
        self.report({'INFO'}, bl_info.get('name') + ': Recalculated normals')
        return {'FINISHED'}

class pie_misc_convert_to_mesh(Operator):
    bl_label = "Convert To Mesh"
    bl_idname = "pie.pie_misc_convert_to_mesh"
    bl_description = "Applies all modifiers and converts to a mesh."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.convert(target='MESH')
        self.report({'INFO'}, bl_info.get('name') + ': Converted to mesh')
        return {'FINISHED'}
