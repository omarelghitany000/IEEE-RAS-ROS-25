class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imag = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denominator = other.real*2 + other.imaginary*2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imag = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex(real, imag)

    def __str__(self):
        sign = '+' if self.imaginary >= 0 else '-'
        return f"{self.real:.2f}{sign}{abs(self.imaginary):.2f}i"


a =Complex(2, 1)
b =Complex(4, 6)

print("A + B =", a + b)
print("A - B =", a - b)
print("A * B =", a * b)
print("A / B =", a / b)
