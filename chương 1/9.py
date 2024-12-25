class Polygon:
    def __init__(self, sides):
        self.sides = sides
    
    def perimeter(self):
        return sum(self.sides)
    
    def area(self):
        pass  # Tính diện tích tùy theo loại đa giác

class Parallelogram(Polygon):
    def __init__(self, base, height):
        super().__init__([base, base, height, height])
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height

class Rectangle(Parallelogram):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width
        self.height = height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# Chương trình chính
square = Square(5)
print("Diện tích hình vuông:", square.area())
