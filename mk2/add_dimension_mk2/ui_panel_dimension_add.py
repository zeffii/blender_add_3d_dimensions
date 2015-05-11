import bpy


# Properties class
class DimensionAdd(bpy.types.Panel):
    ''''''
    bl_idname = "VIEW3D_PT_properties_dimension_add"
    bl_label = "Dimension Add"
    bl_description = "Dimension Add"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        selected = 0
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                for i in obj.data.vertices:
                    if i.select:
                        selected += 1

            if obj.type == 'CURVE':
                for i in obj.data.splines:
                    for j in i.bezier_points:
                        if j.select_control_point:
                            selected += 1

        if selected in {1, 2, 3}:
            return True

    def draw(self, context):
        vertex = []
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                for i in obj.data.vertices:
                    if i.select:
                        vertex.append(obj.matrix_world * i.co)

            if obj.type == 'CURVE':
                for i in obj.data.splines:
                    for j in i.bezier_points:
                        if j.select_control_point:
                            vertex.append(obj.matrix_world * j.co)

        if len(vertex) == 1:
            startvertex = vertex[0]
            endvertex = bpy.context.scene.cursor_location
            layout = self.layout
            col = layout.column()
            col.label("Note:")
            row = layout.row()
            props1 = row.operator("curve.dimension", text='Add linear note')
            props1.Dimension_Change = False
            props1.Dimension_Type = 'Note'
            props1.Dimension_width_or_location = 'location'
            props1.Dimension_startlocation = startvertex
            props1.Dimension_liberty = '2D'
            props1.Dimension_rotation = 0

            props2 = row.operator("curve.dimension", text='Add 3D note')
            props2.Dimension_Change = False
            props2.Dimension_Type = 'Note'
            props2.Dimension_width_or_location = 'location'
            props2.Dimension_startlocation = startvertex
            props2.Dimension_liberty = '3D'
            props2.Dimension_rotation = 0

            col = layout.column()
            col.label("Distance to 3D cursor:")
            row = layout.row()
            props3 = row.operator("curve.dimension", text='Add linear dimension')
            props3.Dimension_Change = False
            props3.Dimension_Type = 'Linear-1'
            props3.Dimension_width_or_location = 'location'
            props3.Dimension_startlocation = endvertex
            props3.Dimension_endlocation = startvertex
            props3.Dimension_liberty = '2D'
            props3.Dimension_rotation = 0

            props4 = row.operator("curve.dimension", text='Add 3D dimension')
            props4.Dimension_Change = False
            props4.Dimension_Type = 'Linear-1'
            props4.Dimension_width_or_location = 'location'
            props4.Dimension_startlocation = endvertex
            props4.Dimension_endlocation = startvertex
            props4.Dimension_liberty = '3D'
            props4.Dimension_rotation = 0

            col = layout.column()
            col.label("Radius to 3D cursor:")
            row = layout.row()
            props7 = row.operator("curve.dimension", text='Add linear radius')
            props7.Dimension_Change = False
            props7.Dimension_Type = 'Radius'
            props7.Dimension_width_or_location = 'location'
            props7.Dimension_startlocation = endvertex
            props7.Dimension_endlocation = startvertex
            props7.Dimension_liberty = '2D'
            props7.Dimension_rotation = 0

            props8 = row.operator("curve.dimension", text='Add 3D radius')
            props8.Dimension_Change = False
            props8.Dimension_Type = 'Radius'
            props8.Dimension_width_or_location = 'location'
            props8.Dimension_startlocation = endvertex
            props8.Dimension_endlocation = startvertex
            props8.Dimension_liberty = '3D'
            props8.Dimension_rotation = 0

            col = layout.column()
            col.label("Diameter to 3D cursor:")
            row = layout.row()
            props9 = row.operator("curve.dimension", text='Add linear diameter')
            props9.Dimension_Change = False
            props9.Dimension_Type = 'Diameter'
            props9.Dimension_width_or_location = 'location'
            props9.Dimension_startlocation = endvertex
            props9.Dimension_endlocation = startvertex
            props9.Dimension_liberty = '2D'
            props9.Dimension_rotation = 0

            props10 = row.operator("curve.dimension", text='Add 3D diameter')
            props10.Dimension_Change = False
            props10.Dimension_Type = 'Diameter'
            props10.Dimension_width_or_location = 'location'
            props10.Dimension_startlocation = endvertex
            props10.Dimension_endlocation = startvertex
            props10.Dimension_liberty = '3D'
            props10.Dimension_rotation = 0

        if len(vertex) == 2:
            startvertex = vertex[0]
            endvertex = vertex[1]
            if endvertex[0] < startvertex[0]:
                startvertex = vertex[1]
                endvertex = vertex[0]

            layout = self.layout
            col = layout.column()
            col.label("Distance:")
            row = layout.row()
            props1 = row.operator("curve.dimension", text='Add linear dimension')
            props1.Dimension_Change = False
            props1.Dimension_Type = 'Linear-1'
            props1.Dimension_width_or_location = 'location'
            props1.Dimension_startlocation = startvertex
            props1.Dimension_endlocation = endvertex
            props1.Dimension_liberty = '2D'
            props1.Dimension_rotation = 0

            props2 = row.operator("curve.dimension", text='Add 3D dimension')
            props2.Dimension_Change = False
            props2.Dimension_Type = 'Linear-1'
            props2.Dimension_width_or_location = 'location'
            props2.Dimension_startlocation = startvertex
            props2.Dimension_endlocation = endvertex
            props2.Dimension_liberty = '3D'
            props2.Dimension_rotation = 0

            col = layout.column()
            col.label("Radius:")
            row = layout.row()
            props3 = row.operator("curve.dimension", text='Add linear radius')
            props3.Dimension_Change = False
            props3.Dimension_Type = 'Radius'
            props3.Dimension_width_or_location = 'location'
            props3.Dimension_startlocation = startvertex
            props3.Dimension_endlocation = endvertex
            props3.Dimension_liberty = '2D'
            props3.Dimension_rotation = 0

            props4 = row.operator("curve.dimension", text='Add 3D radius')
            props4.Dimension_Change = False
            props4.Dimension_Type = 'Radius'
            props4.Dimension_width_or_location = 'location'
            props4.Dimension_startlocation = startvertex
            props4.Dimension_endlocation = endvertex
            props4.Dimension_liberty = '3D'
            props4.Dimension_rotation = 0

            col = layout.column()
            col.label("Diameter:")
            row = layout.row()
            props5 = row.operator("curve.dimension", text='Add linear diameter')
            props5.Dimension_Change = False
            props5.Dimension_Type = 'Diameter'
            props5.Dimension_width_or_location = 'location'
            props5.Dimension_startlocation = startvertex
            props5.Dimension_endlocation = endvertex
            props5.Dimension_liberty = '2D'
            props5.Dimension_rotation = 0

            props6 = row.operator("curve.dimension", text='Add 3D diameter')
            props6.Dimension_Change = False
            props6.Dimension_Type = 'Diameter'
            props6.Dimension_width_or_location = 'location'
            props6.Dimension_startlocation = startvertex
            props6.Dimension_endlocation = endvertex
            props6.Dimension_liberty = '3D'
            props6.Dimension_rotation = 0

        if len(vertex) == 3:
            startvertex = vertex[0]
            endvertex = vertex[1]
            endanglevertex = vertex[2]
            if endvertex[0] < startvertex[0]:
                startvertex = vertex[1]
                endvertex = vertex[0]

            layout = self.layout
            col = layout.column()
            col.label("Angle:")
            row = layout.row()
            props1 = row.operator("curve.dimension", text='Add Linear angle dimension')
            props1.Dimension_Change = False
            props1.Dimension_Type = 'Angular1'
            props1.Dimension_width_or_location = 'location'
            props1.Dimension_startlocation = startvertex
            props1.Dimension_endlocation = endvertex
            props1.Dimension_endanglelocation = endanglevertex
            props1.Dimension_liberty = '2D'
            props1.Dimension_rotation = 0

            props2 = row.operator("curve.dimension", text='Add 3D angle dimension')
            props2.Dimension_Change = False
            props2.Dimension_Type = 'Angular1'
            props2.Dimension_width_or_location = 'location'
            props2.Dimension_startlocation = startvertex
            props2.Dimension_endlocation = endvertex
            props2.Dimension_endanglelocation = endanglevertex
            props2.Dimension_liberty = '3D'
            props2.Dimension_rotation = 0


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)
