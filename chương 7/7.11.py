import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def convert_to_lunar():
    try:
        solar_year = int(entry_solar_year.get())
        lunar_year = solar_year - 1900 + 1
        zodiac_animals = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
        zodiac = zodiac_animals[(lunar_year - 1) % 12]
        
        # Hiển thị kết quả
        messagebox.showinfo("Kết quả", f"Năm Âm Lịch là: {lunar_year} ({zodiac})")

        # Hiển thị hình ảnh con giáp
        img_path = f"{zodiac}.png"  # Hình ảnh các con giáp như "Tý.png", "Sửu.png", ...
        img = Image.open(img_path)
        photo = ImageTk.PhotoImage(img)
        label_img.config(image=photo)
        label_img.image = photo  # Keep a reference to avoid garbage collection

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập năm hợp lệ!")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Chuyển đổi năm Dương lịch sang năm Âm lịch")

# Nhập năm Dương lịch
label_solar_year = tk.Label(window, text="Nhập năm Dương lịch:")
label_solar_year.pack()
entry_solar_year = tk.Entry(window)
entry_solar_year.pack()

# Tạo nút chuyển đổi
convert_button = tk.Button(window, text="Chuyển đổi", command=convert_to_lunar)
convert_button.pack()

# Hiển thị hình ảnh con giáp
label_img = tk.Label(window)
label_img.pack()

# Chạy giao diện người dùng
window.mainloop()
