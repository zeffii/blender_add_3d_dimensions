# star is OK here, the entirety of math is imported anyway,
# and there is no namespace polution in this case
# .. no hobgoblins.
from math import *


def Note(width = 2, length = 2, depth = 0.1, angle = 45, arrow = 'Arrow1', arrowdepth = 0.25, arrowlength = 0.25):
    
    newpoints = []
    
    if arrow == 'Serifs1' or arrow == 'Serifs2':
        arrow = 'Without'
    
    w = 1
    if width < 0:
        w = -1
    angle = radians(angle)
    length = abs(length)
    
    if cos(angle) > 0:
        newpoints.append([0, 0, 0]) #1
        
        if arrow == 'Arrow1':
            g = hypot(arrowlength, depth / 2 + arrowdepth)
            u = asin((depth / 2 + arrowdepth) / g)
            x = cos(angle + u) * g
            y = sin(angle + u) * g
            newpoints.append([w * x, y, 0]) #2
        
            g = hypot(arrowlength, depth / 2)
            u = asin((depth / 2) / g)
            x = cos(angle + u) * g
            y = sin(angle + u) * g
            newpoints.append([w * x, y, 0]) #3
        
        if arrow == 'Arrow2':
            g = hypot(arrowlength, depth / 2 + arrowdepth)
            u = asin((depth / 2 + arrowdepth) / g)
            x = cos(angle + u) * g
            y = sin(angle + u) * g
            newpoints.append([w * x, y, 0]) #2
            
            g = hypot(arrowlength * 3 / 4, depth / 2)
            u = asin((depth / 2) / g)
            x = cos(angle + u) * g
            y = sin(angle + u) * g
            newpoints.append([w * x, y, 0]) #3

        if arrow == 'Without':
            g = w * depth / 2
            x = cos(angle + radians(90)) * g
            y = sin(angle + radians(90)) * g
            newpoints.append([x, y, 0]) #2
            
        g = hypot(width, depth / 2)
        u = asin((depth / 2) / g)
        x = cos(angle + u) * g
        y = sin(angle) * width
        newpoints.append([w * x, y + w * depth / 2, 0]) #4
    
        newpoints.append([w * x + w * length, y + w * depth / 2, 0]) #5
        newpoints.append([w * x + w * length, y-w * depth / 2, 0]) #6
        
        g = hypot(width, depth / 2)
        u = asin((depth / 2) / g)
        y = sin(angle) * width
        x = cos(angle-u) * g
        newpoints.append([w * x, y-w * depth / 2, 0]) #7
        
        if arrow == 'Arrow1':
            g = hypot(arrowlength, depth / 2)
            u = asin((depth / 2) / g)
            x = cos(angle-u) * g
            y = sin(angle-u) * g
            newpoints.append([w * x, y, 0]) #8
            
            g = hypot(arrowlength, depth / 2 + arrowdepth)
            u = asin((depth / 2 + arrowdepth) / g)
            x = cos(angle-u) * g
            y = sin(angle-u) * g
            newpoints.append([w * x, y, 0]) #9
            
        if arrow == 'Arrow2':
            g = hypot(arrowlength * 3 / 4, depth / 2)
            u = asin((depth / 2) / g)
            x = cos(angle-u) * g
            y = sin(angle-u) * g
            newpoints.append([w * x, y, 0]) #8
        
            g = hypot(arrowlength, depth / 2 + arrowdepth)
            u = asin((depth / 2 + arrowdepth) / g)
            x = cos(angle-u) * g
            y = sin(angle-u) * g
            newpoints.append([w * x, y, 0]) #9
            
        if arrow == 'Without':
            g = -w * depth / 2
            x = cos(angle + radians(90)) * g
            y = sin(angle + radians(90)) * g
            newpoints.append([x, y, 0]) #6
        
    else:
        newpoints.append([0, 0, 0]) #1
        
        if arrow == 'Arrow1':
            g = hypot(arrowlength, depth / 2 + arrowdepth)
            u = asin((depth / 2 + arrowdepth) / g)
            x = cos(angle-u) * g
            y = sin(angle-u) * g
            newpoints.append([w * x, y, 0]) #2
        
            g = hypot(arrowlength, depth / 2)
            u = asin((depth / 2) / g)
            x = cos(angle-u) * g
            y = sin(angle-u) * g
            newpoints.append([w * x, y, 0]) #3
        
        if arrow == 'Arrow2':
            g = hypot(arrowlength, depth / 2 + arrowdepth)
            u = asin((depth / 2 + arrowdepth) / g)
            x = cos(angle-u) * g
            y = sin(angle-u) * g
            newpoints.append([w * x, y, 0]) #2
            
            g = hypot(arrowlength * 3 / 4, depth / 2)
            u = asin((depth / 2) / g)
            x = cos(angle-u) * g
            y = sin(angle-u) * g
            newpoints.append([w * x, y, 0]) #3
        
        if arrow == 'Without':
            g = -w * depth / 2
            x = cos(angle + radians(90)) * g
            y = sin(angle + radians(90)) * g
            newpoints.append([x, y, 0]) #2
        
        g = hypot(width, depth / 2)
        u = asin((depth / 2) / g)
        x = cos(angle-u) * g
        y = sin(angle) * width
        newpoints.append([w * x, y + w * depth / 2, 0]) #4
    
        newpoints.append([w * x-w * length, y + w * depth / 2, 0]) #5
        newpoints.append([w * x-w * length, y-w * depth / 2, 0]) #6
        
        g = hypot(width, depth / 2)
        u = asin((depth / 2) / g)
        y = sin(angle) * width
        x = cos(angle + u) * g
        newpoints.append([w * x, y-w * depth / 2, 0]) #7
        
        if arrow == 'Arrow1':
            g = hypot(arrowlength, depth / 2)
            u = asin((depth / 2) / g)
            x = cos(angle + u) * g
            y = sin(angle + u) * g
            newpoints.append([w * x, y, 0]) #8
            
            g = hypot(arrowlength, depth / 2 + arrowdepth)
            u = asin((depth / 2 + arrowdepth) / g)
            x = cos(angle + u) * g
            y = sin(angle + u) * g
            newpoints.append([w * x, y, 0]) #9
            
        if arrow == 'Arrow2':
            g = hypot(arrowlength * 3 / 4, depth / 2)
            u = asin((depth / 2) / g)
            x = cos(angle + u) * g
            y = sin(angle + u) * g
            newpoints.append([w * x, y, 0]) #8
        
            g = hypot(arrowlength, depth / 2 + arrowdepth)
            u = asin((depth / 2 + arrowdepth) / g)
            x = cos(angle + u) * g
            y = sin(angle + u) * g
            newpoints.append([w * x, y, 0]) #9
        
        if arrow == 'Without':
            g = w * depth / 2
            x = cos(angle + radians(90)) * g
            y = sin(angle + radians(90)) * g
            newpoints.append([x, y, 0]) #6

    return newpoints
