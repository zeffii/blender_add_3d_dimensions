from math import *

def Linear1(width=2, length=2, dsize=1, depth=0.1, center=False, arrow='Arrow1', arrowdepth=0.1, arrowlength=0.25):

    newpoints = []

    w = 1
    if width < 0:
        w = -1
    l = 1
    if length < 0:
        l = -1

    if center:
        center1 = w * depth / 2
        center2 = w * depth / 2
    else:
        center1 = 0
        center2 = w * depth

    if arrow == 'Arrow1':
        newpoints.append([-center1, 0, 0]) #1
        newpoints.append([-center1, length, 0]) #2
        newpoints.append([-center1, length + l * dsize, 0]) #3
        newpoints.append([center2, length + l * dsize, 0]) #4
        newpoints.append([center2, length + l * dsize / 2 + l * depth / 100, 0]) #5
        newpoints.append([center2 + w * arrowlength, length + l * dsize / 2 + l * arrowdepth + l * depth / 2, 0]) #6
        newpoints.append([center2 + w * arrowlength, length + l * dsize / 2 + l * depth / 2, 0]) #7
        newpoints.append([width-center2-w * arrowlength, length + l * dsize / 2 + l * depth / 2, 0]) #8
        newpoints.append([width-center2-w * arrowlength, length + l * dsize / 2 + l * arrowdepth + l * depth / 2, 0]) #9
        newpoints.append([width-center2, length + l * dsize / 2 + l * depth / 100, 0]) #10
        newpoints.append([width-center2, length + l * dsize, 0]) #11
        newpoints.append([width + center1, length + l * dsize, 0]) #12
        newpoints.append([width + center1, length, 0]) #13
        newpoints.append([width + center1, 0, 0]) #14
        newpoints.append([width-center2, 0, 0]) #15
        newpoints.append([width-center2, length, 0]) #16
        newpoints.append([width-center2, length + l * dsize / 2-l * depth / 100, 0]) #17
        newpoints.append([width-center2-w * arrowlength, length + l * dsize / 2-l * arrowdepth-l * depth / 2, 0]) #18
        newpoints.append([width-center2-w * arrowlength, length + l * dsize / 2-l * depth / 2, 0]) #19
        newpoints.append([center2 + w * arrowlength, length + l * dsize / 2-l * depth / 2, 0]) #20
        newpoints.append([center2 + w * arrowlength, length + l * dsize / 2-l * arrowdepth-l * depth / 2, 0]) #21
        newpoints.append([center2, length + l * dsize / 2-l * depth / 100, 0]) #22
        newpoints.append([center2, length, 0]) #23
        newpoints.append([center2, 0, 0]) #24

    elif arrow == 'Arrow2':
        newpoints.append([-center1, 0, 0]) #1
        newpoints.append([-center1, length, 0]) #2
        newpoints.append([-center1, length + l * dsize, 0]) #3
        newpoints.append([center2, length + l * dsize, 0]) #4
        newpoints.append([center2, length + l * dsize / 2 + l * depth / 100, 0]) #5
        newpoints.append([center2 + w * arrowlength, length + l * dsize / 2 + l * arrowdepth + l * depth / 2, 0]) #6
        newpoints.append([center2 + w * arrowlength * 3 / 4, length + l * dsize / 2 + l * depth / 2, 0]) #7
        newpoints.append([width-center2-w * arrowlength * 3 / 4, length + l * dsize / 2 + l * depth / 2, 0]) #8
        newpoints.append([width-center2-w * arrowlength, length + l * dsize / 2 + l * arrowdepth + l * depth / 2, 0]) #9
        newpoints.append([width-center2, length + l * dsize / 2 + l * depth / 100, 0]) #10
        newpoints.append([width-center2, length + l * dsize, 0]) #11
        newpoints.append([width + center1, length + l * dsize, 0]) #12
        newpoints.append([width + center1, length, 0]) #13
        newpoints.append([width + center1, 0, 0]) #14
        newpoints.append([width-center2, 0, 0]) #15
        newpoints.append([width-center2, length, 0]) #16
        newpoints.append([width-center2, length + l * dsize / 2-l * depth / 100, 0]) #17
        newpoints.append([width-center2-w * arrowlength, length + l * dsize / 2-l * arrowdepth-l * depth / 2, 0]) #18
        newpoints.append([width-center2-w * arrowlength * 3 / 4, length + l * dsize / 2-l * depth / 2, 0]) #19
        newpoints.append([center2 + w * arrowlength * 3 / 4, length + l * dsize / 2-l * depth / 2, 0]) #20
        newpoints.append([center2 + w * arrowlength, length + l * dsize / 2-l * arrowdepth-l * depth / 2, 0]) #21
        newpoints.append([center2, length + l * dsize / 2-l * depth / 100, 0]) #22
        newpoints.append([center2, length, 0]) #23
        newpoints.append([center2, 0, 0]) #24
    
    elif arrow == 'Serifs1':
        b = sqrt(depth * depth / 2)
        x = sin(radians(45)) * arrowlength * w
        y = cos(radians(45)) * arrowlength * l
        newpoints.append([-center1, 0, 0]) #1
        newpoints.append([-center1, length, 0]) #2
        newpoints.append([-center1, length + l * dsize / 2-l * depth / 2-l * b, 0]) #3
        newpoints.append([-center1-x, length + l * dsize / 2-l * depth / 2-l * b-y, 0]) #4
        newpoints.append([-center1-w * b-x, length + l * dsize / 2-l * depth / 2-y, 0]) #5
        newpoints.append([-center1, length + l * dsize / 2 + l * depth / 2, 0]) #9
        newpoints.append([-center1, length + l * dsize, 0]) #10
        newpoints.append([center2, length + l * dsize, 0]) #11
        newpoints.append([center2, length + l * dsize / 2 + l * depth / 2 + l * b, 0]) #12
        newpoints.append([center2 + x, length + l * dsize / 2 + l * depth / 2 + l * b + y, 0]) #13
        newpoints.append([center2 + w * b + x, length + l * dsize / 2 + l * depth / 2 + y, 0]) #14
        newpoints.append([center2 + w * b, length + l * dsize / 2 + l * depth / 2, 0]) #15
        newpoints.append([width-center2, length + l * dsize / 2 + l * depth / 2, 0]) #16
        newpoints.append([width-center2, length + l * dsize, 0]) #17
        newpoints.append([width + center1, length + l * dsize, 0]) #18
        newpoints.append([width + center1, length + l * dsize / 2 + l * depth / 2 + l * b, 0]) #19
        newpoints.append([width + center1 + x, length + l * dsize / 2 + l * depth / 2 + l * b + y, 0]) #20
        newpoints.append([width + center1 + w * b + x, length + l * dsize / 2 + l * depth / 2 + y, 0]) #21
        newpoints.append([width + center1, length + l * dsize / 2-l * depth / 2, 0]) #25
        newpoints.append([width + center1, length, 0]) #26
        newpoints.append([width + center1, 0, 0]) #27
        newpoints.append([width-center2, 0, 0]) #28
        newpoints.append([width-center2, length, 0]) #29
        newpoints.append([width-center2, length + l * dsize / 2-l * depth / 2-l * b, 0]) #30
        newpoints.append([width-center2-x, length + l * dsize / 2-l * depth / 2-l * b-y, 0]) #31
        newpoints.append([width-center2-w * b-x, length + l * dsize / 2-l * depth / 2-y, 0]) #32
        newpoints.append([width-center2-w * b, length + l * dsize / 2-l * depth / 2, 0]) #33
        newpoints.append([center2, length + l * dsize / 2-l * depth / 2, 0]) #34
        newpoints.append([center2, length, 0]) #35
        newpoints.append([center2, 0, 0]) #36
    
    elif arrow == 'Serifs2':
        b = sqrt(depth * depth / 2)
        x = sin(radians(45)) * arrowlength * w
        y = cos(radians(45)) * arrowlength * l
        newpoints.append([-center1, 0, 0]) #1
        newpoints.append([-center1, length, 0]) #2
        newpoints.append([-center1, length + l * dsize / 2-l * depth / 2-l * b, 0]) #3
        newpoints.append([-center1-x, length + l * dsize / 2-l * depth / 2-l * b-y, 0]) #4
        newpoints.append([-center1-w * b-x, length + l * dsize / 2-l * depth / 2-y, 0]) #5
        newpoints.append([-center1-w * b, length + l * dsize / 2-l * depth / 2, 0]) #6
        newpoints.append([-center1-w * dsize / 2, length + l * dsize / 2-l * depth / 2, 0]) #7
        newpoints.append([-center1-w * dsize / 2, length + l * dsize / 2 + l * depth / 2, 0]) #8
        newpoints.append([-center1, length + l * dsize / 2 + l * depth / 2, 0]) #9
        newpoints.append([-center1, length + l * dsize, 0]) #10
        newpoints.append([center2, length + l * dsize, 0]) #11
        newpoints.append([center2, length + l * dsize / 2 + l * depth / 2 + l * b, 0]) #12
        newpoints.append([center2 + x, length + l * dsize / 2 + l * depth / 2 + l * b + y, 0]) #13
        newpoints.append([center2 + w * b + x, length + l * dsize / 2 + l * depth / 2 + y, 0]) #14
        newpoints.append([center2 + w * b, length + l * dsize / 2 + l * depth / 2, 0]) #15
        newpoints.append([width-center2, length + l * dsize / 2 + l * depth / 2, 0]) #16
        newpoints.append([width-center2, length + l * dsize, 0]) #17
        newpoints.append([width + center1, length + l * dsize, 0]) #18
        newpoints.append([width + center1, length + l * dsize / 2 + l * depth / 2 + l * b, 0]) #19
        newpoints.append([width + center1 + x, length + l * dsize / 2 + l * depth / 2 + l * b + y, 0]) #20
        newpoints.append([width + center1 + w * b + x, length + l * dsize / 2 + l * depth / 2 + y, 0]) #21
        newpoints.append([width + center1 + w * b, length + l * dsize / 2 + l * depth / 2, 0]) #22
        newpoints.append([width + center1 + w * dsize / 2, length + l * dsize / 2 + l * depth / 2, 0]) #23
        newpoints.append([width + center1 + w * dsize / 2, length + l * dsize / 2-l * depth / 2, 0]) #24
        newpoints.append([width + center1, length + l * dsize / 2-l * depth / 2, 0]) #25
        newpoints.append([width + center1, length, 0]) #26
        newpoints.append([width + center1, 0, 0]) #27
        newpoints.append([width-center2, 0, 0]) #28
        newpoints.append([width-center2, length, 0]) #29
        newpoints.append([width-center2, length + l * dsize / 2-l * depth / 2-l * b, 0]) #30
        newpoints.append([width-center2-x, length + l * dsize / 2-l * depth / 2-l * b-y, 0]) #31
        newpoints.append([width-center2-w * b-x, length + l * dsize / 2-l * depth / 2-y, 0]) #32
        newpoints.append([width-center2-w * b, length + l * dsize / 2-l * depth / 2, 0]) #33
        newpoints.append([center2, length + l * dsize / 2-l * depth / 2, 0]) #34
        newpoints.append([center2, length, 0]) #35
        newpoints.append([center2, 0, 0]) #36
    
    elif arrow == 'Without':
        newpoints.append([-center1, 0, 0]) #1
        newpoints.append([-center1, length, 0]) #2
        newpoints.append([-center1, length + l * dsize, 0]) #3
        newpoints.append([center2, length + l * dsize, 0]) #4
        newpoints.append([center2, length + l * dsize / 2 + l * depth / 2, 0]) #7
        newpoints.append([width-center2, length + l * dsize / 2 + l * depth / 2, 0]) #8
        newpoints.append([width-center2, length + l * dsize, 0]) #11
        newpoints.append([width + center1, length + l * dsize, 0]) #12
        newpoints.append([width + center1, length, 0]) #13
        newpoints.append([width + center1, 0, 0]) #14
        newpoints.append([width-center2, 0, 0]) #15
        newpoints.append([width-center2, length, 0]) #16
        newpoints.append([width-center2, length + l * dsize / 2-l * depth / 2, 0]) #19
        newpoints.append([center2, length + l * dsize / 2-l * depth / 2, 0]) #20
        newpoints.append([center2, length, 0]) #23
        newpoints.append([center2, 0, 0]) #24

    return newpoints


