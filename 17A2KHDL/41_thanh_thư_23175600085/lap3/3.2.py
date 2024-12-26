# XỬ LÝ DỮ LIỆU NULL
import pandas as pd
# 1. Kiểm tra xem trong stocks1 có dữ liệu Null nào không
stocks1 = pd.read_csv('stocks1.csv')
print("\nKiểm tra dữ liệu Null:")
print(stocks1.isnull().sum())

# 2. Thay thế dữ liệu Null ở cột high bằng giá trị trung bình của cột high
if 'high' in stocks1.columns:
    mean_high = stocks1['high'].mean()
    stocks1['high'].fillna(mean_high, inplace=True)

# 3. Thay thế dữ liệu Null ở cột low bằng giá trị trung bình của cột low
if 'low' in stocks1.columns:
    mean_low = stocks1['low'].mean()
    stocks1['low'].fillna(mean_low, inplace=True)

# 4. Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Null
print("\nThông tin tổng quan sau khi xử lý dữ liệu Null:")
print(stocks1.info())