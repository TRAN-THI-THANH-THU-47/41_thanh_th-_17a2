import pandas as pd

# Đọc file companies.csv vào DataFrame

companies = pd.read_csv('companies.csv')

# Tạo DataFrame stocks từ dữ liệu cung cấp
stocks_data = {
    "date": ["01-03-19", "04-03-19", "05-03-19", "06-03-19", "07-03-19"],
    "open": [684.770, 693.940, 695.664, 696.502, 689.460],
    "high": [692.52840, 702.39200, 584.92000, 449.53395, 691.47800],
    "low": [680.4460, 685.1260, 575.0500, 443.7725, 673.8600],
    "close": [688.952, 694.510, 695.558, 690.016, 677.494]
}
stocks = pd.DataFrame(stocks_data)

# Thêm cột symbol để khớp với tên công ty trong companies
stocks['symbol'] = ['AMZN', 'AMZN', 'GOOG', 'AAPL', 'FB']

# Kết hợp stocks và companies dựa trên cột 'symbol' và 'name'
merged_data = pd.merge(stocks, companies, left_on='symbol', right_on='name')

# Tính giá đóng cửa trung bình (close) cho mỗi công ty
average_close = merged_data.groupby('name')['close'].mean()

# Hiển thị kết quả cho 5 công ty đầu tiên
print(average_close.head())