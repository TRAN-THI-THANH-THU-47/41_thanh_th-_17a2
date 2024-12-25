import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"Chỉ số BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            conclusion = "Cân nặng thấp"
        elif 18.5 <= bmi < 24.9:
            conclusion = "Cân nặng bình thường"
        elif 25 <= bmi < 29.9:
            conclusion = "Thừa cân"
        else:
            conclusion = "Béo phì"
        
        conclusion_label.config(text=f"Kết luận: {conclusion}")
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập giá trị hợp lệ!")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Tính chỉ số BMI")

# Nhập cân nặng và chiều cao
label_weight = tk.Label(window, text="Nhập cân nặng (kg):")
label_weight.pack()
entry_weight = tk.Entry(window)
entry_weight.pack()

label_height = tk.Label(window, text="Nhập chiều cao (m):")
label_height.pack()
entry_height = tk.Entry(window)
entry_height.pack()

# Tạo nút tính BMI
calculate_button = tk.Button(window, text="Tính BMI", command=calculate_bmi)
calculate_button.pack()

# Hiển thị kết quả BMI và kết luận
result_label = tk.Label(window, text="")
result_label.pack()

conclusion_label = tk.Label(window, text="")
conclusion_label.pack()

# Chạy giao diện người dùng
window.mainloop()
