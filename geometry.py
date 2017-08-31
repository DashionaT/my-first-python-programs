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

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))
