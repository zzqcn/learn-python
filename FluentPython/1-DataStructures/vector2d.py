#!/usr/bin/env python3

"""
1.3 二维向量
"""

import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'
    
    # def __str__(self):
    #     return f'({self.x}, {self.y})'

    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1)
print(repr(v1))
print(str(v1))
print(v1 + v2)

v = Vector(3, 4)
print(abs(v))

# if v:
#     print(True)
# if Vector(0, 0):
#     print(True)
# else:
#     print(False)
print(bool(v))
print(bool(Vector(0, 0)))

print(v * 3)
print(abs(v * 3))
