from vector import Vector

from figure import *

from decorator import Decorator

p1 = Vector(1, 2)
p2 = Vector(3, 4)
print(f"vector 1 = {p1}")
print(f"vector 2 = {p2}")
print(f"vec1 + vec2 = {p1+p2}")
print(f"vec1 - vec 2 = {p1-p2}")
print(f"vec1 * 3 = {p1*3}")
print(f"vec1&vec2 scalar = {Vector.scalarMult(p1,p2)}")
print(f"vec1 length = {p1.length()}")

print("\n\n")

rect = Rectangle(p1, p2)
print(f"Rectangle: {rect}")
print(f"Square of rectangle = {rect.square()}")

p1 = Vector(0, 0)
p2 = Vector(1, 0)
p3 = Vector(0, 1)
triangle = Triangle(p1, p2, p3)
print(f"Triange: {triangle}")
print(f"Square of triangle: {triangle.square()}")

circle = Circle(p1, 5)
print(f"Circle: {circle}")
print(f"Square of circle {circle.square()}")


@Decorator
def wrapped(args):
    print(f'{args } wrapped function')


wrapped(123)
