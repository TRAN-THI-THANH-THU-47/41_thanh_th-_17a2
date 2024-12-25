class Date:
    def __init__(self, day=1, month=1, year=2020):
        self.day = day
        self.month = month
        self.year = year
    
    def display(self):
        print(f"Ngày: {self.day}/{self.month}/{self.year}")
    
    def next_day(self):
        self.day += 1
        if self.day > 31:  # Đơn giản hóa, giả sử tháng nào cũng có 31 ngày
            self.day = 1
            self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1

# Chương trình chính
date = Date(31, 12, 2020)
date.display()
date.next_day()
date.display()
