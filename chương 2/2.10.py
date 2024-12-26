import json

# Dữ liệu JSON giả lập
data = '''
{
    "company": "Công ty TNHH Đất Việt",
    "address": "abc Giải Phóng - Hà Nội",
    "departments": [
        {"name": "Đơn vị A1", "staff_count": 50},
        {"name": "Đơn vị A2", "staff_count": 30},
        {"name": "Đơn vị A3", "staff_count": 20},
        {"name": "Đơn vị A4", "staff_count": 10}
    ]
}
'''

# Chuyển đổi JSON thành đối tượng Python
company_data = json.loads(data)

# Thống kê nhân viên
total_staff = sum(department["staff_count"] for department in company_data["departments"])

# In kết quả thống kê
print(f"Tên công ty: {company_data['company']}")
print(f"Địa chỉ: {company_data['address']}")
print(f"Tổng số nhân viên: {total_staff}\n")

for department in company_data["departments"]:
    ratio = (department["staff_count"] / total_staff) * 100
    print(f"Tên đơn vị: {department['name']}")
    print(f"Số nhân viên: {department['staff_count']}")
    print(f"Tỷ lệ: {ratio:.2f}%\n")
