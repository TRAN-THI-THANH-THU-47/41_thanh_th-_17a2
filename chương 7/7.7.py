import tkinter as tk

def calculate_sum():
    try:
        n = int(entry_number.get())
        total_sum = sum(range(1, n+1))
        result_label.config(text=f"Tổng: {total_sum}")
    except ValueError:
        result_label.config(text="Vui lòng nhập số nguyên!")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Tính tổng từ 1 đến N")

# Nhập số nguyên N
label_number = tk.Label(window, text="Nhập số nguyên N:")
label_number.pack()
entry_number = tk.Entry(window)
entry_number.pack()

# Tạo nút tính tổng
calculate_button = tk.Button(window, text="Tính tổng", command=calculate_sum)
calculate_button.pack()

# Hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy giao diện người dùng
window.mainloop()
