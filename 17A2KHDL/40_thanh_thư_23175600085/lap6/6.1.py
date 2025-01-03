import tkinter as tk
from tkinter import messagebox
import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
def connect_db():
    return sqlite3.connect('products.db')

# Tạo bảng sản phẩm nếu chưa tồn tại
def create_table():
    conn = connect_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

# Thêm sản phẩm vào cơ sở dữ liệu
def add_product(name, price):
    if not name or not price:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return
    conn = connect_db()
    conn.execute('''
        INSERT INTO products (name, price) 
        VALUES (?, ?)
    ''', (name, price))
    conn.commit()
    conn.close()
    display_products()

# Hiển thị danh sách sản phẩm
def display_products():
    conn = connect_db()
    listbox.delete(0, tk.END)
    for product in conn.execute('SELECT * FROM products'):
        listbox.insert(tk.END, f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}")
    conn.close()

# Xóa sản phẩm theo ID
def delete_product():
    try:
        product_id = int(entry_id.get())
        conn = connect_db()
        conn.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()
        conn.close()
        display_products()
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập ID hợp lệ!")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Cập nhật thông tin sản phẩm
def update_product():
    try:
        product_id = int(entry_id.get())
        new_name = entry_name.get()
        new_price = float(entry_price.get())
        if not new_name or new_price <= 0:
            messagebox.showerror("Lỗi", "Vui lòng nhập thông tin hợp lệ!")
            return
        conn = connect_db()
        conn.execute('''
            UPDATE products SET name = ?, price = ? WHERE id = ?
        ''', (new_name, new_price, product_id))
        conn.commit()
        conn.close()
        display_products()
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập ID và giá trị hợp lệ!")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Tạo giao diện người dùng (GUI)
root = tk.Tk()
root.title("Quản lý sản phẩm")

# Nhập thông tin sản phẩm
label_id = tk.Label(root, text="ID sản phẩm:")
label_id.pack()

entry_id = tk.Entry(root)
entry_id.pack()

label_name = tk.Label(root, text="Tên sản phẩm:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_price = tk.Label(root, text="Giá sản phẩm:")
label_price.pack()

entry_price = tk.Entry(root)
entry_price.pack()

# Danh sách sản phẩm
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack()

# Nút chức năng
button_add = tk.Button(root, text="Thêm sản phẩm", command=lambda: add_product(entry_name.get(), entry_price.get()))
button_add.pack()

button_update = tk.Button(root, text="Cập nhật sản phẩm", command=update_product)
button_update.pack()

button_delete = tk.Button(root, text="Xóa sản phẩm", command=delete_product)
button_delete.pack()

# Hiển thị danh sách sản phẩm khi chạy
create_table()
display_products()

# Bắt đầu vòng lặp giao diện
root.mainloop()
