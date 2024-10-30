import numpy as np

# Khởi tạo các array arr_a và arr_b
arr_a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
arr_b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

# Yêu cầu 1: Tạo array arr_c chỉ lấy các phần tử xuất hiện ở cả arr_a và arr_b (không trùng lặp)
arr_c = np.intersect1d(arr_a, arr_b)
print("Array arr_c (elements in both arr_a and arr_b):", arr_c)

# Yêu cầu 2: Tạo array arr_d chứa các phần tử chỉ xuất hiện ở arr_a
arr_d = np.setdiff1d(arr_a, arr_b)
print("Array arr_d (elements unique to arr_a):", arr_d)
