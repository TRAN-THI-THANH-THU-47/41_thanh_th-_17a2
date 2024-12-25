class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ellipse(Point):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b
    
    def area(self):
        import math
        return math.pi * self.a * self.b

class Circle(Ellipse):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r)

# Chương trình chính
circle = Circle(0, 0, 5)
print("Diện tích đường tròn:", circle.area())
