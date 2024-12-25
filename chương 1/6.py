class Stack:
    def __init__(self, size):
        """Khởi tạo ngăn xếp với kích thước tối đa."""
        self.size = size  # Kích thước tối đa của ngăn xếp
        self.stack = []  # Khởi tạo một danh sách rỗng để chứa các phần tử

    def push(self, value):
        """Đưa một phần tử vào ngăn xếp."""
        if len(self.stack) < self.size:
            self.stack.append(value)  # Thêm phần tử vào cuối danh sách
        else:
            print("Ngăn xếp đã đầy!")  # Nếu ngăn xếp đầy, thông báo lỗi

    def pop(self):
        """Lấy một phần tử từ ngăn xếp."""
        if self.is_empty():
            print("Ngăn xếp trống!")  # Nếu ngăn xếp trống, thông báo lỗi
        else:
            return self.stack.pop()  # Loại bỏ và trả về phần tử cuối cùng trong danh sách

    def is_empty(self):
        """Kiểm tra ngăn xếp có trống hay không."""
        return len(self.stack) == 0  # Nếu danh sách rỗng, trả về True

    def is_full(self):
        """Kiểm tra ngăn xếp có đầy hay không."""
        return len(self.stack) == self.size  # Nếu số phần tử bằng kích thước tối đa, trả về True

    def count(self):
        """Trả về số lượng phần tử hiện có trong ngăn xếp."""
        return len(self.stack)  # Đếm số phần tử trong danh sách

    def print_stack(self):
        """In ra nội dung của ngăn xếp."""
        print("Nội dung ngăn xếp:", self.stack)  # In tất cả các phần tử trong ngăn xếp

# Chương trình chính
stack = Stack(5)  # Khởi tạo ngăn xếp với kích thước tối đa là 5
stack.push(10)  # Đưa phần tử 10 vào ngăn xếp
stack.push(20)  # Đưa phần tử 20 vào ngăn xếp
stack.push(30)  # Đưa phần tử 30 vào ngăn xếp

print("Số phần tử hiện tại trong ngăn xếp:", stack.count())  # In số phần tử trong ngăn xếp
stack.print_stack()  # In nội dung ngăn xếp

stack.pop()  # Lấy phần tử khỏi ngăn xếp
print("Số phần tử hiện tại trong ngăn xếp sau khi pop:", stack.count())  # In số phần tử sau khi lấy ra
stack.print_stack()  # In lại nội dung ngăn xếp
