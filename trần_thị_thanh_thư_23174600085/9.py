class DaGiac:
    def __init__(self, canh):
        self.canh = canh

    def tinh_chu_vi(self):
        return sum(self.canh)

class HinhBinhHanh(DaGiac):
    def __init__(self, canh_a, canh_b, goc):
        super().__init__([canh_a, canh_b, canh_a, canh_b])
        self.goc = goc


class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong, 90)

    def tinh_dien_tich(self):
        return self.canh[0] * self.canh[1]

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)


# Tạo một hình vuông
hinh_vuong = HinhVuong(5)
print("Chu vi hình vuông:", hinh_vuong.tinh_chu_vi())
print("Diện tích hình vuông:", hinh_vuong.tinh_dien_tich())

# Tạo một hình chữ nhật
hinh_chu_nhat = HinhChuNhat(4, 6)
print("Chu vi hình chữ nhật:", hinh_chu_nhat.tinh_chu_vi())
print("Diện tích hình chữ nhật:", hinh_chu_nhat.tinh_dien_tich())
