import pandas as pd

# 1. Đọc file stocks2.csv vào DataFrame stocks2
stocks2 = pd.read_csv('stocks2.csv')

# 2. Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
# Giả sử stocks1 đã được đọc trước đó
stocks1 = pd.read_csv('stocks1.csv')  
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# 3. Tính giá trung bình (open, high, low, close) cho mỗi ngày
stocks_avg = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()

# 4. Hiển thị 5 dòng đầu tiên của kết quả
print(stocks_avg.head())
