class Fraction:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1
    
    def is_valid(self):
        return self.denominator != 0
    
    def input_data(self):
        self.numerator = int(input("Nhập tử số: "))
        self.denominator = int(input("Nhập mẫu số: "))
    
    def print_fraction(self):
        if self.is_valid():
            print(f"Phân số: {self.numerator}/{self.denominator}")
        else:
            print("Phân số không hợp lệ (mẫu số không thể bằng 0).")

# Chương trình chính
frac = Fraction()
frac.input_data()
frac.print_fraction()
