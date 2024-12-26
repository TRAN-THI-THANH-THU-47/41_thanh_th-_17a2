import pandas as pd

# Dữ liệu cho DataFrame stocks
stocks_data = {
    "date": ["01-03-19", "04-03-19", "05-03-19", "06-03-19", "07-03-19"],
    "open": [684.770, 693.940, 695.664, 696.502, 689.460],
    "high": [692.52840, 702.39200, 584.92000, 449.53395, 691.47800],
    "low": [680.4460, 685.1260, 575.0500, 443.7725, 673.8600],
    "close": [688.952, 694.510, 695.558, 690.016, 677.494],
    "volume": [12000, 14000, 13000, 15000, 16000]
}
stocks = pd.DataFrame(stocks_data)

# Thêm cột symbol để khớp với tên công ty
stocks['symbol'] = ['AMZN', 'AMZN', 'GOOG', 'AAPL', 'FB']

# 1. Tạo MultiIndex cho DataFrame stocks bằng cột date và symbol
stocks.set_index(['date', 'symbol'], inplace=True)

# 2. Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume
grouped_stocks = stocks.groupby(['date', 'symbol']).mean()

# 3. Sắp xếp dữ liệu theo ngày và mã chứng khoán
sorted_stocks = grouped_stocks.sort_index()

# 4. Hiển thị kết quả cho 5 ngày đầu tiên
print(sorted_stocks.head())