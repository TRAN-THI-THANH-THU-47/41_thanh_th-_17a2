import tkinter as tk
from tkinter import messagebox

def calculate_taxi_fare():
    try:
        car_type = var_car_type.get()
        distance = float(entry_distance.get())
        wait_time = int(entry_wait_time.get())

        if car_type == "4 chỗ":
            base_fare = 12000
            km_rate = 15300 if distance <= 30 else 12100
        else:
            base_fare = 12000
            km_rate = 16100 if distance <= 30 else 13800

        fare = base_fare + (distance - 0.8) * km_rate if distance > 0.8 else base_fare
        wait_fare = 0 if wait_time <= 5 else (wait_time - 5) * 750
        total_fare = fare + wait_fare

        messagebox.showinfo("Kết quả", f"Tiền cước taxi là: {total_fare} đồng")
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập giá trị hợp lệ!")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Tính cước taxi")

# Chọn loại xe
var_car_type = tk.StringVar(value="4 chỗ")
label_car_type = tk.Label(window, text="Chọn loại xe:")
label_car_type.pack()

radio_4_seat = tk.Radiobutton(window, text="4 chỗ", variable=var_car_type, value="4 chỗ")
radio_4_seat.pack()

radio_7_seat = tk.Radiobutton(window, text="7 chỗ", variable=var_car_type, value="7 chỗ")
radio_7_seat.pack()

# Nhập khoảng cách và thời gian chờ
label_distance = tk.Label(window, text="Nhập khoảng cách (km):")
label_distance.pack()
entry_distance = tk.Entry(window)
entry_distance.pack()

label_wait_time = tk.Label(window, text="Nhập thời gian chờ (phút):")
label_wait_time.pack()
entry_wait_time = tk.Entry(window)
entry_wait_time.pack()

# Tạo nút tính cước
calculate_button = tk.Button(window, text="Tính cước", command=calculate_taxi_fare)
calculate_button.pack()

# Chạy giao diện người dùng
window.mainloop()
