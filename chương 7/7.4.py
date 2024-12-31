import tkinter as tk

def submit():
    name = entry_name.get()
    student_id = entry_id.get()
    password = entry_password.get()
    print(f"Name: {name}, ID: {student_id}, Password: {password}")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Thông tin sinh viên")

# Tạo các nhãn và hộp văn bản
label_name = tk.Label(window, text="Tên sinh viên:")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

label_id = tk.Label(window, text="ID sinh viên:")
label_id.pack()
entry_id = tk.Entry(window)
entry_id.pack()

label_password = tk.Label(window, text="Mật khẩu:")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Tạo nút gửi
submit_button = tk.Button(window, text="Gửi", command=submit)
submit_button.pack()

# Chạy giao diện người dùng
window.mainloop()
