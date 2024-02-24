class Rectangle(GeometricFigure):
    def _init__(self. base, heigth):
        self.base = base
        self.heigth = heigth

    def area(self):
        return self.base * self.heigth

    def perimeter(self):
        return 2 * (self.base + self.heigth)