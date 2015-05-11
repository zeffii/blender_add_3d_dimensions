import bpy
from bpy.props import (
    BoolProperty,
    StringProperty,
    EnumProperty,
    FloatVectorProperty,
    FloatProperty,
    IntProperty
)
import mathutils
from mathutils import *

from add_dimension import main


class Dimension(bpy.types.Operator):

    bl_idname = "curve.dimension"
    bl_label = "Dimension"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "add dimension"

    # align_matrix for the invoke
    align_matrix = Matrix()

    Dimension = BoolProperty(
        name="Dimension",
        default=True,
        description="dimension")

    # change properties
    Dimension_Name = StringProperty(
        name="Name",
        description="Name")

    Dimension_Change = BoolProperty(
        name="Change",
        default=False,
        description="change dimension")

    Dimension_Delete = StringProperty(
        name="Delete",
        description="Delete dimension")

    # general properties
    Types = [
        ('Linear-1', 'Linear-1', 'Linear-1'),
        ('Linear-2', 'Linear-2', 'Linear-2'),
        ('Linear-3', 'Linear-3', 'Linear-3'),
        ('Radius', 'Radius', 'Radius'),
        ('Diameter', 'Diameter', 'Diameter'),
        ('Angular1', 'Angular1', 'Angular1'),
        ('Angular2', 'Angular2', 'Angular2'),
        ('Angular3', 'Angular3', 'Angular3'),
        ('Note', 'Note', 'Note')]
    Dimension_Type = EnumProperty(
        name="Type",
        description="Form of Curve to create",
        items=Types)

    XYZTypes = [
        ('TOP', 'Top', 'TOP'),
        ('FRONT', 'Front', 'FRONT'),
        ('RIGHT', 'Right', 'RIGHT'),
        ('BOTTOM', 'Bottom', 'BOTTOM'),
        ('BACK', 'Back', 'BACK'),
        ('LEFT', 'Left', 'LEFT')]
    Dimension_XYZType = EnumProperty(
        name="Coordinate system",
        description="Place in a coordinate system",
        items=XYZTypes)

    XYTypes = [
        ('X', 'X', 'X'),
        ('Y', 'Y', 'Y')]
    Dimension_XYType = EnumProperty(
        name="XY",
        description="XY",
        items=XYTypes)

    XZTypes = [
        ('X', 'X', 'X'),
        ('Z', 'Z', 'Z')]
    Dimension_XZType = EnumProperty(
        name="XZ",
        description="XZ",
        items=XZTypes)

    YZTypes = [
        ('Y', 'Y', 'Y'),
        ('Z', 'Z', 'Z')]
    Dimension_YZType = EnumProperty(
        name="YZ",
        description="YZ",
        items=YZTypes)

    Dimension_startlocation = FloatVectorProperty(
        name="",
        description="Start location",
        default=(0.0, 0.0, 0.0),
        subtype='XYZ')

    Dimension_endlocation = FloatVectorProperty(
        name="",
        description="End location",
        default=(2.0, 2.0, 2.0),
        subtype='XYZ')

    Dimension_endanglelocation = FloatVectorProperty(
        name="",
        description="End angle location",
        default=(4.0, 4.0, 4.0),
        subtype='XYZ')

    width_or_location_items = [
        ('width', 'width', 'width'),
        ('location', 'location', 'location')]
    Dimension_width_or_location = EnumProperty(
        name="width or location",
        items=width_or_location_items,
        description="width or location")

    libertyItems = [
        ('2D', '2D', '2D'),
        ('3D', '3D', '3D')]
    Dimension_liberty = EnumProperty(
        name="2D / 3D",
        items=libertyItems,
        description="2D or 3D Dimension")

    # Arrow
    Arrows = [
        ('Arrow1', 'Arrow1', 'Arrow1'),
        ('Arrow2', 'Arrow2', 'Arrow2'),
        ('Serifs1', 'Serifs1', 'Serifs1'),
        ('Serifs2', 'Serifs2', 'Serifs2'),
        ('Without', 'Without', 'Without')]
    Dimension_arrow = EnumProperty(
        name="Arrow",
        items=Arrows,
        description="Arrow")
    Dimension_arrowdepth = FloatProperty(
        name="Depth",
        default=0.1,
        min=0, soft_min=0,
        description="Arrow depth")
    Dimension_arrowlength = FloatProperty(
        name="Length",
        default=0.25,
        min=0, soft_min=0,
        description="Arrow length")

    # Dimension properties
    Dimension_resolution = IntProperty(
        name="Resolution",
        default=10,
        min=1, soft_min=1,
        description="Resolution")
    Dimension_width = FloatProperty(
        name="Width",
        default=2,
        unit='LENGTH',
        description="Width")
    Dimension_length = FloatProperty(
        name="Length",
        default=2,
        description="Length")
    Dimension_dsize = FloatProperty(
        name="Size",
        default=1,
        min=0, soft_min=0,
        description="Size")

    Dimension_depth = FloatProperty(
        name="Depth",
        default=0.1,
        min=0, soft_min=0,
        description="Depth")
    Dimension_depth_from_center = BoolProperty(
        name="Depth from center",
        default=False,
        description="Depth from center")
    Dimension_angle = FloatProperty(
        name="Angle",
        default=45,
        description="Angle")
    Dimension_rotation = FloatProperty(
        name="Rotation",
        default=0,
        description="Rotation")

    # Dimension units properties
    Units = [
        ('None', 'None', 'None'),
        ('\u00b5m', '\u00b5m', '\u00b5m'),
        ('mm', 'mm', 'mm'),
        ('cm', 'cm', 'cm'),
        ('m', 'm', 'm'),
        ('km', 'km', 'km'),
        ('thou', 'thou', 'thou'),
        ('"', '"', '"'),
        ('\'', '\'', '\''),
        ('yd', 'yd', 'yd'),
        ('mi', 'mi', 'mi')]
    Dimension_units = EnumProperty(
        name="Units",
        items=Units,
        description="Units")

    # Dimension text properties
    Dimension_textsize = FloatProperty(
        name="Size",
        default=1,
        description="Size")
    Dimension_textdepth = FloatProperty(
        name="Depth",
        default=0.2,
        description="Depth")
    Dimension_textround = IntProperty(
        name="Rounding",
        default=2,
        min=0, soft_min=0,
        description="Rounding")
    Dimension_font = StringProperty(
        name="Font",
        default='',
        subtype='FILE_PATH',
        description="Font")

    # Materials properties
    Dimension_matname = StringProperty(
        name="Name",
        default='Dimension_Red',
        description="Material name")

    # Note properties
    Dimension_note = StringProperty(
        name="Note",
        default='Note',
        description="Note text")

    Dimension_align_to_camera = BoolProperty(
        name="Align to camera",
        default=False,
        description="Align to camera")

    TMP_startlocation = FloatVectorProperty(
        name="",
        description="Start location",
        default=(0.0, 0.0, 0.0),
        subtype='XYZ')

    TMP_endlocation = FloatVectorProperty(
        name="",
        description="Start location",
        default=(2.0, 2.0, 2.0),
        subtype='XYZ')
    TMP_endanglelocation = FloatVectorProperty(
        name="",
        description="Start location",
        default=(4.0, 4.0, 4.0),
        subtype='XYZ')

    def draw(self, context):
        layout = self.layout

        # general options
        col = layout.column()
        col.prop(self, 'Dimension_Type')

        # options per Type Linear-1(width = 2, length = 2, dsize = 1, depth =
        # 0.1)
        if self.Dimension_Type == 'Linear-1':
            row = layout.row()
            row.prop(self, 'Dimension_width_or_location', expand=True)
            col = layout.column()
            col.label(text="End location:")
            row = layout.row()
            if self.Dimension_width_or_location == 'width':
                row.prop(self, 'Dimension_width')
            else:
                row.prop(self, 'Dimension_endlocation')
            box = layout.box()
            box.label("Options")
            box.prop(self, 'Dimension_length')
            box.prop(self, 'Dimension_dsize')
            box.prop(self, 'Dimension_depth')
            box.prop(self, 'Dimension_depth_from_center')
            box.prop(self, 'Dimension_rotation')

        # options per Type Linear-2(width = 2, dsize = 1, depth = 0.1)
        if self.Dimension_Type == 'Linear-2':
            row = layout.row()
            row.prop(self, 'Dimension_width_or_location', expand=True)
            col = layout.column()
            col.label(text="End location:")
            row = layout.row()
            if self.Dimension_width_or_location == 'width':
                row.prop(self, 'Dimension_width')
            else:
                row.prop(self, 'Dimension_endlocation')
            box = layout.box()
            box.label("Options")
            box.prop(self, 'Dimension_dsize')
            box.prop(self, 'Dimension_depth')
            box.prop(self, 'Dimension_rotation')

        # options per Type Linear-3(width = 2, length = 2, dsize = 1, depth =
        # 0.1)
        if self.Dimension_Type == 'Linear-3':
            row = layout.row()
            row.prop(self, 'Dimension_width_or_location', expand=True)
            col = layout.column()
            col.label(text="End location:")
            row = layout.row()
            if self.Dimension_width_or_location == 'width':
                row.prop(self, 'Dimension_width')
            else:
                row.prop(self, 'Dimension_endlocation')
            box = layout.box()
            box.label("Options")
            box.prop(self, 'Dimension_length')
            box.prop(self, 'Dimension_dsize')
            box.prop(self, 'Dimension_depth')
            box.prop(self, 'Dimension_depth_from_center')
            box.prop(self, 'Dimension_rotation')

        # options per Type Radius(width = 2, length = 2, dsize = 1, depth =
        # 0.1)
        if self.Dimension_Type == 'Radius':
            row = layout.row()
            row.prop(self, 'Dimension_width_or_location', expand=True)
            col = layout.column()
            col.label(text="End location:")
            row = layout.row()
            if self.Dimension_width_or_location == 'width':
                row.prop(self, 'Dimension_width')
            else:
                row.prop(self, 'Dimension_endlocation')
            box = layout.box()
            box.label("Options")
            box.prop(self, 'Dimension_length')
            box.prop(self, 'Dimension_dsize')
            box.prop(self, 'Dimension_depth')
            box.prop(self, 'Dimension_rotation')

        # options per Type Diameter(width = 2, length = 2, dsize = 1, depth =
        # 0.1)
        if self.Dimension_Type == 'Diameter':
            row = layout.row()
            row.prop(self, 'Dimension_width_or_location', expand=True)
            col = layout.column()
            col.label(text="End location:")
            row = layout.row()
            if self.Dimension_width_or_location == 'width':
                row.prop(self, 'Dimension_width')
            else:
                row.prop(self, 'Dimension_endlocation')
            box = layout.box()
            box.label("Options")
            box.prop(self, 'Dimension_length')
            box.prop(self, 'Dimension_dsize')
            box.prop(self, 'Dimension_depth')
            box.prop(self, 'Dimension_rotation')

        # options per Type Angular1(width = 2, dsize = 1, depth = 0.1, angle =
        # 45)
        if self.Dimension_Type == 'Angular1':
            row = layout.row()
            row.prop(self, 'Dimension_width_or_location', expand=True)
            col = layout.column()
            col.label(text="End location:")
            row = layout.row()
            if self.Dimension_width_or_location == 'width':
                row.prop(self, 'Dimension_angle')
            else:
                row.prop(self, 'Dimension_endlocation')
                col = layout.column()
                col.label(text="End angle location:")
                row = layout.row()
                row.prop(self, 'Dimension_endanglelocation')
                row = layout.row()
                props = row.operator("curve.dimension", text='Change angle')
                props.Dimension_Change = True
                props.Dimension_Delete = self.Dimension_Name
                props.Dimension_width_or_location = self.Dimension_width_or_location
                props.Dimension_startlocation = self.Dimension_endanglelocation
                props.Dimension_endlocation = self.Dimension_startlocation
                props.Dimension_endanglelocation = self.Dimension_endlocation
                props.Dimension_liberty = self.Dimension_liberty
                props.Dimension_Type = self.Dimension_Type
                props.Dimension_XYZType = self.Dimension_XYZType
                props.Dimension_XYType = self.Dimension_XYType
                props.Dimension_XZType = self.Dimension_XZType
                props.Dimension_YZType = self.Dimension_YZType
                props.Dimension_resolution = self.Dimension_resolution
                props.Dimension_width = self.Dimension_width
                props.Dimension_length = self.Dimension_length
                props.Dimension_dsize = self.Dimension_dsize
                props.Dimension_depth = self.Dimension_depth
                props.Dimension_depth_from_center = self.Dimension_depth_from_center
                props.Dimension_angle = self.Dimension_angle
                props.Dimension_rotation = self.Dimension_rotation
                props.Dimension_textsize = self.Dimension_textsize
                props.Dimension_textdepth = self.Dimension_textdepth
                props.Dimension_textround = self.Dimension_textround
                props.Dimension_matname = self.Dimension_matname
                props.Dimension_note = self.Dimension_note
                props.Dimension_align_to_camera = self.Dimension_align_to_camera
                props.Dimension_arrow = self.Dimension_arrow
                props.Dimension_arrowdepth = self.Dimension_arrowdepth
                props.Dimension_arrowlength = self.Dimension_arrowlength
            box = layout.box()
            box.label("Options")
            box.prop(self, 'Dimension_width')
            box.prop(self, 'Dimension_length')
            box.prop(self, 'Dimension_depth')
            box.prop(self, 'Dimension_depth_from_center')
            box.prop(self, 'Dimension_rotation')
            box.prop(self, 'Dimension_resolution')

        # options per Type Angular2(width = 2, dsize = 1, depth = 0.1, angle =
        # 45)
        if self.Dimension_Type == 'Angular2':
            row = layout.row()
            row.prop(self, 'Dimension_width_or_location', expand=True)
            col = layout.column()
            col.label(text="End location:")
            row = layout.row()
            if self.Dimension_width_or_location == 'width':
                row.prop(self, 'Dimension_angle')
            else:
                row.prop(self, 'Dimension_endlocation')
                col = layout.column()
                col.label(text="End angle location:")
                row = layout.row()
                row.prop(self, 'Dimension_endanglelocation')
                row = layout.row()
                props = row.operator("curve.dimension", text='Change angle')
                props.Dimension_Change = True
                props.Dimension_Delete = self.Dimension_Name
                props.Dimension_width_or_location = self.Dimension_width_or_location
                props.Dimension_startlocation = self.Dimension_endanglelocation
                props.Dimension_endlocation = self.Dimension_startlocation
                props.Dimension_endanglelocation = self.Dimension_endlocation
                props.Dimension_liberty = self.Dimension_liberty
                props.Dimension_Type = self.Dimension_Type
                props.Dimension_XYZType = self.Dimension_XYZType
                props.Dimension_XYType = self.Dimension_XYType
                props.Dimension_XZType = self.Dimension_XZType
                props.Dimension_YZType = self.Dimension_YZType
                props.Dimension_resolution = self.Dimension_resolution
                props.Dimension_width = self.Dimension_width
                props.Dimension_length = self.Dimension_length
                props.Dimension_dsize = self.Dimension_dsize
                props.Dimension_depth = self.Dimension_depth
                props.Dimension_depth_from_center = self.Dimension_depth_from_center
                props.Dimension_angle = self.Dimension_angle
                props.Dimension_rotation = self.Dimension_rotation
                props.Dimension_textsize = self.Dimension_textsize
                props.Dimension_textdepth = self.Dimension_textdepth
                props.Dimension_textround = self.Dimension_textround
                props.Dimension_matname = self.Dimension_matname
                props.Dimension_note = self.Dimension_note
                props.Dimension_align_to_camera = self.Dimension_align_to_camera
                props.Dimension_arrow = self.Dimension_arrow
                props.Dimension_arrowdepth = self.Dimension_arrowdepth
                props.Dimension_arrowlength = self.Dimension_arrowlength
            box = layout.box()
            box.label("Options")
            box.prop(self, 'Dimension_width')
            box.prop(self, 'Dimension_depth')
            box.prop(self, 'Dimension_rotation')
            box.prop(self, 'Dimension_resolution')

        # options per Type Angular3(width = 2, dsize = 1, depth = 0.1, angle =
        # 45)
        if self.Dimension_Type == 'Angular3':
            row = layout.row()
            row.prop(self, 'Dimension_width_or_location', expand=True)
            col = layout.column()
            col.label(text="End location:")
            row = layout.row()
            if self.Dimension_width_or_location == 'width':
                row.prop(self, 'Dimension_angle')
            else:
                row.prop(self, 'Dimension_endlocation')
                col = layout.column()
                col.label(text="End angle location:")
                row = layout.row()
                row.prop(self, 'Dimension_endanglelocation')
                row = layout.row()
                props = row.operator("curve.dimension", text='Change angle')
                props.Dimension_Change = True
                props.Dimension_Delete = self.Dimension_Name
                props.Dimension_width_or_location = self.Dimension_width_or_location
                props.Dimension_startlocation = self.Dimension_endanglelocation
                props.Dimension_endlocation = self.Dimension_startlocation
                props.Dimension_endanglelocation = self.Dimension_endlocation
                props.Dimension_liberty = self.Dimension_liberty
                props.Dimension_Type = self.Dimension_Type
                props.Dimension_XYZType = self.Dimension_XYZType
                props.Dimension_XYType = self.Dimension_XYType
                props.Dimension_XZType = self.Dimension_XZType
                props.Dimension_YZType = self.Dimension_YZType
                props.Dimension_resolution = self.Dimension_resolution
                props.Dimension_width = self.Dimension_width
                props.Dimension_length = self.Dimension_length
                props.Dimension_dsize = self.Dimension_dsize
                props.Dimension_depth = self.Dimension_depth
                props.Dimension_depth_from_center = self.Dimension_depth_from_center
                props.Dimension_angle = self.Dimension_angle
                props.Dimension_rotation = self.Dimension_rotation
                props.Dimension_textsize = self.Dimension_textsize
                props.Dimension_textdepth = self.Dimension_textdepth
                props.Dimension_textround = self.Dimension_textround
                props.Dimension_matname = self.Dimension_matname
                props.Dimension_note = self.Dimension_note
                props.Dimension_align_to_camera = self.Dimension_align_to_camera
                props.Dimension_arrow = self.Dimension_arrow
                props.Dimension_arrowdepth = self.Dimension_arrowdepth
                props.Dimension_arrowlength = self.Dimension_arrowlength
            box = layout.box()
            box.label("Options")
            box.prop(self, 'Dimension_width')
            box.prop(self, 'Dimension_length')
            box.prop(self, 'Dimension_dsize')
            box.prop(self, 'Dimension_depth')
            box.prop(self, 'Dimension_depth_from_center')
            box.prop(self, 'Dimension_rotation')
            box.prop(self, 'Dimension_resolution')

        # options per Type Note(width = 2, length = 2, dsize = 1, depth = 0.1)
        if self.Dimension_Type == 'Note':
            row = layout.row()
            row.prop(self, 'Dimension_width_or_location', expand=True)
            col = layout.column()
            col.label(text="End location:")
            row = layout.row()
            if self.Dimension_width_or_location == 'width':
                row.prop(self, 'Dimension_width')
            else:
                row.prop(self, 'Dimension_endlocation')
            box = layout.box()
            box.label("Options")
            box.prop(self, 'Dimension_length')
            box.prop(self, 'Dimension_depth')
            box.prop(self, 'Dimension_angle')
            box.prop(self, 'Dimension_rotation')
            box.prop(self, 'Dimension_note')

        col = layout.column()
        row = layout.row()
        row.prop(self, 'Dimension_align_to_camera')
        col = layout.column()
        row = layout.row()
        row.prop(self, 'Dimension_liberty', expand=True)

        if self.Dimension_liberty == '2D':
            col = layout.column()
            col.label("Coordinate system")
            row = layout.row()
            row.prop(self, 'Dimension_XYZType', expand=True)
            if self.Dimension_XYZType == 'TOP' or self.Dimension_XYZType == 'BOTTOM':
                row = layout.row()
                row.prop(self, 'Dimension_XYType', expand=True)
            if self.Dimension_XYZType == 'FRONT' or self.Dimension_XYZType == 'BACK':
                row = layout.row()
                row.prop(self, 'Dimension_XZType', expand=True)
            if self.Dimension_XYZType == 'RIGHT' or self.Dimension_XYZType == 'LEFT':
                row = layout.row()
                row.prop(self, 'Dimension_YZType', expand=True)

        col = layout.column()
        col.label("Start location:")
        row = layout.row()
        row.prop(self, 'Dimension_startlocation')

        box = layout.box()
        box.prop(self, 'Dimension_units')

        box = layout.box()
        box.label("Text Options")
        box.prop(self, 'Dimension_textsize')
        box.prop(self, 'Dimension_textdepth')
        box.prop(self, 'Dimension_textround')
        box.prop(self, 'Dimension_font')

        box = layout.box()
        box.label("Arrow Options")
        box.prop(self, 'Dimension_arrow')
        box.prop(self, 'Dimension_arrowdepth')
        box.prop(self, 'Dimension_arrowlength')

        box = layout.box()
        box.label("Material Option")
        box.prop(self, 'Dimension_matname')

    @classmethod
    def poll(cls, context):
        return not context.scene

    def execute(self, context):

        if self.Dimension_Change:
            DimensionDelete(self, context)

        # go to object mode
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')

        # turn off undo
        undo = bpy.context.user_preferences.edit.use_global_undo
        bpy.context.user_preferences.edit.use_global_undo = False

        # main function
        self.align_matrix = align_matrix(context, self.Dimension_startlocation)
        main(self, self.align_matrix)

        # restore pre operator undo state
        bpy.context.user_preferences.edit.use_global_undo = undo

        return {'FINISHED'}

    def invoke(self, context, event):
        # store creation_matrix
        if self.Dimension_Change:
            bpy.context.scene.cursor_location = self.Dimension_startlocation
        else:
            if self.Dimension_width_or_location == 'width':
                self.Dimension_startlocation = bpy.context.scene.cursor_location

            if self.Dimension_width_or_location == 'location':
                if (self.Dimension_endlocation[2] - self.Dimension_startlocation[2]) != 0:
                    self.Dimension_XYZType = 'FRONT'
                    self.Dimension_XZType = 'Z'
                if (self.Dimension_endlocation[1] - self.Dimension_startlocation[1]) != 0:
                    self.Dimension_XYZType = 'TOP'
                    self.Dimension_XYType = 'Y'
                if (self.Dimension_endlocation[0] - self.Dimension_startlocation[0]) != 0:
                    self.Dimension_XYZType = 'TOP'
                    self.Dimension_XYType = 'X'

        self.align_matrix = align_matrix(context, self.Dimension_startlocation)

        self.execute(context)

        return {'FINISHED'}


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)
