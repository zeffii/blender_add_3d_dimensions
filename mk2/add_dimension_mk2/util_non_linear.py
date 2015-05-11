from math import *


def Radius(width = 2, length = 2, dsize = 1, depth = 0.1, center = False, arrow = 'Arrow1', arrowdepth = 0.25, arrowlength = 0.25):
    
    newpoints = []
    
    w = 1
    if width < 0:
        w = -1
    length = abs(length)
    
    if center:
       center1 = w * depth / 2
       center2 = w * depth / 2
    else:
       center1 = 0
       center2 = w * depth
    
    if arrow == 'Arrow1':
        newpoints.append([0, depth / 2, 0]) #1
        newpoints.append([width, depth / 2, 0]) #2
        newpoints.append([width + w * arrowlength, depth / 2 + arrowdepth, 0]) #3
        newpoints.append([width + w * arrowlength, depth / 2, 0]) #4
        newpoints.append([width + w * arrowlength + w * length, depth / 2, 0]) #5
        newpoints.append([width + w * arrowlength + w * length, -depth / 2, 0]) #6
        newpoints.append([width + w * arrowlength, -depth / 2, 0]) #7
        newpoints.append([width + w * arrowlength, -depth / 2-arrowdepth, 0]) #8
        newpoints.append([width, -depth / 2, 0]) #9
        newpoints.append([0, -depth / 2, 0]) #10
    
    if arrow == 'Arrow2':
        newpoints.append([0, depth / 2, 0]) #1
        newpoints.append([width, depth / 2, 0]) #2
        newpoints.append([width + w * arrowlength, depth / 2 + arrowdepth, 0]) #3
        newpoints.append([width + w * arrowlength * 3 / 4, depth / 2, 0]) #4
        newpoints.append([width + w * arrowlength + w * length, depth / 2, 0]) #5
        newpoints.append([width + w * arrowlength + w * length, -depth / 2, 0]) #6
        newpoints.append([width + w * arrowlength * 3 / 4, -depth / 2, 0]) #7
        newpoints.append([width + w * arrowlength, -depth / 2-arrowdepth, 0]) #8
        newpoints.append([width, -depth / 2, 0]) #9
        newpoints.append([0, -depth / 2, 0]) #10
    
    if arrow == 'Serifs1':
        b = sqrt(depth * depth / 2)
        x = sin(radians(45)) * arrowlength * w
        y = cos(radians(45)) * arrowlength
        newpoints.append([0, depth / 2, 0]) #1
        newpoints.append([width-center2, depth / 2, 0]) #16
        newpoints.append([width-center2, dsize / 2, 0]) #17
        newpoints.append([width + center1, dsize / 2, 0]) #18
        newpoints.append([width + center1, depth / 2 + b, 0]) #19
        newpoints.append([width + center1 + x, depth / 2 + b + y, 0]) #20
        newpoints.append([width + center1 + w * b + x, depth / 2 + y, 0]) #21
        newpoints.append([width + center1 + w * b, depth / 2, 0]) #22
        newpoints.append([width + center1 + w * length, depth / 2, 0]) #23
        newpoints.append([width + center1 + w * length, -depth / 2, 0]) #24
        newpoints.append([width + center1, -depth / 2, 0]) #25
        newpoints.append([width + center1, -dsize / 2, 0]) #26
        newpoints.append([width-center2, -dsize / 2, 0]) #29
        newpoints.append([width-center2, -depth / 2-b, 0]) #30
        newpoints.append([width-center2-x, -depth / 2-b-y, 0]) #31
        newpoints.append([width-center2-w * b-x, -depth / 2-y, 0]) #32
        newpoints.append([width-center2-w * b, -depth / 2, 0]) #33
        newpoints.append([0, -depth / 2, 0]) #10
    
    if arrow == 'Serifs2':
        b = sqrt(depth * depth / 2)
        x = sin(radians(45)) * arrowlength * w
        y = cos(radians(45)) * arrowlength
        newpoints.append([0, depth / 2, 0]) #1
        newpoints.append([width + center1-w * b, depth / 2, 0]) #19
        newpoints.append([width + center1 + x, depth / 2 + b + y, 0]) #20
        newpoints.append([width + center1 + w * b + x, depth / 2 + y, 0]) #21
        newpoints.append([width + center1 + w * b, depth / 2, 0]) #22
        newpoints.append([width + center1 + w * length, depth / 2, 0]) #23
        newpoints.append([width + center1 + w * length, -depth / 2, 0]) #24
        newpoints.append([width-center2 + w * b, -depth / 2, 0]) #30
        newpoints.append([width-center2-x, -depth / 2-b-y, 0]) #31
        newpoints.append([width-center2-w * b-x, -depth / 2-y, 0]) #32
        newpoints.append([width-center2-w * b, -depth / 2, 0]) #33
        newpoints.append([0, -depth / 2, 0]) #10
    
    elif arrow == 'Without':
        newpoints.append([0, depth / 2, 0]) #1
        newpoints.append([width, depth / 2, 0]) #2
        newpoints.append([width, -depth / 2, 0]) #9
        newpoints.append([0, -depth / 2, 0]) #10

    return newpoints


