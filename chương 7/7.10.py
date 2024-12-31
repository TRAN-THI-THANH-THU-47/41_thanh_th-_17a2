import tkinter as tk
from tkinter import messagebox

def check_age():
    name = entry_name.get()
    try:
        age = int(entry_age.get())
        if age >= 18:
            messagebox.showinfo("Thông báo", f"Xin chào {name}. Bạn đã trưởng thành!")
        else:
            messagebox.showinfo("Thông báo", f"Xin chào {name}. Bạn còn nhỏ tuổi!")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập tuổi hợp lệ!")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Thông tin người dùng")

# Nhập tên và tuổi
label_name = tk.Label(window, text="Nhập tên của bạn:")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

label_age = tk.Label(window, text="Nhập tuổi của bạn:")
label_age.pack()
entry_age = tk.Entry(window)
entry_age.pack()

# Tạo nút kiểm tra tuổi
check_button = tk.Button(window,)
