import mathutils
from mathutils import Matrix, Vector

import bpy
from .utils_linear import Linear1, Linear2, Linear3
from .utils_non_linear import Radius, Diameter, Angular1, Angular2, Angular3
from .utils_note import Note


# Add a TextCurve
def addText(string='', loc=((0, 0, 0)), textsize=1, align='CENTER', offset_y=0, font=''):

    tcu = bpy.data.curves.new(string + 'Data', 'FONT')
    text = bpy.data.objects.new(string + 'Text', tcu)
    text.location = loc

    if font == '':
        fnt = bpy.data.fonts[0]
    else:
        fnt = bpy.data.fonts.load(font)

    tcu.body = string
    tcu.align = align
    tcu.size = textsize
    tcu.offset_y = offset_y
    tcu.font = fnt
    bpy.context.scene.objects.link(text)

    return text


def addUnits(stext, units):
    scale = bpy.context.scene.unit_settings.scale_length
    unit_system = bpy.context.scene.unit_settings.system
    separate_units = bpy.context.scene.unit_settings.use_separate
    if unit_system == 'METRIC':
        if units == 'None': scale_steps = 1
        if units == '\u00b5m': scale_steps = 1000000
        if units == 'mm': scale_steps = 1000
        if units == 'cm': scale_steps = 100
        if units == 'm': scale_steps = 1
        if units == 'km': scale_steps = 1/1000
        if units == 'thou': scale_steps = 36000 * 1.0936133
        if units == '"': scale_steps = 36 * 1.0936133
        if units == '\'': scale_steps = 3 * 1.0936133
        if units == 'yd': scale_steps = 1 * 1.0936133
        if units == 'mi': scale_steps = 1/1760 * 1.0936133
        dval = stext * scale_steps * scale
    elif unit_system == 'IMPERIAL':
        if units == 'None': scale_steps = 3 * 1.0936133
        if units == '\u00b5m': scale_steps = 1000000
        if units == 'mm': scale_steps = 1000
        if units == 'cm': scale_steps = 100
        if units == 'm': scale_steps = 1
        if units == 'km': scale_steps = 1/1000
        if units == 'thou': scale_steps = 36000 * 1.0936133
        if units == '"': scale_steps = 36 * 1.0936133
        if units == '\'': scale_steps = 3 * 1.0936133
        if units == 'yd': scale_steps = 1 * 1.0936133
        if units == 'mi': scale_steps = 1/1760 * 1.0936133
        dval = stext * scale_steps * scale
    else:
        dval = stext
    return dval


def getVerts(self, Type):

    if Type == 'Linear-1':
        verts = Linear1(
            self.Dimension_width, 
            self.Dimension_length, 
            self.Dimension_dsize, 
            self.Dimension_depth, 
            self.Dimension_depth_from_center, 
            self.Dimension_arrow, 
            self.Dimension_arrowdepth, 
            self.Dimension_arrowlength)

    if Type == 'Linear-2':
        verts = Linear2(
            self.Dimension_width, 
            self.Dimension_dsize, 
            self.Dimension_depth, 
            self.Dimension_depth_from_center, 
            self.Dimension_arrow, 
            self.Dimension_arrowdepth, 
            self.Dimension_arrowlength)

    if Type == 'Linear-3':
        verts = Linear3(
            self.Dimension_width, 
            self.Dimension_length, 
            self.Dimension_dsize, 
            self.Dimension_depth, 
            self.Dimension_depth_from_center, 
            self.Dimension_arrow, 
            self.Dimension_arrowdepth, 
            self.Dimension_arrowlength)

    if Type == 'Radius':
        verts = Radius(self.Dimension_width, 
            self.Dimension_length, 
            self.Dimension_dsize, 
            self.Dimension_depth, 
            self.Dimension_depth_from_center, 
            self.Dimension_arrow, 
            self.Dimension_arrowdepth, 
            self.Dimension_arrowlength)

    if Type == 'Diameter':
        verts = Diameter(
            self.Dimension_width, 
            self.Dimension_length, 
            self.Dimension_dsize, 
            self.Dimension_depth, 
            self.Dimension_depth_from_center, 
            self.Dimension_arrow, 
            self.Dimension_arrowdepth, 
            self.Dimension_arrowlength)                           
    
    if Type == 'Angular1':
        if self.Dimension_angle == 0:
            return {'FINISHED'}
        
        verts = Angular1(
            self.Dimension_width, 
            self.Dimension_length, 
            self.Dimension_depth, 
            self.Dimension_angle, 
            self.Dimension_resolution, 
            self.Dimension_depth_from_center, 
            self.Dimension_arrow, 
            self.Dimension_arrowdepth, 
            self.Dimension_arrowlength)

    if Type == 'Angular2':
        if self.Dimension_angle == 0:
            return {'FINISHED'}

        verts = Angular2(
            self.Dimension_width, 
            self.Dimension_depth, 
            self.Dimension_angle, 
            self.Dimension_resolution, 
            self.Dimension_arrow, 
            self.Dimension_arrowdepth, 
            self.Dimension_arrowlength)

    if Type == 'Angular3':
        if self.Dimension_angle == 0:
            return {'FINISHED'}

        verts = Angular3(
            self.Dimension_width, 
            self.Dimension_length, 
            self.Dimension_dsize, 
            self.Dimension_depth, 
            self.Dimension_angle, 
            self.Dimension_resolution, 
            self.Dimension_depth_from_center, 
            self.Dimension_arrow, 
            self.Dimension_arrowdepth, 
            self.Dimension_arrowlength)
    
    if Type == 'Note':
        verts = Note(
            self.Dimension_width, 
            self.Dimension_length, 
            self.Dimension_depth, 
            self.Dimension_angle, 
            self.Dimension_arrow, 
            self.Dimension_arrowdepth, 
            self.Dimension_arrowlength)

    return verts


def align_matrix(context, location):
    '''
    calculates the matrix for the new object
    depending on user pref
    '''

    loc = Matrix.Translation(location)
    obj_align = context.user_preferences.edit.object_align
    if ((context.space_data.type == 'VIEW_3D') and (obj_align == 'VIEW')):
        rot = context.space_data.region_3d.view_matrix.to_3x3().inverted().to_4x4()
    else:
        rot = Matrix()
    align_matrix = loc * rot
    return align_matrix