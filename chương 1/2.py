class TS:
    def __init__(self):
        self.name = ""
        self.math_score = 0
        self.physics_score = 0
        self.chemistry_score = 0
    
    def input_data(self):
        self.name = input("Nhập họ tên thí sinh: ")
        self.math_score = float(input("Nhập điểm môn Toán: "))
        self.physics_score = float(input("Nhập điểm môn Lý: "))
        self.chemistry_score = float(input("Nhập điểm môn Hoá: "))
    
    def total_score(self):
        return self.math_score + self.physics_score + self.chemistry_score
    
    def print_info(self):
        print(f"Họ tên: {self.name}")
        print(f"Điểm Toán: {self.math_score}, Lý: {self.physics_score}, Hoá: {self.chemistry_score}")
        print(f"Tổng điểm: {self.total_score()}")

# Chương trình chính
students = []
n = int(input("Nhập số lượng thí sinh: "))
for _ in range(n):
    student = TS()
    student.input_data()
    students.append(student)

# Lọc thí sinh trúng tuyển và sắp xếp
accepted_students = [student for student in students if student.total_score() >= 20]
accepted_students.sort(key=lambda x: x.total_score(), reverse=True)

print("Danh sách thí sinh trúng tuyển:")
for student in accepted_students:
    student.print_info()
