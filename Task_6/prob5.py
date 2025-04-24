import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def perimeter(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        super().__init__("Circle")
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


circle = Circle(3)
square = Square(4)

print(f"{circle.name} Area: {circle.area()}")
print(f"{circle.name} Perimeter: {circle.perimeter()}")

print(f"{square.name} Area: {square.area()}")
print(f"{square.name} Perimeter: {square.perimeter()}")
