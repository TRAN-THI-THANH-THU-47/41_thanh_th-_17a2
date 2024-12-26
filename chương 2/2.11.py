import json
from datetime import datetime

# Dữ liệu giao dịch giả lập
transactions = [
    {"date": "2024-12-25", "type": "Tiền", "amount": 100},
    {"date": "2024-12-26", "type": "Vàng", "amount": 2}
]

# Hỏi người dùng có muốn lưu giao dịch không
save_data = input("Bạn có muốn ghi vào tập tin không? (1: Có, 0: Không): ")

if save_data == '1':
    # Lấy thời gian hiện tại
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    # Lưu vào tập tin JSON
    filename = f"{current_time}.json"
    with open(filename, 'w') as file:
        json.dump(transactions, file, indent=4)
    print(f"Dữ liệu đã được lưu vào {filename}")
else:
    print("Không lưu dữ liệu.")
