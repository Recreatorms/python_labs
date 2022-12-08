import math


class Figure:
    def square():
        raise NotImplementedError()


class Rectangle(Figure):
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight

    def square(self):
        height = abs(self.topLeft.y - self.bottomRight.y)
        width = abs(self.topLeft.x - self.__bottomRight.x)
        return height * width

    def __str__(self):
        return f"Top left = {self.topLeft}, Bottom right = {self.bottomRight}"


class Triangle(Figure):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):
        return f"Point 1 = {self.p1}, Point 2 = {self.p2}, Point 3 = {self.p3}"

    def square(self):
        return abs(self.p1.x*(self.p2.y-self.p3.y) +
                   self.p2.x*(self.p3.y-self.p1.y) +
                   self.p3.x*(self.p1.y-self.p2.y)) / 2


class Circle(Figure):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"Center = {self.center}, radius = {self.radius}"

    def square(self):
        return math.pi * self.radius * self.radius
