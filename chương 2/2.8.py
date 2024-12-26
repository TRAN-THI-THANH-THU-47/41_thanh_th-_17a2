import json

# Đối tượng Python
python_dict = {"name": "John", "age": 30, "city": "New York"}

# Chuyển đổi đối tượng Python thành chuỗi JSON
json_data = json.dumps(python_dict)

# In chuỗi JSON
print(json_data)
