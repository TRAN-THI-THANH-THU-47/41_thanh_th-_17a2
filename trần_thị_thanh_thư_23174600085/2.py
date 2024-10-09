class ThiSinh:
    def __init__(self, ho_ten='', diem_toan=0, diem_ly=0, diem_hoa=0):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hoá: "))


    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa


    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}, Điểm Lý: {self.diem_ly}, Điểm Hoá: {self.diem_hoa}")
        print(f"Tổng điểm: {self.tinh_tong_diem()}")

def nhap_danh_sach_thi_sinh():
    danh_sach = []
    so_luong = int(input("Nhập số lượng thí sinh: "))
    for i in range(so_luong):
        print(f"Nhập thông tin thí sinh thứ {i+1}:")
        ts = ThiSinh()
        ts.nhap_thong_tin()
        danh_sach.append(ts)
    return danh_sach

def in_danh_sach_trung_tuyen(danh_sach, diem_chuan=20):
    danh_sach_trung_tuyen = [ts for ts in danh_sach if ts.tinh_tong_diem() >= diem_chuan]
   
    danh_sach_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)

    if not danh_sach_trung_tuyen:
        print("Không có thí sinh nào trúng tuyển.")
    else:
        print("\nDanh sách thí sinh trúng tuyển (điểm từ cao xuống thấp):")
        for ts in danh_sach_trung_tuyen:
            ts.in_thong_tin()
            print("-" * 30)
danh_sach_thi_sinh = nhap_danh_sach_thi_sinh()
in_danh_sach_trung_tuyen(danh_sach_thi_sinh)
