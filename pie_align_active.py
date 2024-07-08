import bpy
from bpy.types import Menu, Operator
from . bl_info import *

class MWSCULPTPIES_MT_PIE_ALIGN_ACTIVE(Menu):
    bl_label = "Align Active"
    bl_idname = "MWSCULPTPIES_MT_PIE_ALIGN_ACTIVE"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("pie.pie_align_active_left", icon='TRIA_LEFT')
        pie.operator("pie.pie_align_active_right", icon='TRIA_RIGHT')
        pie.operator("pie.pie_align_active_bottom", icon='TRIA_DOWN')
        pie.operator("pie.pie_align_active_top", icon='TRIA_UP')
        pie.operator("pie.pie_align_active_front", icon='RADIOBUT_ON')
        pie.operator("pie.pie_align_active_back", icon='RADIOBUT_OFF')
        pie.operator("pie.pie_align_active_perspective", icon='VIEW_ORTHO')

class pie_align_active_top(Operator):
    bl_label = "Top"
    bl_idname = "pie.pie_align_active_top"
    bl_description = "Aligns view to active object top"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.view3d.view_axis(type='TOP', align_active=True)
        self.report({'INFO'}, bl_info.get('name') + ': Aligned view to active object top')
        return {'FINISHED'}
        
class pie_align_active_right(Operator):
    bl_label = "Right"
    bl_idname = "pie.pie_align_active_right"
    bl_description = "Aligns view to active object right"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.view3d.view_axis(type='RIGHT', align_active=True)
        self.report({'INFO'}, bl_info.get('name') + ': Aligned view to active object right')
        return {'FINISHED'}
        
class pie_align_active_bottom(Operator):
    bl_label = "Bottom"
    bl_idname = "pie.pie_align_active_bottom"
    bl_description = "Aligns view to active object bottom"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.view3d.view_axis(type='BOTTOM', align_active=True)
        self.report({'INFO'}, bl_info.get('name') + ': Aligned view to active object bottom')
        return {'FINISHED'}
        
class pie_align_active_left(Operator):
    bl_label = "Left"
    bl_idname = "pie.pie_align_active_left"
    bl_description = "Aligns view to active object left"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.view3d.view_axis(type='LEFT', align_active=True)
        self.report({'INFO'}, bl_info.get('name') + ': Aligned view to active object left')
        return {'FINISHED'}
        
class pie_align_active_front(Operator):
    bl_label = "Front"
    bl_idname = "pie.pie_align_active_front"
    bl_description = "Aligns view to active object front"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.view3d.view_axis(type='FRONT', align_active=True)
        self.report({'INFO'}, bl_info.get('name') + ': Aligned view to active object front')
        return {'FINISHED'}
        
class pie_align_active_back(Operator):
    bl_label = "Back"
    bl_idname = "pie.pie_align_active_back"
    bl_description = "Aligns view to active object back"

    def execute(self, context):
        if bpy.context.active_object == None:
            self.report({'ERROR'}, bl_info.get('name') + ': Please select an object first')
            return {'FINISHED'}
        bpy.context.active_object.select_set(True)

        if bpy.context.active_object.mode != 'SCULPT' and bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.view3d.view_axis(type='BACK', align_active=True)
        self.report({'INFO'}, bl_info.get('name') + ': Aligned view to active object back')
        return {'FINISHED'}
        
class pie_align_active_perspective(Operator):
    bl_label = "Perspective / Orthographic"
    bl_idname = "pie.pie_align_active_perspective"
    bl_description = "Toggles perspective / authographic mode"

    def execute(self, context):
        bpy.ops.view3d.view_persportho()
        self.report({'INFO'}, bl_info.get('name') + ': Toggled perspective / authographic mode')
        return {'FINISHED'}
