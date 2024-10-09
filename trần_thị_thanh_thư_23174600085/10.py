import math

class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)  
        self.a = a  
        self.b = b  

    def tinh_dien_tich(self):
        return math.pi * self.a * self.b

class DuongTron(Elip):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r) 

# Nhập liệu từ người dùng
x = float(input("Nhập hoành độ tâm elip: "))
y = float(input("Nhập tung độ tâm elip: "))
a = float(input("Nhập bán trục lớn: "))
b = float(input("Nhập bán trục nhỏ: "))

# Tạo đối tượng elip
elip1 = Elip(x, y, a, b)

# Tính và in diện tích
dien_tich = elip1.tinh_dien_tich()
print("Diện tích elip là:", dien_tich)