def Linear2(width = 2, dsize = 1, depth = 0.1, center = False, arrow = 'Arrow1', arrowdepth = 0.25, arrowlength = 0.25):
    
    newpoints = []
    
    w = 1
    if width < 0:
        w = -1
    
    if center:
       center1 = w * depth / 2
       center2 = w * depth / 2
    else:
       center1 = 0
       center2 = w * depth
    
    if arrow == 'Arrow1':
        newpoints.append([0, 0, 0]) #1
        newpoints.append([w * arrowlength, arrowdepth + depth / 2, 0]) #2
        newpoints.append([w * arrowlength, depth / 2, 0]) #3
        newpoints.append([width-w * arrowlength, depth / 2, 0]) #4
        newpoints.append([width-w * arrowlength, arrowdepth + depth / 2, 0]) #5
        newpoints.append([width, 0, 0]) #6
        newpoints.append([width-w * arrowlength, -arrowdepth-depth / 2, 0]) #7
        newpoints.append([width-w * arrowlength, -depth / 2, 0]) #8
        newpoints.append([w * arrowlength, -depth / 2, 0]) #9
        newpoints.append([w * arrowlength, -arrowdepth-depth / 2, 0]) #10
    
    elif arrow == 'Arrow2':
        newpoints.append([0, 0, 0]) #1
        newpoints.append([w * arrowlength, arrowdepth + depth / 2, 0]) #2
        newpoints.append([w * arrowlength * 3 / 4, depth / 2, 0]) #3
        newpoints.append([width-w * arrowlength * 3 / 4, depth / 2, 0]) #4
        newpoints.append([width-w * arrowlength, arrowdepth + depth / 2, 0]) #5
        newpoints.append([width, 0, 0]) #6
        newpoints.append([width-w * arrowlength, -arrowdepth-depth / 2, 0]) #7
        newpoints.append([width-w * arrowlength * 3 / 4, -depth / 2, 0]) #8
        newpoints.append([w * arrowlength * 3 / 4, -depth / 2, 0]) #9
        newpoints.append([w * arrowlength, -arrowdepth-depth / 2, 0]) #10
    
    elif arrow == 'Serifs1':
        b = sqrt(depth * depth / 2)
        x = sin(radians(45)) * arrowlength * w
        y = cos(radians(45)) * arrowlength
        newpoints.append([-center1, -dsize / 2, 0]) #2
        newpoints.append([-center1, -depth / 2-b, 0]) #3
        newpoints.append([-center1-x, -depth / 2-b-y, 0]) #4
        newpoints.append([-center1-w * b-x, -depth / 2-y, 0]) #5
        newpoints.append([-center1-w * b, -depth / 2, 0]) #6
        newpoints.append([-center1-w * dsize / 2, -depth / 2, 0]) #7
        newpoints.append([-center1-w * dsize / 2, depth / 2, 0]) #8
        newpoints.append([-center1, depth / 2, 0]) #9
        newpoints.append([-center1, dsize / 2, 0]) #10
        newpoints.append([center2, dsize / 2, 0]) #11
        newpoints.append([center2, depth / 2 + b, 0]) #12
        newpoints.append([center2 + x, depth / 2 + b + y, 0]) #13
        newpoints.append([center2 + w * b + x, depth / 2 + y, 0]) #14
        newpoints.append([center2 + w * b, depth / 2, 0]) #15
        newpoints.append([width-center2, depth / 2, 0]) #16
        newpoints.append([width-center2, dsize / 2, 0]) #17
        newpoints.append([width + center1, dsize / 2, 0]) #18
        newpoints.append([width + center1, depth / 2 + b, 0]) #19
        newpoints.append([width + center1 + x, depth / 2 + b + y, 0]) #20
        newpoints.append([width + center1 + w * b + x, depth / 2 + y, 0]) #21
        newpoints.append([width + center1 + w * b, depth / 2, 0]) #22
        newpoints.append([width + center1 + w * dsize / 2, depth / 2, 0]) #23
        newpoints.append([width + center1 + w * dsize / 2, -depth / 2, 0]) #24
        newpoints.append([width + center1, -depth / 2, 0]) #25
        newpoints.append([width + center1, -dsize / 2, 0]) #26
        newpoints.append([width-center2, -dsize / 2, 0]) #29
        newpoints.append([width-center2, -depth / 2-b, 0]) #30
        newpoints.append([width-center2-x, -depth / 2-b-y, 0]) #31
        newpoints.append([width-center2-w * b-x, -depth / 2-y, 0]) #32
        newpoints.append([width-center2-w * b, -depth / 2, 0]) #33
        newpoints.append([center2, -depth / 2, 0]) #34
        newpoints.append([center2, -dsize / 2, 0]) #35
    
    elif arrow == 'Serifs2':
        b = sqrt(depth * depth / 2)
        x = sin(radians(45)) * arrowlength * w
        y = cos(radians(45)) * arrowlength
        newpoints.append([-center1 + w * b, -depth / 2, 0]) #3
        newpoints.append([-center1-x, -depth / 2-b-y, 0]) #4
        newpoints.append([-center1-w * b-x, -depth / 2-y, 0]) #5
        newpoints.append([center2 + x, depth / 2 + b + y, 0]) #13
        newpoints.append([center2 + w * b + x, depth / 2 + y, 0]) #14
        newpoints.append([center2 + w * b, depth / 2, 0]) #15
        newpoints.append([width + center1-w * b, depth / 2, 0]) #19
        newpoints.append([width + center1 + x, depth / 2 + b + y, 0]) #20
        newpoints.append([width + center1 + w * b + x, depth / 2 + y, 0]) #21
        newpoints.append([width-center2-x, -depth / 2-b-y, 0]) #31
        newpoints.append([width-center2-w * b-x, -depth / 2-y, 0]) #32
        newpoints.append([width-center2-w * b, -depth / 2, 0]) #33
    
    elif arrow == 'Without':
        newpoints.append([0, depth / 2, 0]) #3
        newpoints.append([width, depth / 2, 0]) #4
        newpoints.append([width, -depth / 2, 0]) #8
        newpoints.append([0, -depth / 2, 0]) #9
    
    return newpoints


