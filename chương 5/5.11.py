import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect("ql_nhan_vien.db")
cursor = conn.cursor()

# Tạo bảng PHONG
cursor.execute("""
CREATE TABLE IF NOT EXISTS PHONG (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
);
""")

# Tạo bảng NHAN_VIEN
cursor.execute("""
CREATE TABLE IF NOT EXISTS NHAN_VIEN (
    Id INTEGER PRIMARY KEY,
    Ho_Ten TEXT NOT NULL,
    Tuoi INTEGER NOT NULL,
    Dia_Chi TEXT NOT NULL,
    Luong REAL NOT NULL,
    Id_phong INTEGER,
    FOREIGN KEY (Id_phong) REFERENCES PHONG(Id)
);
""")

# Hàm thêm phòng
def add_phong(name, price, amount):
    cursor.execute("INSERT INTO PHONG (Name, Price, Amount) VALUES (?, ?, ?);", (name, price, amount))
    conn.commit()
    print("Phòng đã được thêm.")

# Hàm thêm nhân viên
def add_nhan_vien(ho_ten, tuoi, dia_chi, luong, id_phong):
    cursor.execute("INSERT INTO NHAN_VIEN (Ho_Ten, Tuoi, Dia_Chi, Luong, Id_phong) VALUES (?, ?, ?, ?, ?);", 
                   (ho_ten, tuoi, dia_chi, luong, id_phong))
    conn.commit()
    print("Nhân viên đã được thêm.")

# Hàm hiển thị nhân viên
def display_nhan_vien():
    cursor.execute("SELECT * FROM NHAN_VIEN;")
    nhan_vien = cursor.fetchall()
    for nv in nhan_vien:
        print(nv)

# Ví dụ sử dụng:
add_phong("Phòng Kinh Doanh", 5000.0, 3)  # Thêm phòng
add_nhan_vien("Nguyễn Văn A", 30, "Hà Nội", 1000.0, 1)  # Thêm nhân viên
display_nhan_vien()  # Hiển thị nhân viên

# Đóng kết nối
conn.close()
