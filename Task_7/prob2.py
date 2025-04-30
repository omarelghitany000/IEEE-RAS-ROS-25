import math

class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Point(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

# Given points
A = Point(7, 4, 5)
B = Point(1, 7, 6)
C = Point(0, 5, 9)
D = Point(1, 7, 2)

# Vectors
AB = B - A  # (1, 7, 6) - (7, 4, 5) = (-6, 3, 1)
BC = C - B  # (0, 5, 9) - (1, 7, 6) = (-1, -2, 3)
CD = D - C  # (1, 7, 2) - (0, 5, 9) = (1, 2, -7)

# Normal vectors
X = AB.cross(BC)
Y = BC.cross(CD)

# Calculate the angle
angle = math.degrees(math.acos(X.dot(Y) / (X.magnitude() * Y.magnitude())))

# Output the result
print(f"{angle:.2f}")
