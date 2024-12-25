import tkinter as tk
from tkinter import messagebox

def show_exercise(exercise_name):
    messagebox.showinfo("Thông báo", f"Bài tập: {exercise_name}")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Hệ thống bài tập Python")

# Tạo thanh menu
menu_bar = tk.Menu(window)

# Tạo menu cho các chương
chapter_menu = tk.Menu(menu_bar, tearoff=0)
for chapter in range(1, 8):  # Chương từ 1 đến 7
    chapter_name = f"Chương {chapter}"
    chapter_menu.add_command(label=chapter_name, command=lambda chapter=chapter: show_exercise(f"{chapter}.1"))

# Thêm các mục vào menu
menu_bar.add_cascade(label="Chương", menu=chapter_menu)

# Đặt menu cho cửa sổ
window.config(menu=menu_bar)

# Chạy giao diện người dùng
window.mainloop()
