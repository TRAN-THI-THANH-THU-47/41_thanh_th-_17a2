class HinhChuNhat:
    def __init__(self, chieu_dai=0, chieu_rong=0):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    def in_thong_tin(self):
        chu_vi = self.tinh_chu_vi()
        dien_tich = self.tinh_dien_tich()
        print(f"Chiều dài: {self.chieu_dai}")
        print(f"Chiều rộng: {self.chieu_rong}")
        print(f"Chu vi: {chu_vi}")
        print(f"Diện tích: {dien_tich}")


# Chương trình chính
hcn = HinhChuNhat()
hcn.nhap_du_lieu()
hcn.in_thong_tin()
