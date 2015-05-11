from .utils import addText, addUnits


def makeMaterial(name, diffuse, specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = 'LAMBERT'
    mat.diffuse_intensity = 1.0
    mat.specular_color = specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 1.0
    mat.alpha = alpha
    mat.ambient = 1
    mat.specular_hardness = 1
    mat.use_shadeless = True
    return mat


def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)


def ablength(x1=0.0, y1=0.0, z1=0.0, x2=0.0, y2=0.0, z2=0.0):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


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


def setBezierHandles(obj, mode='VECTOR'):
    scene = bpy.context.scene
    if not (obj.type in {'CURVE'}):
        return
    scene.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT', toggle=True)
    bpy.ops.curve.select_all(action='SELECT')
    bpy.ops.curve.handle_type_set(type=mode)
    bpy.ops.object.mode_set(mode='OBJECT', toggle=True)


def createCurve(vertArray, self, align_matrix):
    # options to vars
    name = self.Dimension_Type         # Type as name

    # create curve
    scene = bpy.context.scene
    newCurve = bpy.data.curves.new(name, type = 'CURVE') # curvedatablock
    newSpline = newCurve.splines.new('BEZIER') # spline

    newSpline.bezier_points.add(int(len(vertArray) * 0.333333333))
    newSpline.bezier_points.foreach_set('co', vertArray)

    # set curveOptions
    newCurve.dimensions = '2D'
    newSpline.use_cyclic_u = True
    newSpline.use_endpoint_u = True

    # create object with newCurve
    DimensionCurve = bpy.data.objects.new(name, newCurve) # object
    scene.objects.link(DimensionCurve) # place in active scene
    DimensionCurve.select = True # set as selected
    DimensionCurve.Dimension = True
    scene.objects.active = DimensionCurve  # set as active
    DimensionCurve.matrix_world = align_matrix # apply matrix
    self.Dimension_Name = DimensionCurve.name
    
    # creat DimensionText and rotation    
    w = 1
    if self.Dimension_width < 0 :
        w = -1
    l = 1
    if self.Dimension_length < 0 :
        l = -1

    x = self.Dimension_width / 2
    y = self.Dimension_length + l * self.Dimension_dsize / 2 + self.Dimension_depth / 2 + self.Dimension_textdepth
    
    gettextround = int(self.Dimension_textround)
    stext = addUnits(self.Dimension_width, self.Dimension_units)
    stext = abs(round(stext, gettextround))
    if gettextround == 0:
        stext = abs(int(stext))
    
    align = 'CENTER'
    offset_y = 0
    
    if self.Dimension_Type == 'Linear-2':
        y = self.Dimension_depth / 2 + self.Dimension_textdepth

    if self.Dimension_Type == 'Radius':
        x = self.Dimension_width + w * self.Dimension_dsize / 2 + w * abs(self.Dimension_length) / 2
        y = self.Dimension_depth / 2 + self.Dimension_textdepth

    if self.Dimension_Type == 'Diameter':
        x = 0
        y = self.Dimension_depth / 2 + self.Dimension_textdepth 

    g = hypot(x, y)
    c = self.Dimension_startlocation
    u = asin(y / g)
    if self.Dimension_width < 0 :
        u = radians(180) - u
    xx = cos(u) * g
    yy = sin(u) * g
    
    stext = str(stext)
    if not self.Dimension_units == 'None' :
        stext += self.Dimension_units

    if self.Dimension_Type == 'Angular1' or self.Dimension_Type == 'Angular2' or self.Dimension_Type == 'Angular3':
        xx = cos(radians(self.Dimension_angle / 2)) * (self.Dimension_width + w * self.Dimension_depth / 2 + w * self.Dimension_textdepth)
        yy = sin(radians(self.Dimension_angle / 2)) * (self.Dimension_width + w * self.Dimension_depth / 2 + w * self.Dimension_textdepth)
        system_rotation = bpy.context.scene.unit_settings.system_rotation
        if system_rotation == 'DEGREES':
            stext = abs(round(self.Dimension_angle, gettextround))
            if gettextround == 0:
                stext = abs(int(stext))
            stext = str(stext) + '°'
        else:
            stext = abs(round(self.Dimension_angle * pi / 180, gettextround))
            if gettextround == 0:
                stext = abs(int(stext))
            stext = str(stext)
        align = 'LEFT'
        if self.Dimension_XYZType == 'BOTTOM' or self.Dimension_XYZType == 'BACK' or self.Dimension_XYZType == 'LEFT':
            align = 'RIGHT'
        if self.Dimension_width < 0 :
            offset_y = 0
            align = 'RIGHT'
            if self.Dimension_XYZType == 'BOTTOM' or self.Dimension_XYZType == 'BACK' or self.Dimension_XYZType == 'LEFT':
                align = 'LEFT'
    
    if self.Dimension_Type == 'Note':
        if cos(radians(self.Dimension_angle)) > 0:
            xx = cos(radians(self.Dimension_angle)) * (self.Dimension_width) + l * w * self.Dimension_depth / 2 + l * w * self.Dimension_textdepth
            yy = sin(radians(self.Dimension_angle)) * (self.Dimension_width) + w * self.Dimension_depth / 2 + w * self.Dimension_textdepth
            stext = self.Dimension_note
            align = 'LEFT'
            if self.Dimension_XYZType == 'BOTTOM' or self.Dimension_XYZType == 'BACK' or self.Dimension_XYZType == 'LEFT':
                align = 'RIGHT'
            if self.Dimension_width < 0 :
                align = 'RIGHT'
                xx = cos(radians(self.Dimension_angle)) * (self.Dimension_width) + l * w * self.Dimension_depth / 2 + l * w * self.Dimension_textdepth
                yy = sin(radians(self.Dimension_angle)) * (self.Dimension_width) - w * self.Dimension_depth / 2 - w * self.Dimension_textdepth
                if self.Dimension_XYZType == 'BOTTOM' or self.Dimension_XYZType == 'BACK' or self.Dimension_XYZType == 'LEFT':
                   align = 'LEFT'
        else:
            xx = cos(radians(self.Dimension_angle)) * (self.Dimension_width) - l * w * self.Dimension_depth / 2 - l * w * self.Dimension_textdepth
            yy = sin(radians(self.Dimension_angle)) * (self.Dimension_width) + w * self.Dimension_depth / 2 + w * self.Dimension_textdepth
            stext = self.Dimension_note
            align = 'RIGHT'
            if self.Dimension_XYZType == 'BOTTOM' or self.Dimension_XYZType == 'BACK' or self.Dimension_XYZType == 'LEFT':
                align = 'LEFT'
            if self.Dimension_width < 0 :
                align = 'LEFT'
                xx = cos(radians(self.Dimension_angle)) * (self.Dimension_width) - l * w * self.Dimension_depth / 2 - l * w * self.Dimension_textdepth
                yy = sin(radians(self.Dimension_angle)) * (self.Dimension_width) - w * self.Dimension_depth / 2 - w * self.Dimension_textdepth
                if self.Dimension_XYZType == 'BOTTOM' or self.Dimension_XYZType == 'BACK' or self.Dimension_XYZType == 'LEFT':
                    align = 'RIGHT'
    
    if self.Dimension_liberty == '2D':
        tv = Vector((xx, yy, 0))
        
        DimensionText = addText(stext, tv, self.Dimension_textsize, align, offset_y, self.Dimension_font)

        if self.Dimension_XYZType == 'TOP' or self.Dimension_XYZType == 'BOTTOM':
            DimensionCurve.rotation_euler[0] = radians(0)
            DimensionCurve.rotation_euler[1] = radians(0)
            if self.Dimension_XYType == 'X':
                DimensionCurve.rotation_euler[2] = radians(self.Dimension_rotation)
            if self.Dimension_XYType == 'Y':
                DimensionCurve.rotation_euler[2] = radians(90+self.Dimension_rotation)
        
        if self.Dimension_XYZType == 'FRONT' or self.Dimension_XYZType == 'BACK':
            DimensionCurve.rotation_euler[0] = radians(90)
            if self.Dimension_XZType == 'X':
                DimensionCurve.rotation_euler[1] = -radians(self.Dimension_rotation)
            if self.Dimension_XZType == 'Z':
                DimensionCurve.rotation_euler[1] = -radians(90+self.Dimension_rotation)
            DimensionCurve.rotation_euler[2] = radians(0)
        
        if self.Dimension_XYZType == 'RIGHT' or self.Dimension_XYZType == 'LEFT':
            DimensionCurve.rotation_euler[0] = radians(90)
            if self.Dimension_YZType == 'Y':
                DimensionCurve.rotation_euler[1] = -radians(self.Dimension_rotation)
            if self.Dimension_YZType == 'Z':
                DimensionCurve.rotation_euler[1] = -radians(90+self.Dimension_rotation)
            DimensionCurve.rotation_euler[2] = radians(90)
        
        if self.Dimension_XYZType == 'TOP' or self.Dimension_XYZType == 'FRONT' or self.Dimension_XYZType == 'RIGHT':
            DimensionText.rotation_euler[1] = radians(0)
        if self.Dimension_XYZType == 'BOTTOM' or self.Dimension_XYZType == 'BACK' or self.Dimension_XYZType == 'LEFT':
            DimensionText.rotation_euler[1] = radians(180)
        
        if self.Dimension_width_or_location == 'location':
            if self.Dimension_Type == 'Angular1' or self.Dimension_Type == 'Angular2' or self.Dimension_Type == 'Angular3':
                vx = self.Dimension_endlocation.x - self.Dimension_startlocation.x
                vy = self.Dimension_endlocation.y - self.Dimension_startlocation.y
                vz = self.Dimension_endlocation.z - self.Dimension_startlocation.z
                if self.Dimension_XYZType == 'TOP' or self.Dimension_XYZType == 'BOTTOM':
                    g = hypot(vx, vy)
                    if g !=  0 :
                       u2 = acos(vx / g)
                       u1 = asin(vy / g)
                       if u1 < 0 :
                           u2 = u1
                    else:
                       u2 = 0
                    DimensionCurve.rotation_euler[2] = u2
    
                if self.Dimension_XYZType == 'FRONT' or self.Dimension_XYZType == 'BACK':
                    g = hypot(vx, vz)
                    if g !=  0 :
                       u2 = acos(vx / g)
                       u1 = asin(vz / g)
                       if u1 < 0 :
                           u2 = u1
                    else:
                       u2 = 0
                    DimensionCurve.rotation_euler[1] = -u2

                if self.Dimension_XYZType == 'RIGHT' or self.Dimension_XYZType == 'LEFT':
                    g = hypot(vy, vz)
                    if g !=  0 :
                       u2 = acos(vy / g)
                       u1 = asin(vz / g)
                       if u1 < 0 :
                           u2 = u1
                    else:
                       u2 = 0
                    DimensionCurve.rotation_euler[1] = -u2

    if self.Dimension_liberty == '3D':
        tv = Vector((xx, yy, 0))
        DimensionText = addText(stext, tv, self.Dimension_textsize, align, offset_y, self.Dimension_font)
        v = self.Dimension_endlocation - self.Dimension_startlocation
        if v.length !=  0 :
           u1 = -asin(v[2] / v.length)
        else:
           u1 = 0
        g = hypot(v[0], v[1])
        if g !=  0 :
           u2 = asin(v[1] / g)
           if self.Dimension_endlocation.x < self.Dimension_startlocation.x :
              u2 = radians(180)-asin(v[1] / g)
        else:
           u2 = 0
        
        DimensionCurve.rotation_euler[0] = radians(self.Dimension_rotation)
        DimensionCurve.rotation_euler[1] = u1
        DimensionCurve.rotation_euler[2] = u2

    # Align to view
    if self.Dimension_align_to_camera :
        obj_camera = bpy.context.scene.camera
        DimensionCurve.rotation_euler[0] = obj_camera.rotation_euler[0]
        DimensionCurve.rotation_euler[1] = obj_camera.rotation_euler[1]
        DimensionCurve.rotation_euler[2] = obj_camera.rotation_euler[2]

    # set materials
    if self.Dimension_matname in bpy.data.materials :
        setMaterial(DimensionCurve, bpy.data.materials[self.Dimension_matname])
        setMaterial(DimensionText, bpy.data.materials[self.Dimension_matname])
    else:
        red = makeMaterial(self.Dimension_matname, (1, 0, 0), (1, 0, 0), 1)
        setMaterial(DimensionCurve, red)
        setMaterial(DimensionText, red)
    
    setBezierHandles(DimensionCurve, 'VECTOR')
    setBezierHandles(DimensionText, 'VECTOR') 

    DimensionText.parent = DimensionCurve

    group_name = 'Dimensions'

    if group_name in bpy.data.groups:
        group = bpy.data.groups[group_name]
    else:
        group = bpy.data.groups.new(group_name)

    if not DimensionCurve.name in group.objects:
        group.objects.link(DimensionCurve)
    
    if not DimensionText.name in group.objects:
        group.objects.link(DimensionText)
    
    DimensionCurve.select = True
    DimensionText.select = True

    DimensionCurve.Dimension_Name = self.Dimension_Name
    DimensionCurve.Dimension_Type = self.Dimension_Type
    DimensionCurve.Dimension_XYZType = self.Dimension_XYZType
    DimensionCurve.Dimension_XYType = self.Dimension_XYType
    DimensionCurve.Dimension_XZType = self.Dimension_XZType
    DimensionCurve.Dimension_YZType = self.Dimension_YZType
    DimensionCurve.Dimension_startlocation = c
    DimensionCurve.Dimension_endlocation = self.Dimension_endlocation
    DimensionCurve.Dimension_endanglelocation = self.Dimension_endanglelocation
    DimensionCurve.Dimension_width_or_location = self.Dimension_width_or_location
    DimensionCurve.Dimension_liberty = self.Dimension_liberty
    DimensionCurve.Dimension_Change = False

    #### Dimension properties
    DimensionCurve.Dimension_resolution = self.Dimension_resolution
    DimensionCurve.Dimension_width = self.Dimension_width
    DimensionCurve.Dimension_length = self.Dimension_length
    DimensionCurve.Dimension_dsize = self.Dimension_dsize
    DimensionCurve.Dimension_depth = self.Dimension_depth
    DimensionCurve.Dimension_depth_from_center = self.Dimension_depth_from_center
    DimensionCurve.Dimension_angle = self.Dimension_angle
    DimensionCurve.Dimension_rotation = self.Dimension_rotation
    
    #### Dimension text properties
    DimensionCurve.Dimension_textsize = self.Dimension_textsize
    DimensionCurve.Dimension_textdepth = self.Dimension_textdepth
    DimensionCurve.Dimension_textround = self.Dimension_textround
    DimensionCurve.Dimension_font = self.Dimension_font
    
    #### Dimension Arrow properties
    DimensionCurve.Dimension_arrow = self.Dimension_arrow
    DimensionCurve.Dimension_arrowdepth = self.Dimension_arrowdepth
    DimensionCurve.Dimension_arrowlength = self.Dimension_arrowlength

    #### Materials properties
    DimensionCurve.Dimension_matname = self.Dimension_matname
    
    #### Note properties
    DimensionCurve.Dimension_note = self.Dimension_note
    DimensionCurve.Dimension_align_to_camera = self.Dimension_align_to_camera

    return

