import tkinter as tk

def find_divisors():
    try:
        n = int(entry_number.get())
        divisors = [str(i) for i in range(1, n+1) if n % i == 0]
        result_label.config(text=f"Các ước của {n}: {', '.join(divisors)}")
    except ValueError:
        result_label.config(text="Vui lòng nhập số nguyên!")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Liệt kê các ước")

# Nhập số nguyên N
label_number = tk.Label(window, text="Nhập số nguyên N:")
label_number.pack()
entry_number = tk.Entry(window)
entry_number.pack()

# Tạo nút liệt kê ước
find_button = tk.Button(window, text="Liệt kê ước", command=find_divisors)
find_button.pack()

# Hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy giao diện người dùng
window.mainloop()
