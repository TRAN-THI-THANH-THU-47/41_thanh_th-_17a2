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

# 1. Tạo Pivot Table với date làm chỉ mục, symbol làm cột, và giá trị trung bình của close
pivot_table = stocks.pivot_table(values='close', index='date', columns='symbol', aggfunc='mean')

# 2. Thêm cột tính tổng volume giao dịch cho mỗi mã chứng khoán (symbol)
total_volume = stocks.groupby('symbol')['volume'].sum()
pivot_table.loc['Total Volume'] = total_volume

# 3. Sắp xếp Pivot Table dựa trên tổng volume giao dịch, từ cao xuống thấp
sorted_symbols = total_volume.sort_values(ascending=False)
sorted_pivot_table = pivot_table[sorted_symbols.index]

# 4. Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất
result = sorted_pivot_table.loc[['Total Volume']]
print(result)