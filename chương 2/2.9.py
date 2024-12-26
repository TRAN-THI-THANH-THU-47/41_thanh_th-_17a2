import json

# Đối tượng Python
person = {"name": "John", "age": 30, "city": "New York"}

# Chuyển thành JSON với thụt lề
json_str = json.dumps(person, indent=4)

# In chuỗi JSON với thụt lề
print(json_str)
