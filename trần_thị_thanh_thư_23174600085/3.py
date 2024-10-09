import math

class PhanSo:
    def __init__(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        if self.mau_so == 0:
            raise ValueError("Mẫu số phải khác 0.")
        self.rut_gon()

    def rut_gon(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

    def in_phan_so(self):
        print(f"{self.tu_so}" if self.mau_so == 1 else f"{self.tu_so}/{self.mau_so}")

# Chương trình chính
ps = PhanSo()
ps.in_phan_so()
