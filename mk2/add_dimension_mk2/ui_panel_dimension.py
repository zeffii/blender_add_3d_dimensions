import bpy
from bpy.props import (
    BoolProperty,
    StringProperty,
    EnumProperty,
    FloatVectorProperty,
    FloatProperty,
    IntProperty
)


# Properties class
class DimensionPanel(bpy.types.Panel):
    ''''''
    bl_idname = "OBJECT_PT_properties_dimension"
    bl_label = "Dimension change"
    bl_description = "Dimension change"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        if context.object.Dimension:
            return (context.object)

    def draw(self, context):
        if context.object.Dimension:
            layout = self.layout

            obj = context.object
            row = layout.row()

            props = row.operator("curve.dimension", text='Change')
            props.Dimension_Change = True
            props.Dimension_Delete = obj.name
            props.Dimension_startlocation = obj.location

            # could be setattrd ?
            props.Dimension_width_or_location = obj.Dimension_width_or_location
            props.Dimension_endlocation = obj.Dimension_endlocation
            props.Dimension_endanglelocation = obj.Dimension_endanglelocation
            props.Dimension_liberty = obj.Dimension_liberty
            props.Dimension_Type = obj.Dimension_Type
            props.Dimension_XYZType = obj.Dimension_XYZType
            props.Dimension_XYType = obj.Dimension_XYType
            props.Dimension_XZType = obj.Dimension_XZType
            props.Dimension_YZType = obj.Dimension_YZType
            props.Dimension_resolution = obj.Dimension_resolution
            props.Dimension_width = obj.Dimension_width
            props.Dimension_length = obj.Dimension_length
            props.Dimension_dsize = obj.Dimension_dsize
            props.Dimension_depth = obj.Dimension_depth
            props.Dimension_depth_from_center = obj.Dimension_depth_from_center
            props.Dimension_angle = obj.Dimension_angle
            props.Dimension_rotation = obj.Dimension_rotation
            props.Dimension_textsize = obj.Dimension_textsize
            props.Dimension_textdepth = obj.Dimension_textdepth
            props.Dimension_textround = obj.Dimension_textround
            props.Dimension_matname = obj.Dimension_matname
            props.Dimension_note = obj.Dimension_note
            props.Dimension_align_to_camera = obj.Dimension_align_to_camera
            props.Dimension_arrow = obj.Dimension_arrow
            props.Dimension_arrowdepth = obj.Dimension_arrowdepth
            props.Dimension_arrowlength = obj.Dimension_arrowlength


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)
