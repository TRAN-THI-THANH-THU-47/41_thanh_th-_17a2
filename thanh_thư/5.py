import numpy as np

# Đọc dữ liệu từ tập tin heights_1.txt và weights_1.txt
# Bạn cần đảm bảo rằng file heights_1.txt và weights_1.txt có sẵn trong thư mục hiện tại
with open('heights_1.txt', 'r') as file:
    height = [float(line.strip()) for line in file]

with open('weights_1.txt', 'r') as file:
    weight = [float(line.strip()) for line in file]

# Yêu cầu 1: Tạo numpy array arr_height từ list height
arr_height = np.array(height)
print("Array arr_height:", arr_height)

# Yêu cầu 2: Tạo numpy array arr_weight từ list weight
arr_weight = np.array(weight)
print("Array arr_weight:", arr_weight)
