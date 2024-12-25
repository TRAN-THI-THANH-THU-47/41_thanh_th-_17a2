import tkinter as tk

# Tạo cửa sổ chính
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Nhãn với phông chữ")

# Tạo nhãn với kiểu phông chữ
label = tk.Label(window, text="Nhãn với phông chữ đặc biệt", font=("Helvetica", 16, "bold"))
label.pack()

# Chạy giao diện người dùng
window.mainloop()