##------------------------------------------------------------
# Main Function
def main(self, align_matrix):
    # deselect all objects
    bpy.ops.object.select_all(action = 'DESELECT')

    # options
    Type = self.Dimension_Type
    
    if self.Dimension_width_or_location == 'location':
        if self.Dimension_liberty == '2D':
            if self.Dimension_XYZType == 'TOP':
                if self.Dimension_XYType == 'X':
                    self.Dimension_width = self.Dimension_endlocation[0] - self.Dimension_startlocation[0]
                if self.Dimension_XYType == 'Y':
                    self.Dimension_width = self.Dimension_endlocation[1] - self.Dimension_startlocation[1]
            if self.Dimension_XYZType == 'FRONT':
                if self.Dimension_XZType == 'X':
                    self.Dimension_width = self.Dimension_endlocation[0] - self.Dimension_startlocation[0]
                if self.Dimension_XZType == 'Z':
                    self.Dimension_width = self.Dimension_endlocation[2] - self.Dimension_startlocation[2]
            if self.Dimension_XYZType == 'RIGHT':
                if self.Dimension_YZType == 'Y':
                    self.Dimension_width = self.Dimension_endlocation[1] - self.Dimension_startlocation[1]
                if self.Dimension_YZType == 'Z':
                    self.Dimension_width = self.Dimension_endlocation[2] - self.Dimension_startlocation[2]
            if self.Dimension_XYZType == 'BOTTOM':
                if self.Dimension_XYType == 'X':
                    self.Dimension_width = self.Dimension_endlocation[0] - self.Dimension_startlocation[0]
                if self.Dimension_XYType == 'Y':
                    self.Dimension_width = self.Dimension_endlocation[1] - self.Dimension_startlocation[1]
            if self.Dimension_XYZType == 'BACK':
                if self.Dimension_XZType == 'X':
                    self.Dimension_width = self.Dimension_endlocation[0] - self.Dimension_startlocation[0]
                if self.Dimension_XZType == 'Z':
                    self.Dimension_width = self.Dimension_endlocation[2] - self.Dimension_startlocation[2]
            if self.Dimension_XYZType == 'LEFT':
                if self.Dimension_YZType == 'Y':
                    self.Dimension_width = self.Dimension_endlocation[1] - self.Dimension_startlocation[1]
                if self.Dimension_YZType == 'Z':
                    self.Dimension_width = self.Dimension_endlocation[2] - self.Dimension_startlocation[2]
        if self.Dimension_liberty == '3D':
            v = self.Dimension_endlocation - self.Dimension_startlocation
            self.Dimension_width = v.length
 
        if Type == 'Angular1' or Type == 'Angular2' or Type == 'Angular3':
            c = ablength(self.Dimension_startlocation.x, self.Dimension_startlocation.y, self.Dimension_startlocation.z, self.Dimension_endlocation.x, self.Dimension_endlocation.y, self.Dimension_endlocation.z)
            b = ablength(self.Dimension_startlocation.x, self.Dimension_startlocation.y, self.Dimension_startlocation.z, self.Dimension_endanglelocation.x, self.Dimension_endanglelocation.y, self.Dimension_endanglelocation.z)
            a = ablength(self.Dimension_endanglelocation.x, self.Dimension_endanglelocation.y, self.Dimension_endanglelocation.z, self.Dimension_endlocation.x, self.Dimension_endlocation.y, self.Dimension_endlocation.z)
            self.Dimension_width = max(a, b, c)
            vanglex = self.Dimension_endanglelocation.x - self.Dimension_startlocation.x
            vangley = self.Dimension_endanglelocation.y - self.Dimension_startlocation.y
            vanglez = self.Dimension_endanglelocation.z - self.Dimension_startlocation.z
            vendx = self.Dimension_endlocation.x - self.Dimension_startlocation.x
            vendy = self.Dimension_endlocation.y - self.Dimension_startlocation.y
            vendz = self.Dimension_endlocation.z - self.Dimension_startlocation.z
            if self.Dimension_XYZType == 'TOP' or self.Dimension_XYZType == 'BOTTOM':
                self.Dimension_XYType = 'X'
                g = hypot(vanglex, vangley)
                if g !=  0 :
                   u2 = acos(vanglex / g)
                   u1 = asin(vangley / g)
                   if u1 < 0 :
                       u2 = -u2
                else:
                   u2 = 0
                g = hypot(vendx, vendy)
                if g !=  0 :
                   uu2 = acos(vendx / g)
                   uu1 = asin(vendy / g)
                   if uu1 < 0 :
                       uu2 = -uu2
                else:
                   uu2 = 0
                self.Dimension_angle = degrees(u2 - uu2)
            if self.Dimension_XYZType == 'FRONT' or self.Dimension_XYZType == 'BACK':
                self.Dimension_XZType = 'Z'
                g = hypot(vanglex, vanglez)
                if g !=  0 :
                   u2 = acos(vanglex / g)
                   u1 = asin(vanglez / g)
                   if u1 < 0 :
                       u2 = -u2
                else:
                   u2 = 0
                g = hypot(vendx, vendz)
                if g !=  0 :
                   uu2 = acos(vendx / g)
                   uu1 = asin(vendz / g)
                   if uu1 < 0 :
                       uu2 = -uu2
                else:
                   uu2 = 0
                self.Dimension_angle = degrees(u2 - uu2)
            if self.Dimension_XYZType == 'RIGHT' or self.Dimension_XYZType == 'LEFT':
                self.Dimension_YZType = 'Z'
                g = hypot(vangley, vanglez)
                if g !=  0 :
                   u2 = acos(vangley / g)
                   u1 = asin(vanglez / g)
                   if u1 < 0 :
                       u2 = -u2
                else:
                   u2 = 0
                g = hypot(vendy, vendz)
                if g !=  0 :
                   uu2 = acos(vendy / g)
                   uu1 = asin(vendz / g)
                   if uu1 < 0 :
                       uu2 = -uu2
                else:
                   uu2 = 0
                self.Dimension_angle = degrees(u2 - uu2)
            if self.Dimension_liberty == '3D':
                c = ablength(self.Dimension_startlocation.x, self.Dimension_startlocation.y, self.Dimension_startlocation.z, self.Dimension_endlocation.x, self.Dimension_endlocation.y, self.Dimension_endlocation.z)
                b = ablength(self.Dimension_startlocation.x, self.Dimension_startlocation.y, self.Dimension_startlocation.z, self.Dimension_endanglelocation.x, self.Dimension_endanglelocation.y, self.Dimension_endanglelocation.z)
                a = ablength(self.Dimension_endanglelocation.x, self.Dimension_endanglelocation.y, self.Dimension_endanglelocation.z, self.Dimension_endlocation.x, self.Dimension_endlocation.y, self.Dimension_endlocation.z)
                if b != 0 and c != 0 :
                    self.Dimension_angle = degrees(acos((b**2 + c**2 - a**2)/(2*b*c)))
                else:
                    self.Dimension_angle = 0
   
    #
    if self.Dimension_width == 0:
        return {'FINISHED'}
    
    # get verts
    if Type == 'Linear-1':
        verts = Linear1(self.Dimension_width, 
                          self.Dimension_length, 
                          self.Dimension_dsize, 
                          self.Dimension_depth, 
                          self.Dimension_depth_from_center, 
                          self.Dimension_arrow, 
                          self.Dimension_arrowdepth, 
                          self.Dimension_arrowlength)

    if Type == 'Linear-2':
        verts = Linear2(self.Dimension_width, 
                          self.Dimension_dsize, 
                          self.Dimension_depth, 
                          self.Dimension_depth_from_center, 
                          self.Dimension_arrow, 
                          self.Dimension_arrowdepth, 
                          self.Dimension_arrowlength)

    if Type == 'Linear-3':
        verts = Linear3(self.Dimension_width, 
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
        verts = Diameter(self.Dimension_width, 
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
        verts = Angular1(self.Dimension_width, 
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
        verts = Angular2(self.Dimension_width, 
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
    
    vertArray = []
    # turn verts into array
    for v in verts:
        vertArray  += v
    
    # create object
    createCurve(vertArray, self, align_matrix)


#### Delete dimension group
def DimensionDelete(self, context):
    
    if bpy.ops.object.mode_set.poll(): 
        bpy.ops.object.mode_set(mode = 'OBJECT') 

    bpy.ops.object.select_grouped(extend=True, type='CHILDREN_RECURSIVE')
    bpy.ops.object.delete()

        
#location update
def StartLocationUpdate(self, context):
    bpy.context.scene.cursor_location = self.Dimension_startlocation
