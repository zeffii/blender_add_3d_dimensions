import bpy
from bpy.props import (
    BoolProperty,
    StringProperty,
    EnumProperty,
    FloatVectorProperty,
    FloatProperty,
    IntProperty
)


# Add properties to objects
def DimensionVariables():

    Object = bpy.types.Object

    Object.Dimension = BoolProperty()
    Object.Dimension_Change = BoolProperty()
    Object.Dimension_Name = StringProperty(
        name="Name",
        description="Name")

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
    Object.Dimension_Type = EnumProperty(
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
    Object.Dimension_XYZType = EnumProperty(
        name="Coordinate system",
        description="Place in a coordinate system",
        items=XYZTypes)

    XYTypes = [
        ('X', 'X', 'X'),
        ('Y', 'Y', 'Y')]
    Object.Dimension_XYType = EnumProperty(
        name="XY",
        description="XY",
        items=XYTypes)

    XZTypes = [
        ('X', 'X', 'X'),
        ('Z', 'Z', 'Z')]
    Object.Dimension_XZType = EnumProperty(
        name="XZ",
        description="XZ",
        items=XZTypes)

    YZTypes = [
        ('Y', 'Y', 'Y'),
        ('Z', 'Z', 'Z')]
    Object.Dimension_YZType = EnumProperty(
        name="YZ",
        description="YZ",
        items=YZTypes)

    Object.Dimension_YZType = EnumProperty(
        name="Coordinate system",
        description="Place in a coordinate system",
        items=YZTypes)

    Object.Dimension_startlocation = FloatVectorProperty(
        name="Start location",
        description="",
        default=(0.0, 0.0, 0.0),
        subtype='XYZ',
        update=StartLocationUpdate)

    Object.Dimension_endlocation = FloatVectorProperty(
        name="End location",
        description="",
        default=(2.0, 2.0, 2.0),
        subtype='XYZ')

    Object.Dimension_endanglelocation = FloatVectorProperty(
        name="End angle location",
        description="End angle location",
        default=(4.0, 4.0, 4.0),
        subtype='XYZ')

    width_or_location_items = [
        ('width', 'width', 'width'),
        ('location', 'location', 'location')]
    Object.Dimension_width_or_location = EnumProperty(
        name="width or location",
        items=width_or_location_items,
        description="width or location")

    libertyItems = [
        ('2D', '2D', '2D'),
        ('3D', '3D', '3D')]
    Object.Dimension_liberty = EnumProperty(
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
    Object.Dimension_arrow = EnumProperty(
        name="Arrow",
        items=Arrows,
        description="Arrow")

    Object.Dimension_arrowdepth = FloatProperty(
        name="Depth",
        default=0.1,
        min=0, soft_min=0,
        description="Arrow depth")

    Object.Dimension_arrowlength = FloatProperty(
        name="Length",
        default=0.25,
        min=0, soft_min=0,
        description="Arrow length")

    # Dimension properties
    Object.Dimension_resolution = IntProperty(
        name="Resolution",
        default=10,
        min=1, soft_min=1,
        description="Resolution")

    Object.Dimension_width = FloatProperty(
        name="Width",
        default=2,
        unit='LENGTH',
        description="Width")

    Object.Dimension_length = FloatProperty(
        name="Length",
        default=2,
        description="Length")

    Object.Dimension_dsize = FloatProperty(
        name="Size",
        default=1,
        min=0, soft_min=0,
        description="Size")

    Object.Dimension_depth = FloatProperty(
        name="Depth",
        default=0.1,
        min=0, soft_min=0,
        description="Depth")

    Object.Dimension_depth_from_center = BoolProperty(
        name="Depth from center",
        default=False,
        description="Depth from center")

    Object.Dimension_angle = FloatProperty(
        name="Angle",
        default=45,
        description="Angle")

    Object.Dimension_rotation = FloatProperty(
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
    Object.Dimension_units = EnumProperty(
        name="Units",
        items=Units,
        description="Units")

    # Dimension text properties
    Object.Dimension_textsize = FloatProperty(
        name="Size",
        default=1,
        description="Size")

    Object.Dimension_textdepth = FloatProperty(
        name="Depth",
        default=0.2,
        description="Depth")

    Object.Dimension_textround = IntProperty(
        name="Rounding",
        default=2,
        min=0, soft_min=0,
        description="Rounding")

    Object.Dimension_font = StringProperty(
        name="Font",
        default='',
        subtype='FILE_PATH',
        description="Font")

    # Materials properties
    Object.Dimension_matname = StringProperty(
        name="Name",
        default='Dimension_Red',
        description="Material name")

    # Note text
    Object.Dimension_note = StringProperty(
        name="Note",
        default='Note',
        description="Note text")

    Object.Dimension_align_to_camera = BoolProperty(
        name="Align to camera",
        default=False,
        description="Align to camera")
