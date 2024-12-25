class Triangle:
    def __init__(self, a, b, c):
        self.sides = [a, b, c]
    
    def perimeter(self):
        return sum(self.sides)
    
    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2])) ** 0.5

class RightTriangle(Triangle):
    def __init__(self, base, height):
        super().__init__(base, height, (base**2 + height**2) ** 0.5)

class IsoscelesTriangle(Triangle):
    def __init__(self, equal_side, base):
        super().__init__(equal_side, equal_side, base)

class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side):
        super().__init__(side, side)

# Chương trình chính
equilateral = EquilateralTriangle(5)
print("Diện tích tam giác đều:", equilateral.area())
