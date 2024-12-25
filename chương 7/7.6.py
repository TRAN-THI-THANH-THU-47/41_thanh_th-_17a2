import tkinter as tk

def reverse_word():
    word = entry_word.get()
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    result_label.config(text=f"Word reversed: {reversed_word}")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Đảo ngược từ")

# Nhập từ cần đảo ngược
label_word = tk.Label(window, text="Nhập từ:")
label_word.pack()
entry_word = tk.Entry(window)
entry_word.pack()

# Tạo nút đảo ngược
reverse_button = tk.Button(window, text="Đảo ngược", command=reverse_word)
reverse_button.pack()

# Hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy giao diện người dùng
window.mainloop()
