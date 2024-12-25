class Date:
    def __init__(self, day=1, month=1, year=2000):
        """Khởi tạo ngày, tháng, năm với giá trị mặc định là 1/1/2000."""
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        """Hiển thị thông tin ngày, tháng, năm."""
        print(f"Ngày: {self.day}/{self.month}/{self.year}")

    def next_day(self):
        """Tính ngày tiếp theo."""
        self.day += 1
        if (self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or 
            self.month == 8 or self.month == 10 or self.month == 12) and self.day > 31:
            self.day = 1
            self.month += 1
        elif (self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11) and self.day > 30:
            self.day = 1
            self.month += 1
        elif self.month == 2 and self.day > 28:
            self.day = 1
            self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1
