# This program demonstrates how to use the math module.
#
# Dashiona Todd
# August 22, 2014

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

def parallelogram_area(b, h):
    a = b * h
    return a

def trapezoid_area(c, b, h):
    a = (c + b / 2) * h
    return a

def rectangular_prism_volume(w, h, l):
    v = w * h * l
    return v

def cone_volume(r, h):
    v = (math.pi * r**2) * h / 3
    return v

def sphere_volume(r):
    v = (4 / 3) * math.pi * r**3
    return v

def rectangular_prism_surface_area(l, w, h):
    a = 2 * ( w * l + h * l + h * w)
    return a

def sphere_surface_area(r):
    a = 4 * math.pi * r**2
    return a

def hypotenuse(a, b):
   h = (math.sqrt(a**2 + b**2))
   return h

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))
print(parallelogram_area(4,3))
print(trapezoid_area(5,2,9))
print(rectangular_prism_volume(9,4,7))
print(cone_volume(6,4))
print(circle_area(9))
print(rectangular_prism_surface_area(2,3,7))
print(sphere_surface_area(3))
print(hypotenuse(4,6))