def Diameter(width = 2, length = 2, dsize = 1, depth = 0.1, center = False, arrow = 'Arrow1', arrowdepth = 0.25, arrowlength = 0.25):
    
    newpoints = []
    
    width = width / 2
    w = 1
    if width < 0:
        w = -1
    length = abs(length)
    
    if center:
       center1 = w * depth / 2
       center2 = w * depth / 2
    else:
       center1 = 0
       center2 = w * depth
    
    if arrow == 'Arrow1':
        newpoints.append([0, depth / 2, 0]) #1
        newpoints.append([width, depth / 2, 0]) #2
        newpoints.append([width + w * arrowlength, depth / 2 + arrowdepth, 0]) #3
        newpoints.append([width + w * arrowlength, depth / 2, 0]) #4
        newpoints.append([width + w * arrowlength + w * length, depth / 2, 0]) #5
        newpoints.append([width + w * arrowlength + w * length, -depth / 2, 0]) #6
        newpoints.append([width + w * arrowlength, -depth / 2, 0]) #7
        newpoints.append([width + w * arrowlength, -depth / 2-arrowdepth, 0]) #8
        newpoints.append([width, -depth / 2, 0]) #9
        newpoints.append([0, -depth / 2, 0]) #10
        newpoints.append([-width, -depth / 2, 0]) #11
        newpoints.append([-width-w * arrowlength, -depth / 2-arrowdepth, 0]) #12
        newpoints.append([-width-w * arrowlength, -depth / 2, 0]) #13
        newpoints.append([-width-w * arrowlength-w * length, -depth / 2, 0]) #14
        newpoints.append([-width-w * arrowlength-w * length, depth / 2, 0]) #15
        newpoints.append([-width-w * arrowlength, depth / 2, 0]) #16
        newpoints.append([-width-w * arrowlength, depth / 2 + arrowdepth, 0]) #17
        newpoints.append([-width, depth / 2, 0]) #18
    
    if arrow == 'Arrow2':
        newpoints.append([0, depth / 2, 0]) #1
        newpoints.append([width, depth / 2, 0]) #2
        newpoints.append([width + w * arrowlength, depth / 2 + arrowdepth, 0]) #3
        newpoints.append([width + w * arrowlength * 3 / 4, depth / 2, 0]) #4
        newpoints.append([width + w * arrowlength + w * length, depth / 2, 0]) #5
        newpoints.append([width + w * arrowlength + w * length, -depth / 2, 0]) #6
        newpoints.append([width + w * arrowlength * 3 / 4, -depth / 2, 0]) #7
        newpoints.append([width + w * arrowlength, -depth / 2-arrowdepth, 0]) #8
        newpoints.append([width, -depth / 2, 0]) #9
        newpoints.append([0, -depth / 2, 0]) #10
        newpoints.append([-width, -depth / 2, 0]) #11
        newpoints.append([-width-w * arrowlength, -depth / 2-arrowdepth, 0]) #12
        newpoints.append([-width-w * arrowlength * 3 / 4, -depth / 2, 0]) #13
        newpoints.append([-width-w * arrowlength-w * length, -depth / 2, 0]) #14
        newpoints.append([-width-w * arrowlength-w * length, depth / 2, 0]) #15
        newpoints.append([-width-w * arrowlength * 3 / 4, depth / 2, 0]) #16
        newpoints.append([-width-w * arrowlength, depth / 2 + arrowdepth, 0]) #17
        newpoints.append([-width, depth / 2, 0]) #18
    
    if arrow == 'Serifs1':
        b = sqrt(depth * depth / 2)
        x = sin(radians(45)) * arrowlength * w
        y = cos(radians(45)) * arrowlength
        newpoints.append([0, depth / 2, 0]) #1
        newpoints.append([width-center2, depth / 2, 0]) #16
        newpoints.append([width-center2, dsize / 2, 0]) #17
        newpoints.append([width + center1, dsize / 2, 0]) #18
        newpoints.append([width + center1, depth / 2 + b, 0]) #19
        newpoints.append([width + center1 + x, depth / 2 + b + y, 0]) #20
        newpoints.append([width + center1 + w * b + x, depth / 2 + y, 0]) #21
        newpoints.append([width + center1 + w * b, depth / 2, 0]) #22
        newpoints.append([width + center1 + w * length, depth / 2, 0]) #23
        newpoints.append([width + center1 + w * length, -depth / 2, 0]) #24
        newpoints.append([width + center1, -depth / 2, 0]) #25
        newpoints.append([width + center1, -dsize / 2, 0]) #26
        newpoints.append([width-center2, -dsize / 2, 0]) #29
        newpoints.append([width-center2, -depth / 2-b, 0]) #30
        newpoints.append([width-center2-x, -depth / 2-b-y, 0]) #31
        newpoints.append([width-center2-w * b-x, -depth / 2-y, 0]) #32
        newpoints.append([width-center2-w * b, -depth / 2, 0]) #33
        newpoints.append([0, -depth / 2, 0]) #10
        newpoints.append([-width + center2, -depth / 2, 0]) #25
        newpoints.append([-width + center2, -dsize / 2, 0]) #26
        newpoints.append([-width-center1, -dsize / 2, 0]) #29
        newpoints.append([-width-center1, -depth / 2-b, 0]) #30
        newpoints.append([-width-center1-x, -depth / 2-b-y, 0]) #31
        newpoints.append([-width-center1-w * b-x, -depth / 2-y, 0]) #32
        newpoints.append([-width-center1-w * b, -depth / 2, 0]) #33
        newpoints.append([-width + center2-w * length, -depth / 2, 0]) #24
        newpoints.append([-width + center2-w * length, depth / 2, 0]) #23
        newpoints.append([-width-center1, depth / 2, 0]) #16
        newpoints.append([-width-center1, dsize / 2, 0]) #17
        newpoints.append([-width + center2, dsize / 2, 0]) #18
        newpoints.append([-width + center2, depth / 2 + b, 0]) #19
        newpoints.append([-width + center2 + x, depth / 2 + b + y, 0]) #20
        newpoints.append([-width + center2 + w * b + x, depth / 2 + y, 0]) #21
        newpoints.append([-width + center2 + w * b, depth / 2, 0]) #22
    
    if arrow == 'Serifs2':
        b = sqrt(depth * depth / 2)
        x = sin(radians(45)) * arrowlength * w
        y = cos(radians(45)) * arrowlength
        newpoints.append([0, depth / 2, 0]) #1
        newpoints.append([width + center1-w * b, depth / 2, 0]) #19
        newpoints.append([width + center1 + x, depth / 2 + b + y, 0]) #20
        newpoints.append([width + center1 + w * b + x, depth / 2 + y, 0]) #21
        newpoints.append([width + center1 + w * b, depth / 2, 0]) #22
        newpoints.append([width + center1 + w * length, depth / 2, 0]) #23
        newpoints.append([width + center1 + w * length, -depth / 2, 0]) #24
        newpoints.append([width-center2 + w * b, -depth / 2, 0]) #30
        newpoints.append([width-center2-x, -depth / 2-b-y, 0]) #31
        newpoints.append([width-center2-w * b-x, -depth / 2-y, 0]) #32
        newpoints.append([width-center2-w * b, -depth / 2, 0]) #33
        newpoints.append([0, -depth / 2, 0]) #10
        newpoints.append([-width-center1 + w * b, -depth / 2, 0]) #30
        newpoints.append([-width-center1-x, -depth / 2-b-y, 0]) #31
        newpoints.append([-width-center1-w * b-x, -depth / 2-y, 0]) #32
        newpoints.append([-width-center1-w * b, -depth / 2, 0]) #33
        newpoints.append([-width + center2-w * length, -depth / 2, 0]) #24
        newpoints.append([-width + center2-w * length, depth / 2, 0]) #23
        newpoints.append([-width + center2-w * b, depth / 2, 0]) #19
        newpoints.append([-width + center2 + x, depth / 2 + b + y, 0]) #20
        newpoints.append([-width + center2 + w * b + x, depth / 2 + y, 0]) #21
        newpoints.append([-width + center2 + w * b, depth / 2, 0]) #22
    
    elif arrow == 'Without':
        newpoints.append([0, depth / 2, 0]) #1
        newpoints.append([width, depth / 2, 0]) #2
        newpoints.append([width, -depth / 2, 0]) #9
        newpoints.append([0, -depth / 2, 0]) #10
        newpoints.append([-width, -depth / 2, 0]) #11
        newpoints.append([-width, depth / 2, 0]) #18
    
    return newpoints


