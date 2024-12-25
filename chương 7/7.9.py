import tkinter as tk
import math

def calculate_gcd():
    try:
        m = int(entry_m.get())
        n = int(entry_n.get())
        gcd = math.gcd(m, n)
        result_label.config(text=f"GCD({m}, {n}) = {gcd}")
    except ValueError:
        result_label.config(text="Vui lòng nhập số nguyên hợp lệ!")

def calculate_lcm():
    try:
        m = int(entry_m.get())
        n = int(entry_n.get())
        lcm = abs(m * n) // math.gcd(m, n)
        result_label.config(text=f"LCM({m}, {n}) = {lcm}")
    except ValueError:
        result_label.config(text="Vui lòng nhập số nguyên hợp lệ!")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Tính GCD và LCM")

# Nhập m và n
label_m = tk.Label(window, text="Nhập giá trị m:")
label_m.pack()
entry_m = tk.Entry(window)
entry_m.pack()

label_n = tk.Label(window, text="Nhập giá trị n:")
label_n.pack()
entry_n = tk.Entry(window)
entry_n.pack()

# Tạo nút tính GCD và LCM
gcd_button = tk.Button(window, text="Tính GCD", command=calculate_gcd)
gcd_button.pack()

lcm_button = tk.Button(window, text="Tính LCM", command=calculate_lcm)
lcm_button.pack()

# Hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy giao diện người dùng
window.mainloop()
