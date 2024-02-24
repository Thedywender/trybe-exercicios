from math import pi as PI

class Circle(GeometricFigure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * (self.radius ** 2)

    def perimeter(self):
        return 2 * PI * self.radius

