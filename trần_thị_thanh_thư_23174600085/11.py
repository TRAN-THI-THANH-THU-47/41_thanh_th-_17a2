import math

class Triangle:
    def __init__(self, a, b, c):
        self.sides = [a, b, c]

    def area(self):
        s = sum(self.sides) / 2
        return math.sqrt(s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]))

class RightTriangle(Triangle):
    def __init__(self, base, height):
        super().__init__(base, height, math.sqrt(base**2 + height**2))

class IsoscelesTriangle(Triangle):
    def __init__(self, base, height):
        super().__init__(base, height, height)

class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side):
        super().__init__(side, (math.sqrt(3) / 2) * side)

def main():
    base = float(input("Nhập cạnh đáy của tam giác vuông: "))
    height = float(input("Nhập cạnh cao của tam giác vuông: "))
    rt = RightTriangle(base, height)
    print(f"Tam giác vuông: Diện tích = {rt.area()}")

    base = float(input("Nhập cạnh đáy của tam giác cân: "))
    height = float(input("Nhập chiều cao của tam giác cân: "))
    it = IsoscelesTriangle(base, height)
    print(f"Tam giác cân: Diện tích = {it.area()}")

    side = float(input("Nhập cạnh của tam giác đều: "))
    et = EquilateralTriangle(side)
    print(f"Tam giác đều: Diện tích = {et.area()}")

main()
