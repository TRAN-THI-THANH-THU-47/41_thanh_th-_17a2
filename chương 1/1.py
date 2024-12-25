class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0
    
    def input_data(self):
        self.length = float(input("Nhập độ dài cạnh của hình chữ nhật: "))
        self.width = float(input("Nhập độ rộng cạnh của hình chữ nhật: "))
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def area(self):
        return self.length * self.width
    
    def print_info(self):
        print(f"Hình chữ nhật có độ dài {self.length} và độ rộng {self.width}")
        print(f"Chu vi: {self.perimeter()}")
        print(f"Diện tích: {self.area()}")

# Chương trình chính
rect = Rectangle()
rect.input_data()
rect.print_info()
