import bpy
from bpy.types import Menu, Operator
from . bl_info import *

class pie_symmetry(Menu):
    bl_label = "Symmetry"
    bl_idname = "mw_sculpt_pie.symmetry"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("pie.pie_symmetry_xx", icon='ARROW_LEFTRIGHT')
        pie.operator("pie.pie_symmetry_x", icon='ARROW_LEFTRIGHT')
        pie.operator("pie.pie_symmetry_zz", icon='ARROW_LEFTRIGHT')
        pie.operator("pie.pie_symmetry_z", icon='ARROW_LEFTRIGHT')
        pie.operator("pie.pie_symmetry_y", icon='ARROW_LEFTRIGHT')
        pie.operator("pie.pie_symmetry_yy", icon='ARROW_LEFTRIGHT')
        pie.operator("pie.pie_symmetry_reset_radial", icon='RADIOBUT_OFF')
        
class pie_symmetry_x(Operator):
    bl_label = "X"
    bl_idname = "pie.pie_symmetry_x"
    bl_description = "Copies mesh data from +X to -X"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.scene.tool_settings.sculpt.symmetrize_direction = 'POSITIVE_X'
        bpy.ops.sculpt.symmetrize()
        self.report({'INFO'}, bl_info.get('name') + ': Copied mesh data from +X to -X')
        return {'FINISHED'}
        
class pie_symmetry_xx(Operator):
    bl_label = "-X"
    bl_idname = "pie.pie_symmetry_xx"
    bl_description = "Copies mesh data from -X to +X"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.scene.tool_settings.sculpt.symmetrize_direction = 'NEGATIVE_X'
        bpy.ops.sculpt.symmetrize()
        self.report({'INFO'}, bl_info.get('name') + ': Copied mesh data from -X to +X')
        return {'FINISHED'}
        
class pie_symmetry_y(Operator):
    bl_label = "Y"
    bl_idname = "pie.pie_symmetry_y"
    bl_description = "Copies mesh data from +Y to -Y"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.scene.tool_settings.sculpt.symmetrize_direction = 'POSITIVE_Y'
        bpy.ops.sculpt.symmetrize()
        self.report({'INFO'}, bl_info.get('name') + ': Copied mesh data from +Y to -Y')
        return {'FINISHED'}
        
class pie_symmetry_yy(Operator):
    bl_label = "-Y"
    bl_idname = "pie.pie_symmetry_yy"
    bl_description = "Copies mesh data from -Y to +Y"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.scene.tool_settings.sculpt.symmetrize_direction = 'NEGATIVE_Y'
        bpy.ops.sculpt.symmetrize()
        self.report({'INFO'}, bl_info.get('name') + ': Copied mesh data from -Y to +Y')
        return {'FINISHED'}
        
class pie_symmetry_z(Operator):
    bl_label = "Z"
    bl_idname = "pie.pie_symmetry_z"
    bl_description = "Copies mesh data from +Z to -Z"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.scene.tool_settings.sculpt.symmetrize_direction = 'POSITIVE_Z'
        bpy.ops.sculpt.symmetrize()
        self.report({'INFO'}, bl_info.get('name') + ': Copied mesh data from +Z to -Z')
        return {'FINISHED'}
        
class pie_symmetry_zz(Operator):
    bl_label = "-Z"
    bl_idname = "pie.pie_symmetry_zz"
    bl_description = "Copies mesh data from -Z to +Z"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.scene.tool_settings.sculpt.symmetrize_direction = 'NEGATIVE_Z'
        bpy.ops.sculpt.symmetrize()
        self.report({'INFO'}, bl_info.get('name') + ': Copied mesh data from -Z to +Z')
        return {'FINISHED'}
        
class pie_symmetry_reset_radial(Operator):
    bl_label = "Radial Reset"
    bl_idname = "pie.pie_symmetry_reset_radial"
    bl_description = "Resets radial symmetry to 1"

    def execute(self, context):
        if bpy.context.active_object.mode != 'SCULPT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.scene.tool_settings.sculpt.radial_symmetry[0] = 1
        bpy.context.scene.tool_settings.sculpt.radial_symmetry[1] = 1
        bpy.context.scene.tool_settings.sculpt.radial_symmetry[2] = 1
        self.report({'INFO'}, bl_info.get('name') + ': Reset radial symmetry to 1')
        return {'FINISHED'}
