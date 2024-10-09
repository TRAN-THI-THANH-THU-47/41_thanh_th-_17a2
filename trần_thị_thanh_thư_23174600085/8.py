class Date:
    def __init__(self, day=1, month=1, year=2023):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    def next(self):
        days_in_month = [31, 28 + (1 if self.is_leap_year() else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.day < days_in_month[self.month - 1]:
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

class Employee:
    def __init__(self, name, birth_date, join_date):
        self.name = name
        self.birth_date = birth_date  # Đối tượng Date cho ngày sinh
        self.join_date = join_date     # Đối tượng Date cho ngày vào công ty

    def display_info(self):
        print(f"Họ tên: {self.name}")
        print("Ngày sinh:", end=' ')
        self.birth_date.display()
        print("Ngày vào công ty:", end=' ')
        self.join_date.display()

# Chương trình thử nghiệm
# Nhập thông tin nhân viên
name = input("Nhập họ tên nhân viên: ")
day_birth = int(input("Nhập ngày sinh: "))
month_birth = int(input("Nhập tháng sinh: "))
year_birth = int(input("Nhập năm sinh: "))
day_join = int(input("Nhập ngày vào công ty: "))
month_join = int(input("Nhập tháng vào công ty: "))
year_join = int(input("Nhập năm vào công ty: "))

# Tạo đối tượng Date cho ngày sinh và ngày vào công ty
birth_date = Date(day_birth, month_birth, year_birth)
join_date = Date(day_join, month_join, year_join)

# Tạo đối tượng Employee
employee = Employee(name, birth_date, join_date)

# Hiển thị thông tin nhân viên
employee.display_info()
