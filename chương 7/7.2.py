import tkinter as tk

# Tạo cửa sổ chính
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Cửa sổ có nhãn")

# Tạo nhãn và hiển thị trên cửa sổ
label = tk.Label(window, text="Đây là một nhãn!")
label.pack()

# Chạy giao diện người dùng
window.mainloop()
