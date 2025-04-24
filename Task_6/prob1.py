class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
circle =Circle(4)

print("The Area =:", circle.area())
print("The Perimeter =:", circle.perimeter())

    