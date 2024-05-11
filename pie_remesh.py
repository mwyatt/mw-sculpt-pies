import bpy
from bpy.types import Menu, Operator
from . bl_info import *

class pie_remesh(Menu):
    bl_label = "Remesh"
    bl_idname = "mw_sculpt_pie.remesh"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("pie.pie_remesh_0075", icon='FILE_3D')
        pie.operator("pie.pie_remesh_03", icon='FILE_3D')
        pie.operator("pie.pie_remesh_01", icon='FILE_3D')
        pie.operator("pie.pie_remesh_06", icon='FILE_3D')
        pie.operator("pie.pie_remesh_005", icon='FILE_3D')
        pie.operator("pie.pie_remesh_04", icon='FILE_3D')
        pie.operator("pie.pie_remesh_015", icon='FILE_3D')
        pie.operator("pie.pie_remesh_02", icon='FILE_3D')

class pie_remesh_06(Operator):
    bl_label = "0.6"
    bl_idname = "pie.pie_remesh_06"
    bl_description = "Remesh selected object to 0.6 voxel size."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.object.data.remesh_voxel_size = 0.6
        bpy.ops.object.voxel_remesh()
        self.report({'INFO'}, bl_info.get('name') + ': Remeshed to 0.6 voxel size')
        return {'FINISHED'}

class pie_remesh_04(Operator):
    bl_label = "0.4"
    bl_idname = "pie.pie_remesh_04"
    bl_description = "Remesh selected object to 0.4 voxel size."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.object.data.remesh_voxel_size = 0.4
        bpy.ops.object.voxel_remesh()
        self.report({'INFO'}, bl_info.get('name') + ': Remeshed to 0.4 voxel size')
        return {'FINISHED'}
        
class pie_remesh_03(Operator):
    bl_label = "0.3"
    bl_idname = "pie.pie_remesh_03"
    bl_description = "Remesh selected object to 0.3 voxel size."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.object.data.remesh_voxel_size = 0.3
        bpy.ops.object.voxel_remesh()
        self.report({'INFO'}, bl_info.get('name') + ': Remeshed to 0.3 voxel size')
        return {'FINISHED'}
        
class pie_remesh_02(Operator):
    bl_label = "0.2"
    bl_idname = "pie.pie_remesh_02"
    bl_description = "Remesh selected object to 0.2 voxel size."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.object.data.remesh_voxel_size = 0.2
        bpy.ops.object.voxel_remesh()
        self.report({'INFO'}, bl_info.get('name') + ': Remeshed to 0.2 voxel size')
        return {'FINISHED'}

class pie_remesh_015(Operator):
    bl_label = "0.15"
    bl_idname = "pie.pie_remesh_015"
    bl_description = "Remesh selected object to 0.15 voxel size."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.object.data.remesh_voxel_size = 0.15
        bpy.ops.object.voxel_remesh()
        self.report({'INFO'}, bl_info.get('name') + ': Remeshed to 0.15 voxel size')
        return {'FINISHED'}

class pie_remesh_01(Operator):
    bl_label = "0.1"
    bl_idname = "pie.pie_remesh_01"
    bl_description = "Remesh selected object to 0.1 voxel size."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.object.data.remesh_voxel_size = 0.1
        bpy.ops.object.voxel_remesh()
        self.report({'INFO'}, bl_info.get('name') + ': Remeshed to 0.1 voxel size')
        return {'FINISHED'}
        
class pie_remesh_0075(Operator):
    bl_label = "0.075"
    bl_idname = "pie.pie_remesh_0075"
    bl_description = "Remesh selected object to 0.075 voxel size."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.object.data.remesh_voxel_size = 0.075
        bpy.ops.object.voxel_remesh()
        self.report({'INFO'}, bl_info.get('name') + ': Remeshed to 0.075 voxel size')
        return {'FINISHED'}
        
class pie_remesh_005(Operator):
    bl_label = "0.05"
    bl_idname = "pie.pie_remesh_005"
    bl_description = "Remesh selected object to 0.05 voxel size."

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='SCULPT')
        bpy.context.object.data.remesh_voxel_size = 0.05
        bpy.ops.object.voxel_remesh()
        self.report({'INFO'}, bl_info.get('name') + ': Remeshed to 0.05 voxel size')
        return {'FINISHED'}
