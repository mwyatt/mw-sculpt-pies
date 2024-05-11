import bpy
from bpy.types import Menu, Operator
from . bl_info import *
from . rotation_copy import copyRotation

class pie_create(Menu):
    bl_label = "Create"
    bl_idname = "mw_sculpt_pie.create"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("pie.pie_create_cube", icon='MESH_CUBE')
        pie.operator("pie.pie_create_sphere", icon='MESH_UVSPHERE')
        pie.operator("pie.pie_create_cylinder", icon='MESH_CYLINDER')
        pie.operator("pie.pie_create_cone", icon='MESH_CONE')

class pie_create_cube(Operator):
    bl_label = "Cube"
    bl_idname = "pie.pie_create_cube"
    bl_description = "Creates a cube in the location of the selected object."

    def execute(self, context):
        if bpy.context.active_object != None:
            og_obj = bpy.context.active_object
            if bpy.context.active_object.mode != 'OBJECT':
                bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.mesh.primitive_cube_add(size=5, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.ops.view3d.snap_selected_to_cursor()
        if 'og_obj' in locals():
            copyRotation(bpy.context.active_object, og_obj, context)
        self.report({'INFO'}, bl_info.get('name') + ': Cube created')
        return {'FINISHED'}

class pie_create_sphere(Operator):
    bl_label = "Sphere"
    bl_idname = "pie.pie_create_sphere"
    bl_description = "Creates a sphere."

    def execute(self, context):
        if bpy.context.active_object != None:
            og_obj = bpy.context.active_object
            if bpy.context.active_object.mode != 'OBJECT':
                bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.mesh.primitive_uv_sphere_add(radius=2.5, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.ops.view3d.snap_selected_to_cursor()
        if 'og_obj' in locals():
            copyRotation(bpy.context.active_object, og_obj, context)
        self.report({'INFO'}, bl_info.get('name') + ': Sphere created')
        return {'FINISHED'}
   
class pie_create_cylinder(Operator):
    bl_label = "Cylinder"
    bl_idname = "pie.pie_create_cylinder"
    bl_description = "Creates a cylinder."

    def execute(self, context):
        if bpy.context.active_object != None:
            og_obj = bpy.context.active_object
            if bpy.context.active_object.mode != 'OBJECT':
                bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.mesh.primitive_cylinder_add(radius=2.5, depth=5, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.ops.view3d.snap_selected_to_cursor()
        if 'og_obj' in locals():
            copyRotation(bpy.context.active_object, og_obj, context)
        self.report({'INFO'}, bl_info.get('name') + ': Cylinder created')
        return {'FINISHED'}

class pie_create_cone(Operator):
    bl_label = "Cone"
    bl_idname = "pie.pie_create_cone"
    bl_description = "Creates a cone."

    def execute(self, context):
        if bpy.context.active_object != None:
            og_obj = bpy.context.active_object
            if bpy.context.active_object.mode != 'OBJECT':
                bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.mesh.primitive_cone_add(radius1=2.5, radius2=0, depth=5, enter_editmode=False, align='WORLD', location=(-10.1265, -1.28029, 34.9788), scale=(1, 1, 1))
        bpy.ops.view3d.snap_selected_to_cursor()
        if 'og_obj' in locals():
            copyRotation(bpy.context.active_object, og_obj, context)
        self.report({'INFO'}, bl_info.get('name') + ': Cone created')
        return {'FINISHED'}