def Angular1(width = 2, length = 2, depth = 0.1, angle = 45, resolution = 10, center = False, arrow = 'Arrow1', arrowdepth = 0.25, arrowlength = 0.25):
    
    newpoints = []
    
    if arrow == 'Serifs1' or arrow == 'Serifs2':
        arrow = 'Without'
        
    w = 1
    if width < 0:
        w = -1
    
    if resolution == 0:
       resolution = 1
       
    if arrow == 'Without':
       arrowdepth = 0.0
       arrowlength = 0.0
    
    length = abs(length)
    angle = radians(angle)

    if center:
       center1 = w * depth / 2
       center2 = w * depth / 2
    else:
       center1 = 0
       center2 = w * depth
       
    g = hypot(width + w * length, center2)
    u_depth = asin((center2) / g)
    
    g = hypot(width, center2)
    u_depth_min = asin((center2 + center2/4) / g)
    
    g = hypot(width, arrowlength + w * center2)
    u_arrow = asin((arrowlength + w * center2) / g)
       
    if width < 0:
        u_depth = -u_depth
        u_depth_min = -u_depth_min
    
    a = 1
    if angle < 0 :
       a = -1
       u_depth = -u_depth
       u_depth_min = -u_depth_min
       u_arrow = -u_arrow

    x = (a * center1) / tan(angle / 2)
    newpoints.append([-x, -a * center1, 0]) #1
    newpoints.append([width + w * length, -a * center1, 0]) #2
    newpoints.append([width + w * length, a * center2, 0]) #3
    
    if arrow == 'Without':
        newpoints.append([width + w * depth / 2, a * center2, 0]) #4
    else:
        newpoints.append([width + w * depth / 100, a * center2, 0]) #4
    
    g = width + w * arrowdepth + w * depth / 2
    x = cos(u_arrow + u_depth) * g
    y = sin(u_arrow + u_depth) * g
    newpoints.append([x, y, 0]) #5
    
    if arrow == 'Arrow1':
        g = width + w * depth / 2
        x = cos(u_arrow + u_depth) * g
        y = sin(u_arrow + u_depth) * g
        newpoints.append([x, y, 0]) #6
    if arrow == 'Arrow2':
        g = width + w * depth / 2
        x = cos(u_arrow * 3 / 4 + u_depth) * g
        y = sin(u_arrow * 3 / 4 + u_depth) * g
        newpoints.append([x, y, 0]) #6
        
    i = 1
    while i < resolution :
        u = i * (angle - u_arrow * 2 - u_depth * 2) / resolution
        g = width + w * depth / 2
        x = cos(u + u_arrow + u_depth) * g
        y = sin(u + u_arrow + u_depth) * g
        newpoints.append([x, y, 0]) #n
        i  += 1
    
    if arrow == 'Arrow1':
        g = width + w * depth / 2
        x = cos(angle - u_arrow - u_depth) * g
        y = sin(angle - u_arrow - u_depth) * g
        newpoints.append([x, y, 0]) #7
    if arrow == 'Arrow2':
        g = width + w * depth / 2
        x = cos(angle - u_arrow * 3 / 4 - u_depth) * g
        y = sin(angle - u_arrow * 3 / 4 - u_depth) * g
        newpoints.append([x, y, 0]) #7
    
    u = angle - u_arrow - u_depth
    g = width + w * arrowdepth + w * depth / 2
    x = cos(u) * g
    y = sin(u) * g
    newpoints.append([x, y, 0]) #8
    
    if arrow == 'Without':
        g = width + w * depth / 2
        x = cos(angle-u_depth_min) * g
        y = sin(angle-u_depth_min) * g
        newpoints.append([x, y, 0]) #9
    else:
        g = width + w * depth / 100
        x = cos(angle-u_depth_min) * g
        y = sin(angle-u_depth_min) * g
        newpoints.append([x, y, 0]) #9
    
    if arrow == 'Without':
        g = width-w * depth / 2
        x = cos(angle-u_depth_min) * g
        y = sin(angle-u_depth_min) * g
        newpoints.append([x, y, 0]) #10
    else:
        g = width-w * depth / 100
        x = cos(angle-u_depth_min) * g
        y = sin(angle-u_depth_min) * g
        newpoints.append([x, y, 0]) #10
    
    g = width-w * arrowdepth-w * depth / 2
    x = cos(u) * g
    y = sin(u) * g
    newpoints.append([x, y, 0]) #11
    
    if arrow == 'Arrow1':
        u = angle - u_arrow - u_depth
        g = width-w * depth / 2
        x = cos(u) * g
        y = sin(u) * g
        newpoints.append([x, y, 0]) #12
    if arrow == 'Arrow2':
        u = angle - u_arrow * 3 / 4 - u_depth
        g = width-w * depth / 2
        x = cos(u) * g
        y = sin(u) * g
        newpoints.append([x, y, 0]) #12
    
    i = resolution - 1
    while i >=  1 :
        u = i * (angle - u_arrow * 2 - u_depth * 2) / resolution
        g = width-w * depth / 2
        x = cos(u + u_arrow + u_depth) * g
        y = sin(u + u_arrow + u_depth) * g
        newpoints.append([x, y, 0]) #n
        i -=  1
    
    if arrow == 'Arrow1':
        g = width-w * depth / 2
        x = cos(u_arrow + u_depth) * g
        y = sin(u_arrow + u_depth) * g
        newpoints.append([x, y, 0]) #13
    if arrow == 'Arrow2':
        g = width-w * depth / 2
        x = cos(u_arrow * 3 / 4 + u_depth) * g
        y = sin(u_arrow * 3 / 4 + u_depth) * g
        newpoints.append([x, y, 0]) #13
    
    g = width-w * arrowdepth-w * depth / 2
    x = cos(u_arrow + u_depth) * g
    y = sin(u_arrow + u_depth) * g
    newpoints.append([x, y, 0]) #14
    
    if arrow == 'Without':
        newpoints.append([width-w * depth / 2, a * center2, 0]) #15
    else:
        newpoints.append([width-w * depth / 100, a * center2, 0]) #15
    
    x = (a * center2) / tan(angle / 2)
    newpoints.append([x, a * center2, 0]) #16
    
    g = width + w * length
    x = cos(angle-u_depth) * g
    y = sin(angle-u_depth) * g
    newpoints.append([x, y, 0]) #17
    
    if center:
        g = width + w * length
        x = cos(angle + u_depth) * g
        y = sin(angle + u_depth) * g
        newpoints.append([x, y, 0]) #18    
    else:
        g = width + w * length
        x = cos(angle) * g
        y = sin(angle) * g
        newpoints.append([x, y, 0]) #18
           
    return newpoints


