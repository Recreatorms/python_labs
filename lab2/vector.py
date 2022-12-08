import numpy as np


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.x

    @x.setter
    def _(self, x):
        self.x = x

    @property
    def y(self):
        return self.y

    @y.setter
    def _(self, y):
        self.y = y

    @staticmethod
    def __operate(f, u, v):
        return Vector(*f(u, v))

    def __add__(self, other):
        return Vector.__operate(lambda u, v: (u.x + v.x, u.y + v.y),
                                self, other)

    def __sub__(self, other):
        return Vector.__operate(lambda u, v: (u.x - v.x, u.y - v.y),
                                self, other)

    def __mul__(self, other):
        if type(other) is Vector:
            return (self.x * other.x + self.y * other.y)
        return Vector.__operate(lambda u, v: (u.x * v, u.y * v),
                                self, other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __abs__(self):
        return np.sqrt(Vector.__mul__(self, self))

    def __str__(self):
        return f"<{self.x}; {self.y}>"

    def __repr__(self):
        return f"<{self.x}; {self.y}>"

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __ne__(self, __o: object) -> bool:
        return not (self.x == __o.x and self.y == __o.y)
