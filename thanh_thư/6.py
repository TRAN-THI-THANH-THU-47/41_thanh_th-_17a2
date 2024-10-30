import numpy as np

# Yêu cầu 1: Tạo array arr có kích thước 3x3 với các giá trị True
arr = np.full((3, 3), True)
print("Array arr (3x3 with True values):")
print(arr)

# Yêu cầu 2: Tạo array 2 chiều từ arr_ID và đổi chỗ cột 1 với cột 3
arr_ID = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
arr_2D = arr_ID.reshape(3, 3)  # Tạo array 2 chiều 3x3
print("\nArray arr_2D before swapping columns:")
print(arr_2D)

# Đổi chỗ cột 1 với cột 3
arr_2D[:, [1, 2]] = arr_2D[:, [2, 1]]
print("\nArray arr_2D after swapping columns 1 and 3:")
print(arr_2D)

# Yêu cầu 3: Chuyển dòng 1 sang dòng 2 và ngược lại
arr_2D[[0, 1]] = arr_2D[[1, 0]]
print("\nArray arr_2D after swapping rows 1 and 2:")
print(arr_2D)

# Yêu cầu 4: Đảo ngược các dòng của arr_2D
arr_2D = arr_2D[::-1]
print("\nArray arr_2D after reversing rows:")
print(arr_2D)

# Yêu cầu 5: Đảo ngược các cột của arr_2D
arr_2D = arr_2D[:, ::-1]
print("\nArray arr_2D after reversing columns:")
print(arr_2D)

# Yêu cầu 6: Kiểm tra giá trị rỗng trong arr_2D_null
arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
has_nan = np.isnan(arr_2D_null).any()
print("\nArray arr_2D_null has NaN values:", has_nan)

# Yêu cầu 7: Thay thế giá trị NaN bằng 0
arr_2D_null = np.nan_to_num(arr_2D_null, nan=0)
print("\nArray arr_2D_null after replacing NaN with 0:")
print(arr_2D_null)