def Angular2(width = 2, depth = 0.1, angle = 45, resolution = 10, arrow = 'Arrow1', arrowdepth = 0.25, arrowlength = 0.25):
    
    newpoints = []
    
    if arrow == 'Serifs1' or arrow == 'Serifs2':
        arrow = 'Without'
    
    w = 1
    if width < 0:
        w = -1
    
    if resolution == 0:
       resolution = 1
    
    if arrow == 'Without':
       arrowdepth = 0.0
       arrowlength = 0.0
    
    angle = radians(angle)
    
    newpoints.append([width, 0, 0]) #1
    
    g = hypot(width + w * depth / 2, arrowlength)
    u_arrow = asin((arrowlength) / g)
    if angle < 0 :
       u_arrow = -u_arrow
    
    g = width + w * arrowdepth + w * depth / 2
    x = cos(u_arrow) * g
    y = sin(u_arrow) * g
    newpoints.append([x, y, 0]) #2
    
    if arrow == 'Arrow1':
        g = width + w * depth / 2
        x = cos(u_arrow) * g
        y = sin(u_arrow) * g
        newpoints.append([x, y, 0]) #3
    
    if arrow == 'Arrow2':
        g = width + w * depth / 2
        x = cos(u_arrow * 3 / 4) * g
        y = sin(u_arrow * 3 / 4) * g
        newpoints.append([x, y, 0]) #3
        
    i = 1
    while i < resolution :
        u = i * (angle - u_arrow * 2) / resolution
        g = width + w * depth / 2
        x = cos(u + u_arrow) * g
        y = sin(u + u_arrow) * g
        newpoints.append([x, y, 0]) #n
        i  += 1
    
    if arrow == 'Arrow1':
        u = angle - u_arrow
        g = width + w * depth / 2
        x = cos(u) * g
        y = sin(u) * g
        newpoints.append([x, y, 0]) #4
    if arrow == 'Arrow2':
        u = angle - u_arrow * 3 / 4
        g = width + w * depth / 2
        x = cos(u) * g
        y = sin(u) * g
        newpoints.append([x, y, 0]) #4
    
    u = angle - u_arrow
    g = width + w * arrowdepth + w * depth / 2
    x = cos(u) * g
    y = sin(u) * g
    newpoints.append([x, y, 0]) #5
    
    g = width
    x = cos(angle) * g
    y = sin(angle) * g
    newpoints.append([x, y, 0]) #6
    
    g = width-w * arrowdepth-w * depth / 2
    x = cos(u) * g
    y = sin(u) * g
    newpoints.append([x, y, 0]) #7
    
    if arrow == 'Arrow1':
        u = angle - u_arrow
        g = width-w * depth / 2
        x = cos(u) * g
        y = sin(u) * g
        newpoints.append([x, y, 0]) #8
    if arrow == 'Arrow2':
        u = angle - u_arrow * 3 / 4
        g = width-w * depth / 2
        x = cos(u) * g
        y = sin(u) * g
        newpoints.append([x, y, 0]) #8
    
    i = resolution - 1
    while i > 0 :
        u = i * (angle - u_arrow * 2) / resolution
        g = width-w * depth / 2
        x = cos(u + u_arrow) * g
        y = sin(u + u_arrow) * g
        newpoints.append([x, y, 0]) #n
        i -=  1
        
    if arrow == 'Arrow1':
        g = width-w * depth / 2
        x = cos(u_arrow) * g
        y = sin(u_arrow) * g
        newpoints.append([x, y, 0]) #9
    if arrow == 'Arrow2':
        g = width-w * depth / 2
        x = cos(u_arrow * 3 / 4) * g
        y = sin(u_arrow * 3 / 4) * g
        newpoints.append([x, y, 0]) #9
    
    g = width-w * arrowdepth-w * depth / 2
    x = cos(u_arrow) * g
    y = sin(u_arrow) * g
    newpoints.append([x, y, 0]) #10
        
    return newpoints

