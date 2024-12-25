import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite (tạo mới nếu chưa có)
conn = sqlite3.connect("product.db")
cursor = conn.cursor()

# Tạo bảng sản phẩm
cursor.execute("""
CREATE TABLE IF NOT EXISTS product (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
);
""")

# Hàm hiển thị tất cả sản phẩm
def display_products():
    cursor.execute("SELECT * FROM product;")
    products = cursor.fetchall()
    for product in products:
        print(product)

# Hàm thêm sản phẩm
def add_product(name, price, amount):
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?);", (name, price, amount))
    conn.commit()
    print("Sản phẩm đã được thêm.")

# Hàm tìm kiếm sản phẩm theo tên
def search_product_by_name(name):
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?;", ('%' + name + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)

# Hàm cập nhật giá và số lượng của sản phẩm theo id
def update_product(id, price, amount):
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?;", (price, amount, id))
    conn.commit()
    print("Thông tin sản phẩm đã được cập nhật.")

# Hàm xóa sản phẩm theo id
def delete_product(id):
    cursor.execute("DELETE FROM product WHERE Id = ?;", (id,))
    conn.commit()
    print("Sản phẩm đã bị xóa.")

# Ví dụ sử dụng:
display_products()  # Hiển thị danh sách sản phẩm
add_product("Laptop", 1500.0, 10)  # Thêm sản phẩm
search_product_by_name("Laptop")  # Tìm kiếm sản phẩm theo tên
update_product(1, 1600.0, 8)  # Cập nhật giá và số lượng
delete_product(1)  # Xóa sản phẩm

# Đóng kết nối
conn.close()
