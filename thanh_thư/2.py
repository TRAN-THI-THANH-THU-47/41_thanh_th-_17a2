import numpy as np

# Yêu cầu 1: Tạo numpy array arr có giá trị từ 0-9
arr = np.arange(10)
print("Array arr:", arr)
print("Data type of arr:", arr.dtype)
print("Shape of arr:", arr.shape)

# Yêu cầu 2: Tạo arr_odd và arr_even từ arr
arr_odd = arr[arr % 2 != 0]  # Các phần tử lẻ
arr_even = arr[arr % 2 == 0]  # Các phần tử chẵn

print("Array arr_odd (odd elements):", arr_odd)
print("Array arr_even (even elements):", arr_even)

# Yêu cầu 3: Tạo arr_update_1 từ arr với các phần tử chẵn giữ nguyên, các phần tử lẻ thay bằng 100
arr_update_1 = np.where(arr % 2 == 0, arr, 100)
print("Array arr_update_1 (even elements remain, odd replaced by 100):", arr_update_1)
