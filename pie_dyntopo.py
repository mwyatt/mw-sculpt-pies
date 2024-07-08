import bpy
from bpy.types import Menu, Operator
from . bl_info import *
from . rotation_copy import copyRotation

class MWSCULPTPIES_MT_PIE_DYNTOPO(Menu):
    bl_label = "Modifier"
    bl_idname = "MWSCULPTPIES_MT_PIE_DYNTOPO"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("pie.pie_dyntopo_enable", icon='MOD_BEVEL')
        pie.operator("pie.pie_dyntopo_disable", icon='MOD_BEVEL')
        pie.operator("pie.pie_dyntopo_flood", icon='MOD_BEVEL')
        pie.operator("pie.pie_dyntopo_res_1", icon='MOD_BEVEL')
        pie.operator("pie.pie_dyntopo_res_3", icon='MOD_BEVEL')
        pie.operator("pie.pie_dyntopo_res_5", icon='MOD_BEVEL')
        pie.operator("pie.pie_dyntopo_res_7", icon='MOD_BEVEL')
        pie.operator("pie.pie_dyntopo_res_9", icon='MOD_BEVEL')

class pie_dyntopo_enable(Operator):
    bl_label = "Dyntopo On"
    bl_idname = "pie.pie_dyntopo_enable"
    bl_description = "Turns on dynamic topology"

    def execute(self, context):

        # Must be in sculpt mode.
        if bpy.context.active_object.mode != 'SCULPT':
            self.report({'ERROR'}, bl_info.get('name') + ': Please enter sculpt mode first')
            return {'FINISHED'}

        if bpy.context.view_layer.objects.active.use_dynamic_topology_sculpting == False:
            bpy.ops.sculpt.dynamic_topology_toggle()

        self.report({'INFO'}, bl_info.get('name') + ': Dynamic topology enabled')
        return {'FINISHED'}

class pie_dyntopo_disable(Operator):
    bl_label = "Dyntopo Off"
    bl_idname = "pie.pie_dyntopo_disable"
    bl_description = "Turns off dynamic topology"

    def execute(self, context):

        # Must be in sculpt mode.
        if bpy.context.active_object.mode != 'SCULPT':
            self.report({'ERROR'}, bl_info.get('name') + ': Please enter sculpt mode first')
            return {'FINISHED'}

        if bpy.context.view_layer.objects.active.use_dynamic_topology_sculpting == True:
            bpy.ops.sculpt.dynamic_topology_toggle()

        self.report({'INFO'}, bl_info.get('name') + ': Dynamic topology disabled')
        return {'FINISHED'}

class pie_dyntopo_flood(Operator):
    bl_label = "Flood Fill"
    bl_idname = "pie.pie_dyntopo_flood"
    bl_description = "Flood Fill at current resolution"

    def execute(self, context):

        # Must be in sculpt mode.
        if bpy.context.active_object.mode != 'SCULPT':
            self.report({'ERROR'}, bl_info.get('name') + ': Please enter sculpt mode first')
            return {'FINISHED'}

        if bpy.context.view_layer.objects.active.use_dynamic_topology_sculpting == False:
            bpy.ops.sculpt.dynamic_topology_toggle()

        bpy.ops.sculpt.detail_flood_fill()

        self.report({'INFO'}, bl_info.get('name') + ': Flood filled')
        return {'FINISHED'}

class pie_dyntopo_res_5(Operator):
    bl_label = "5"
    bl_idname = "pie.pie_dyntopo_res_5"
    bl_description = "Set resolution"

    def execute(self, context):
        # Must be in sculpt mode.
        if bpy.context.active_object.mode != 'SCULPT':
            self.report({'ERROR'}, bl_info.get('name') + ': Please enter sculpt mode first')
            return {'FINISHED'}
        bpy.data.scenes[0].tool_settings.sculpt.constant_detail_resolution = 5
        self.report({'INFO'}, bl_info.get('name') + ': Resolution set')
        return {'FINISHED'}

class pie_dyntopo_res_1(Operator):
    bl_label = "1"
    bl_idname = "pie.pie_dyntopo_res_1"
    bl_description = "Set resolution"

    def execute(self, context):
        # Must be in sculpt mode.
        if bpy.context.active_object.mode != 'SCULPT':
            self.report({'ERROR'}, bl_info.get('name') + ': Please enter sculpt mode first')
            return {'FINISHED'}
        bpy.data.scenes[0].tool_settings.sculpt.constant_detail_resolution = 1
        self.report({'INFO'}, bl_info.get('name') + ': Resolution set')
        return {'FINISHED'}

class pie_dyntopo_res_3(Operator):
    bl_label = "3"
    bl_idname = "pie.pie_dyntopo_res_3"
    bl_description = "Set resolution"

    def execute(self, context):
        # Must be in sculpt mode.
        if bpy.context.active_object.mode != 'SCULPT':
            self.report({'ERROR'}, bl_info.get('name') + ': Please enter sculpt mode first')
            return {'FINISHED'}
        bpy.data.scenes[0].tool_settings.sculpt.constant_detail_resolution = 3
        self.report({'INFO'}, bl_info.get('name') + ': Resolution set')
        return {'FINISHED'}

class pie_dyntopo_res_7(Operator):
    bl_label = "7"
    bl_idname = "pie.pie_dyntopo_res_7"
    bl_description = "Set resolution"

    def execute(self, context):
        # Must be in sculpt mode.
        if bpy.context.active_object.mode != 'SCULPT':
            self.report({'ERROR'}, bl_info.get('name') + ': Please enter sculpt mode first')
            return {'FINISHED'}
        bpy.data.scenes[0].tool_settings.sculpt.constant_detail_resolution = 7
        self.report({'INFO'}, bl_info.get('name') + ': Resolution set')
        return {'FINISHED'}

class pie_dyntopo_res_9(Operator):
    bl_label = "9"
    bl_idname = "pie.pie_dyntopo_res_9"
    bl_description = "Set resolution"

    def execute(self, context):
        # Must be in sculpt mode.
        if bpy.context.active_object.mode != 'SCULPT':
            self.report({'ERROR'}, bl_info.get('name') + ': Please enter sculpt mode first')
            return {'FINISHED'}
        bpy.data.scenes[0].tool_settings.sculpt.constant_detail_resolution = 9
        self.report({'INFO'}, bl_info.get('name') + ': Resolution set')
        return {'FINISHED'}