def Linear3(width = 2, length = 2, dsize = 1, depth = 0.1, center = False, arrow = 'Arrow1', arrowdepth = 0.25, arrowlength = 0.25):
    
    newpoints = []
    
    w = 1
    if width < 0:
        w = -1
    l = 1
    if length < 0:
        l = -1

    if center:
       center1 = w * depth / 2
       center2 = w * depth / 2
    else:
       center1 = 0
       center2 = w * depth
    
    if arrow == 'Arrow1':
        newpoints.append([-center1, 0, 0]) #1
        newpoints.append([-center1, length, 0]) #2
        newpoints.append([-center1, length + l * dsize / 2-l * depth / 100, 0]) #3
        newpoints.append([-center1-w * arrowlength, length + l * dsize / 2-l * arrowdepth-l * depth / 2, 0]) #4
        newpoints.append([-center1-w * arrowlength, length + l * dsize / 2-l * depth / 2, 0]) #5
        newpoints.append([-center1-w * arrowlength-w * dsize / 2, length + l * dsize / 2-l * depth / 2, 0]) #6
        newpoints.append([-center1-w * arrowlength-w * dsize / 2, length + l * dsize / 2 + l * depth / 2, 0]) #7
        newpoints.append([-center1-w * arrowlength, length + l * dsize / 2 + l * depth / 2, 0]) #8
        newpoints.append([-center1-w * arrowlength, length + l * dsize / 2 + l * arrowdepth + l * depth / 2, 0]) #9
        newpoints.append([-center1, length + l * dsize / 2 + l * depth / 100, 0]) #10
        newpoints.append([-center1, length + l * dsize, 0]) #11
        newpoints.append([center2, length + l * dsize, 0]) #12
        newpoints.append([center2, length + l * dsize / 2 + l * depth / 2, 0]) #13
        newpoints.append([width-center2, length + l * dsize / 2 + l * depth / 2, 0]) #14
        newpoints.append([width-center2, length + l * dsize, 0]) #15
        newpoints.append([width + center1, length + l * dsize, 0]) #16
        newpoints.append([width + center1, length + l * dsize / 2 + l * depth / 100, 0]) #17
        newpoints.append([width + center1 + w * arrowlength, length + l * dsize / 2 + l * arrowdepth + l * depth / 2, 0]) #18
        newpoints.append([width + center1 + w * arrowlength, length + l * dsize / 2 + l * depth / 2, 0]) #19
        newpoints.append([width + center1 + w * arrowlength + w * dsize / 2, length + l * dsize / 2 + l * depth / 2, 0]) #20
        newpoints.append([width + center1 + w * arrowlength + w * dsize / 2, length + l * dsize / 2-l * depth / 2, 0]) #21
        newpoints.append([width + center1 + w * arrowlength, length + l * dsize / 2-l * depth / 2, 0]) #22
        newpoints.append([width + center1 + w * arrowlength, length + l * dsize / 2-l * arrowdepth-l * depth / 2, 0]) #23
        newpoints.append([width + center1, length + l * dsize / 2-l * depth / 100, 0]) #24
        newpoints.append([width + center1, length, 0]) #25
        newpoints.append([width + center1, 0, 0]) #26
        newpoints.append([width-center2, 0, 0]) #27
        newpoints.append([width-center2, length, 0]) #28
        newpoints.append([width-center2, length + l * dsize / 2-l * depth / 2, 0]) #29
        newpoints.append([center2, length + l * dsize / 2-l * depth / 2, 0]) #30
        newpoints.append([center2, length, 0]) #31
        newpoints.append([center2, 0, 0]) #32
    
    if arrow == 'Arrow2':
        newpoints.append([-center1, 0, 0]) #1
        newpoints.append([-center1, length, 0]) #2
        newpoints.append([-center1, length + l * dsize / 2-l * depth / 100, 0]) #3
        newpoints.append([-center1-w * arrowlength, length + l * dsize / 2-l * arrowdepth-l * depth / 2, 0]) #4
        newpoints.append([-center1-w * arrowlength * 3 / 4, length + l * dsize / 2-l * depth / 2, 0]) #5
        newpoints.append([-center1-w * arrowlength-w * dsize, length + l * dsize / 2-l * depth / 2, 0]) #6
        newpoints.append([-center1-w * arrowlength-w * dsize, length + l * dsize / 2 + l * depth / 2, 0]) #7
        newpoints.append([-center1-w * arrowlength * 3 / 4, length + l * dsize / 2 + l * depth / 2, 0]) #8
        newpoints.append([-center1-w * arrowlength, length + l * dsize / 2 + l * arrowdepth + l * depth / 2, 0]) #9
        newpoints.append([-center1, length + l * dsize / 2 + l * depth / 100, 0]) #10
        newpoints.append([-center1, length + l * dsize, 0]) #11
        newpoints.append([center2, length + l * dsize, 0]) #12
        newpoints.append([center2, length + l * dsize / 2 + l * depth / 2, 0]) #13
        newpoints.append([width-center2, length + l * dsize / 2 + l * depth / 2, 0]) #14
        newpoints.append([width-center2, length + l * dsize, 0]) #15
        newpoints.append([width + center1, length + l * dsize, 0]) #16
        newpoints.append([width + center1, length + l * dsize / 2 + l * depth / 100, 0]) #17
        newpoints.append([width + center1 + w * arrowlength, length + l * dsize / 2 + l * arrowdepth + l * depth / 2, 0]) #18
        newpoints.append([width + center1 + w * arrowlength * 3 / 4, length + l * dsize / 2 + l * depth / 2, 0]) #19
        newpoints.append([width + center1 + w * arrowlength + w * dsize, length + l * dsize / 2 + l * depth / 2, 0]) #20
        newpoints.append([width + center1 + w * arrowlength + w * dsize, length + l * dsize / 2-l * depth / 2, 0]) #21
        newpoints.append([width + center1 + w * arrowlength * 3 / 4, length + l * dsize / 2-l * depth / 2, 0]) #22
        newpoints.append([width + center1 + w * arrowlength, length + l * dsize / 2-l * arrowdepth-l * depth / 2, 0]) #23
        newpoints.append([width + center1, length + l * dsize / 2-l * depth / 100, 0]) #24
        newpoints.append([width + center1, length, 0]) #25
        newpoints.append([width + center1, 0, 0]) #26
        newpoints.append([width-center2, 0, 0]) #27
        newpoints.append([width-center2, length, 0]) #28
        newpoints.append([width-center2, length + l * dsize / 2-l * depth / 2, 0]) #29
        newpoints.append([center2, length + l * dsize / 2-l * depth / 2, 0]) #30
        newpoints.append([center2, length, 0]) #31
        newpoints.append([center2, 0, 0]) #32
    
    elif arrow == 'Serifs1':
        b = sqrt(depth * depth / 2)
        x = sin(radians(45)) * arrowlength * w
        y = cos(radians(45)) * arrowlength * l
        newpoints.append([-center1, 0, 0]) #1
        newpoints.append([-center1, length, 0]) #2
        newpoints.append([-center1, length + l * dsize / 2-l * depth / 2-l * b, 0]) #3
        newpoints.append([-center1-x, length + l * dsize / 2-l * depth / 2-l * b-y, 0]) #4
        newpoints.append([-center1-w * b-x, length + l * dsize / 2-l * depth / 2-y, 0]) #5
        newpoints.append([-center1-w * b, length + l * dsize / 2-l * depth / 2, 0]) #6
        newpoints.append([-center1-w * dsize / 2, length + l * dsize / 2-l * depth / 2, 0]) #7
        newpoints.append([-center1-w * dsize / 2, length + l * dsize / 2 + l * depth / 2, 0]) #8
        newpoints.append([-center1, length + l * dsize / 2 + l * depth / 2, 0]) #9
        newpoints.append([-center1, length + l * dsize, 0]) #10
        newpoints.append([center2, length + l * dsize, 0]) #11
        newpoints.append([center2, length + l * dsize / 2 + l * depth / 2 + l * b, 0]) #12
        newpoints.append([center2 + x, length + l * dsize / 2 + l * depth / 2 + l * b + y, 0]) #13
        newpoints.append([center2 + w * b + x, length + l * dsize / 2 + l * depth / 2 + y, 0]) #14
        newpoints.append([center2 + w * b, length + l * dsize / 2 + l * depth / 2, 0]) #15
        newpoints.append([width-center2, length + l * dsize / 2 + l * depth / 2, 0]) #16
        newpoints.append([width-center2, length + l * dsize, 0]) #17
        newpoints.append([width + center1, length + l * dsize, 0]) #18
        newpoints.append([width + center1, length + l * dsize / 2 + l * depth / 2 + l * b, 0]) #19
        newpoints.append([width + center1 + x, length + l * dsize / 2 + l * depth / 2 + l * b + y, 0]) #20
        newpoints.append([width + center1 + w * b + x, length + l * dsize / 2 + l * depth / 2 + y, 0]) #21
        newpoints.append([width + center1 + w * b, length + l * dsize / 2 + l * depth / 2, 0]) #22
        newpoints.append([width + center1 + w * dsize / 2, length + l * dsize / 2 + l * depth / 2, 0]) #23
        newpoints.append([width + center1 + w * dsize / 2, length + l * dsize / 2-l * depth / 2, 0]) #24
        newpoints.append([width + center1, length + l * dsize / 2-l * depth / 2, 0]) #25
        newpoints.append([width + center1, length, 0]) #26
        newpoints.append([width + center1, 0, 0]) #27
        newpoints.append([width-center2, 0, 0]) #28
        newpoints.append([width-center2, length, 0]) #29
        newpoints.append([width-center2, length + l * dsize / 2-l * depth / 2-l * b, 0]) #30
        newpoints.append([width-center2-x, length + l * dsize / 2-l * depth / 2-l * b-y, 0]) #31
        newpoints.append([width-center2-w * b-x, length + l * dsize / 2-l * depth / 2-y, 0]) #32
        newpoints.append([width-center2-w * b, length + l * dsize / 2-l * depth / 2, 0]) #33
        newpoints.append([center2, length + l * dsize / 2-l * depth / 2, 0]) #34
        newpoints.append([center2, length, 0]) #35
        newpoints.append([center2, 0, 0]) #36
    
    elif arrow == 'Serifs2':
        b = sqrt(depth * depth / 2)
        x = sin(radians(45)) * arrowlength * w
        y = cos(radians(45)) * arrowlength * l
        newpoints.append([-center1, 0, 0]) #1
        newpoints.append([-center1, length, 0]) #2
        newpoints.append([-center1, length + l * dsize / 2-l * depth / 2-l * b, 0]) #3
        newpoints.append([-center1-x, length + l * dsize / 2-l * depth / 2-l * b-y, 0]) #4
        newpoints.append([-center1-w * b-x, length + l * dsize / 2-l * depth / 2-y, 0]) #5
        newpoints.append([-center1-w * b, length + l * dsize / 2-l * depth / 2, 0]) #6
        newpoints.append([-center1-w * dsize, length + l * dsize / 2-l * depth / 2, 0]) #7
        newpoints.append([-center1-w * dsize, length + l * dsize / 2 + l * depth / 2, 0]) #8
        newpoints.append([-center1, length + l * dsize / 2 + l * depth / 2, 0]) #9
        newpoints.append([-center1, length + l * dsize, 0]) #10
        newpoints.append([center2, length + l * dsize, 0]) #11
        newpoints.append([center2, length + l * dsize / 2 + l * depth / 2 + l * b, 0]) #12
        newpoints.append([center2 + x, length + l * dsize / 2 + l * depth / 2 + l * b + y, 0]) #13
        newpoints.append([center2 + w * b + x, length + l * dsize / 2 + l * depth / 2 + y, 0]) #14
        newpoints.append([center2 + w * b, length + l * dsize / 2 + l * depth / 2, 0]) #15
        newpoints.append([width-center2, length + l * dsize / 2 + l * depth / 2, 0]) #16
        newpoints.append([width-center2, length + l * dsize, 0]) #17
        newpoints.append([width + center1, length + l * dsize, 0]) #18
        newpoints.append([width + center1, length + l * dsize / 2 + l * depth / 2 + l * b, 0]) #19
        newpoints.append([width + center1 + x, length + l * dsize / 2 + l * depth / 2 + l * b + y, 0]) #20
        newpoints.append([width + center1 + w * b + x, length + l * dsize / 2 + l * depth / 2 + y, 0]) #21
        newpoints.append([width + center1 + w * b, length + l * dsize / 2 + l * depth / 2, 0]) #22
        newpoints.append([width + center1 + w * dsize, length + l * dsize / 2 + l * depth / 2, 0]) #23
        newpoints.append([width + center1 + w * dsize, length + l * dsize / 2-l * depth / 2, 0]) #24
        newpoints.append([width + center1, length + l * dsize / 2-l * depth / 2, 0]) #25
        newpoints.append([width + center1, length, 0]) #26
        newpoints.append([width + center1, 0, 0]) #27
        newpoints.append([width-center2, 0, 0]) #28
        newpoints.append([width-center2, length, 0]) #29
        newpoints.append([width-center2, length + l * dsize / 2-l * depth / 2-l * b, 0]) #30
        newpoints.append([width-center2-x, length + l * dsize / 2-l * depth / 2-l * b-y, 0]) #31
        newpoints.append([width-center2-w * b-x, length + l * dsize / 2-l * depth / 2-y, 0]) #32
        newpoints.append([width-center2-w * b, length + l * dsize / 2-l * depth / 2, 0]) #33
        newpoints.append([center2, length + l * dsize / 2-l * depth / 2, 0]) #34
        newpoints.append([center2, length, 0]) #35
        newpoints.append([center2, 0, 0]) #36
    
    elif arrow == 'Without':
        newpoints.append([-center1, 0, 0]) #1
        newpoints.append([-center1, length, 0]) #2
        newpoints.append([-center1, length + l * dsize / 2-l * depth / 2, 0]) #5
        newpoints.append([-center1-w * dsize / 2, length + l * dsize / 2-l * depth / 2, 0]) #6
        newpoints.append([-center1-w * dsize / 2, length + l * dsize / 2 + l * depth / 2, 0]) #7
        newpoints.append([-center1, length + l * dsize / 2 + l * depth / 2, 0]) #8
        newpoints.append([-center1, length + l * dsize, 0]) #11
        newpoints.append([center2, length + l * dsize, 0]) #12
        newpoints.append([center2, length + l * dsize / 2 + l * depth / 2, 0]) #13
        newpoints.append([width-center2, length + l * dsize / 2 + l * depth / 2, 0]) #14
        newpoints.append([width-center2, length + l * dsize, 0]) #15
        newpoints.append([width + center1, length + l * dsize, 0]) #16
        newpoints.append([width + center1, length + l * dsize / 2 + l * depth / 2, 0]) #19
        newpoints.append([width + center1 + w * dsize / 2, length + l * dsize / 2 + l * depth / 2, 0]) #20
        newpoints.append([width + center1 + w * dsize / 2, length + l * dsize / 2-l * depth / 2, 0]) #21
        newpoints.append([width + center1, length + l * dsize / 2-l * depth / 2, 0]) #22
        newpoints.append([width + center1, length, 0]) #25
        newpoints.append([width + center1, 0, 0]) #26
        newpoints.append([width-center2, 0, 0]) #27
        newpoints.append([width-center2, length, 0]) #28
        newpoints.append([width-center2, length + l * dsize / 2-l * depth / 2, 0]) #29
        newpoints.append([center2, length + l * dsize / 2-l * depth / 2, 0]) #30
        newpoints.append([center2, length, 0]) #31
        newpoints.append([center2, 0, 0]) #32

    return newpoints
