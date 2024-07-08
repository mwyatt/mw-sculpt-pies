import bpy
from bpy.types import Menu, Operator
from . bl_info import *
from . common import *

class MWSCULPTPIES_MT_PIE_FLIP(Menu):
    bl_label = "Flip"
    bl_idname = "MWSCULPTPIES_MT_PIE_FLIP"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("pie.pie_flip_x", icon='ARROW_LEFTRIGHT')
        pie.operator("pie.pie_flip_y", icon='ARROW_LEFTRIGHT')
        pie.operator("pie.pie_flip_z", icon='ARROW_LEFTRIGHT')

class pie_flip_x(Operator):
    bl_label = "X"
    bl_idname = "pie.pie_flip_x"
    bl_description = "Mirrors over the x axis."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.transform.mirror(orient_type='LOCAL', constraint_axis=(True, False, False))
        apply_scale()
        self.report({'INFO'}, bl_info.get('name') + ': Mirrored over x axis')
        return {'FINISHED'}
        
class pie_flip_y(Operator):
    bl_label = "Y"
    bl_idname = "pie.pie_flip_y"
    bl_description = "Mirrors over the y axis."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.transform.mirror(orient_type='LOCAL', constraint_axis=(False, True, False))
        apply_scale()
        self.report({'INFO'}, bl_info.get('name') + ': Mirrored over y axis')
        return {'FINISHED'}
        
class pie_flip_z(Operator):
    bl_label = "Z"
    bl_idname = "pie.pie_flip_z"
    bl_description = "Mirrors over the z axis."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.transform.mirror(orient_type='LOCAL', constraint_axis=(False, False, True))
        apply_scale()
        self.report({'INFO'}, bl_info.get('name') + ': Mirrored over z axis')
        return {'FINISHED'}
