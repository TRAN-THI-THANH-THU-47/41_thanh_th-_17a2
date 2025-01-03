import sqlite3

def connect():
    """Kết nối đến CSDL và tạo bảng nếu chưa tồn tại."""
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product (
            Id INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Price REAL NOT NULL,
            Amount INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def display_products():
    """Hiển thị danh sách sản phẩm."""
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    if products:
        print("\nDanh sách sản phẩm:")
        for product in products:
            print(f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")
    else:
        print("\nKhông có sản phẩm nào trong cơ sở dữ liệu.")
    conn.close()

def add_product():
    """Thêm sản phẩm mới."""
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    amount = int(input("Nhập số lượng sản phẩm: "))
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    conn.close()
    print("Sản phẩm đã được thêm thành công!")

def search_product():
    """Tìm kiếm sản phẩm theo tên."""
    name = input("Nhập tên sản phẩm cần tìm: ")
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", (f"%{name}%",))
    products = cursor.fetchall()
    if products:
        print("\nKết quả tìm kiếm:")
        for product in products:
            print(f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")
    else:
        print("\nKhông tìm thấy sản phẩm nào.")
    conn.close()

def update_product():
    """Cập nhật thông tin sản phẩm."""
    product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
    price = float(input("Nhập giá mới: "))
    amount = int(input("Nhập số lượng mới: "))
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (price, amount, product_id))
    conn.commit()
    conn.close()
    print("Thông tin sản phẩm đã được cập nhật!")

def delete_product():
    """Xóa sản phẩm theo ID."""
    product_id = int(input("Nhập ID sản phẩm cần xóa: "))
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))
    conn.commit()
    conn.close()
    print("Sản phẩm đã được xóa!")

def main():
    """Hàm chính để chạy chương trình."""
    connect()
    while True:
        print("\n--- Quản Lý Sản Phẩm ---")
        print("1. Hiển Thị Danh Sách Sản Phẩm")
        print("2. Thêm Sản Phẩm Mới")
        print("3. Tìm Kiếm Sản Phẩm Theo Tên")
        print("4. Cập Nhật Thông Tin Sản Phẩm")
        print("5. Xóa Sản Phẩm")
        print("6. Thoát")
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == "1":
            display_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại!")

if __name__ == "__main__":
    main()
