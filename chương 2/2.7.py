import json

# JSON string
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Chuyển đổi JSON thành đối tượng Python
python_obj = json.loads(json_data)

# In đối tượng Python
print(python_obj)