def Angular3(width = 2, length = 2, dsize = 1, depth = 0.1, angle = 45, resolution = 10, center = False, arrow = 'Arrow1', arrowdepth = 0.25, arrowlength = 0.25):
    
    newpoints = []
    
    if arrow == 'Serifs1' or arrow == 'Serifs2':
        arrow = 'Without'
    
    w = 1
    if width < 0:
        w = -1
    
    if resolution == 0:
       resolution = 1
       
    if arrow == 'Without':
       arrowdepth = 0.0
       arrowlength = 0.0
    
    resolution_2 = floor(resolution / 2)
    
    length = abs(length)
    angle = radians(angle)
    
    if center:
       center1 = w * depth / 2
       center2 = w * depth / 2
    else:
       center1 = 0
       center2 = w * depth

    g = hypot(width + w * length, center2)
    u_depth = asin((center2) / g)
    
    g = hypot(width + depth / 2, center2)
    u_depth_13 = asin((center2 + center2/4) / g)
    
    g = hypot(width-depth / 2, center2)
    u_depth_14 = asin((center2 + center2/4) / g)
    
    g = hypot(width, center2)
    u_depth_min = asin((center2) / g)
    
    g = hypot(width, arrowlength + w * center2)
    u_arrow = asin((arrowlength + w * center2) / g)
    
    g = hypot(width, arrowlength + w * center2 + dsize)
    u_dsize = asin((arrowlength + w * center2 + dsize) / g)
       
    if width < 0:
        u_depth = -u_depth
        u_depth_min = -u_depth_min
        u_depth_13 = -u_depth_13
        u_depth_14 = -u_depth_14
    
    a = 1
    if angle < 0 :
       a = -1
       u_depth = -u_depth
       u_depth_min = -u_depth_min
       u_arrow = -u_arrow
       u_depth_13 = -u_depth_13
       u_depth_14 = -u_depth_14

    x = (a * center1) / tan(angle / 2)
    newpoints.append([-x, -a * center1, 0]) #1
    
    if arrow == 'Without':
        newpoints.append([width-w * depth / 2, -a * center1, 0]) #2
    else:
        newpoints.append([width-w * depth / 100, -a * center1, 0]) #2
    
    g = width-w * arrowdepth-w * depth / 2
    x = cos(-u_arrow-u_depth) * g
    y = sin(-u_arrow-u_depth) * g
    newpoints.append([x, y, 0]) #3
    
    if arrow == 'Arrow1':
        g = width-w * depth / 2
        x = cos(-u_arrow-u_depth) * g
        y = sin(-u_arrow-u_depth) * g
        newpoints.append([x, y, 0]) #4
    if arrow == 'Arrow2':
        g = width-w * depth / 2
        x = cos(-u_arrow * 3 / 4-u_depth) * g
        y = sin(-u_arrow * 3 / 4-u_depth) * g
        newpoints.append([x, y, 0]) #4
    
    i = 1
    while i < resolution_2 :
        u = i * (-u_dsize) / resolution_2
        g = width-w * depth / 2
        x = cos(u-u_arrow) * g
        y = sin(u-u_arrow) * g
        newpoints.append([x, y, 0]) #n
        i  += 1
    
    g = width-w * depth / 2
    x = cos(-u_arrow-u_depth-u_dsize) * g
    y = sin(-u_arrow-u_depth-u_dsize) * g
    newpoints.append([x, y, 0]) #5
    
    g = width + w * depth / 2
    x = cos(-u_arrow-u_depth-u_dsize) * g
    y = sin(-u_arrow-u_depth-u_dsize) * g
    newpoints.append([x, y, 0]) #6
    
    i = resolution_2
    while i >=  1 :
        u = i * (-u_dsize) / resolution_2
        g = width + w * depth / 2
        x = cos(u-u_arrow) * g
        y = sin(u-u_arrow) * g
        newpoints.append([x, y, 0]) #n
        i -=  1
    
    if arrow == 'Arrow1':
       g = width + w * depth / 2
       x = cos(-u_arrow-u_depth) * g
       y = sin(-u_arrow-u_depth) * g
       newpoints.append([x, y, 0]) #7
    if arrow == 'Arrow2':
       g = width + w * depth / 2
       x = cos(-u_arrow * 3 / 4-u_depth) * g
       y = sin(-u_arrow * 3 / 4-u_depth) * g
       newpoints.append([x, y, 0]) #7
    
    g = width + w * arrowdepth + w * depth / 2
    x = cos(-u_arrow-u_depth) * g
    y = sin(-u_arrow-u_depth) * g
    newpoints.append([x, y, 0]) #8
    
    if arrow == 'Without':
        newpoints.append([width + w * depth / 2, -a * center1, 0]) #9
    else:
        newpoints.append([width + w * depth / 100, -a * center1, 0]) #9
    
    newpoints.append([width + w * length, -a * center1, 0]) #10
    
    newpoints.append([width + w * length, a * center2, 0]) #11
    
    g = width + w * depth / 2
    x = cos(u_depth_min) * g
    y = sin(u_depth_min) * g
    newpoints.append([x, y, 0]) #12
    
    i = 1
    while i < resolution :
        u = i * (angle - u_depth * 2) / resolution
        g = width + w * depth / 2
        x = cos(u + u_depth) * g
        y = sin(u + u_depth) * g
        newpoints.append([x, y, 0]) #n
        i  += 1
    
    if width > 0 :
        g = width + w * depth / 2
        x = cos(angle - u_depth_13) * g
        y = sin(angle - u_depth_13) * g
        newpoints.append([x, y, 0]) #13
    
        g = width-w * depth / 2
        x = cos(angle - u_depth_14) * g
        y = sin(angle - u_depth_14) * g
        newpoints.append([x, y, 0]) #14
    else:
        g = width + w * depth / 2
        x = cos(angle - u_depth_14) * g
        y = sin(angle - u_depth_14) * g
        newpoints.append([x, y, 0]) #13
    
        g = width-w * depth / 2
        x = cos(angle - u_depth_13) * g
        y = sin(angle - u_depth_13) * g
        newpoints.append([x, y, 0]) #14
    
    i = resolution - 1
    while i >=  1 :
        u = i * (angle - u_depth * 2) / resolution
        g = width-w * depth / 2
        x = cos(u + u_depth) * g
        y = sin(u + u_depth) * g
        newpoints.append([x, y, 0]) #n
        i -=  1
    
    g = width-w * depth / 2
    x = cos(u_depth_min) * g
    y = sin(u_depth_min) * g
    newpoints.append([x, y, 0]) #15
    
    x = (a * center2) / tan(angle / 2)
    newpoints.append([x, a * center2, 0]) #16
    
    g = width + w * length
    x = cos(angle-u_depth) * g
    y = sin(angle-u_depth) * g
    newpoints.append([x, y, 0]) #17
    
    if center:
        g = width + w * length
        x = cos(angle + u_depth) * g
        y = sin(angle + u_depth) * g
        newpoints.append([x, y, 0]) #18
        
        if arrow == 'Without':
            g = width + w * depth / 2
            x = cos(angle + u_depth) * g
            y = sin(angle + u_depth) * g
            newpoints.append([x, y, 0]) #19
        else:
            g = width + w * depth / 100
            x = cos(angle + u_depth) * g
            y = sin(angle + u_depth) * g
            newpoints.append([x, y, 0]) #19
    else:
        g = width + w * length
        x = cos(angle) * g
        y = sin(angle) * g
        newpoints.append([x, y, 0]) #18
    
        if arrow == 'Without':
            g = width + w * depth / 2
            x = cos(angle) * g
            y = sin(angle) * g
            newpoints.append([x, y, 0]) #19
        else:
            g = width + w * depth / 100
            x = cos(angle) * g
            y = sin(angle) * g
            newpoints.append([x, y, 0]) #19
    
    g = width + w * arrowdepth + w * depth / 2
    x = cos(angle + u_arrow + u_depth) * g
    y = sin(angle + u_arrow + u_depth) * g
    newpoints.append([x, y, 0]) #20
    
    if arrow == 'Arrow1':
        g = width + w * depth / 2
        x = cos(angle + u_arrow + u_depth) * g
        y = sin(angle + u_arrow + u_depth) * g
        newpoints.append([x, y, 0]) #21
    if arrow == 'Arrow2':
        g = width + w * depth / 2
        x = cos(angle + u_arrow * 3 / 4 + u_depth) * g
        y = sin(angle + u_arrow * 3 / 4 + u_depth) * g
        newpoints.append([x, y, 0]) #21
    
    i = 1
    while i < resolution_2 :
        u = i * (u_dsize) / resolution_2
        g = width + w * depth / 2
        x = cos(u + angle + u_arrow) * g
        y = sin(u + angle + u_arrow) * g
        newpoints.append([x, y, 0]) #n
        i  += 1
    
    g = width + w * depth / 2
    x = cos(angle + u_arrow + u_depth + u_dsize) * g
    y = sin(angle + u_arrow + u_depth + u_dsize) * g
    newpoints.append([x, y, 0]) #22
    
    g = width-w * depth / 2
    x = cos(angle + u_arrow + u_depth + u_dsize) * g
    y = sin(angle + u_arrow + u_depth + u_dsize) * g
    newpoints.append([x, y, 0]) #23
    
    i = resolution_2
    while i >=  1 :
        u = i * (u_dsize) / resolution_2
        g = width-w * depth / 2
        x = cos(u + angle + u_arrow) * g
        y = sin(u + angle + u_arrow) * g
        newpoints.append([x, y, 0]) #n
        i -=  1
    
    if arrow == 'Arrow1':
        g = width-w * depth / 2
        x = cos(angle + u_arrow + u_depth) * g
        y = sin(angle + u_arrow + u_depth) * g
        newpoints.append([x, y, 0]) #24
    if arrow == 'Arrow2':
        g = width-w * depth / 2
        x = cos(angle + u_arrow * 3 / 4 + u_depth) * g
        y = sin(angle + u_arrow * 3 / 4 + u_depth) * g
        newpoints.append([x, y, 0]) #24
    
    g = width-w * arrowdepth-w * depth / 2
    x = cos(angle + u_arrow + u_depth) * g
    y = sin(angle + u_arrow + u_depth) * g
    newpoints.append([x, y, 0]) #25
    
    if center:
        if arrow == 'Without':
            g = width-w * depth / 2
            x = cos(angle + u_depth) * g
            y = sin(angle + u_depth) * g
            newpoints.append([x, y, 0]) #26
        else:
            g = width-w * depth / 100
            x = cos(angle + u_depth) * g
            y = sin(angle + u_depth) * g
            newpoints.append([x, y, 0]) #26
    else:
        if arrow == 'Without':
            g = width-w * depth / 2
            x = cos(angle) * g
            y = sin(angle) * g
            newpoints.append([x, y, 0]) #26
        else:
            g = width-w * depth / 100
            x = cos(angle) * g
            y = sin(angle) * g
            newpoints.append([x, y, 0]) #26
 
    return newpoints