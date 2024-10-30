import numpy as np

# Yêu cầu 1: Tạo art_zeros có 10 phần tử 0, cập nhật phần tử ở vị trí thứ 5 là 1
art_zeros = np.zeros(10, dtype=int)
art_zeros[4] = 1  # Vị trí thứ 5 (index = 4) cập nhật thành 1
print("Array art_zeros:", art_zeros)

# Yêu cầu 2: Tạo arr_h có giá trị từ 10 đến 24, in danh sách theo thứ tự đảo ngược
arr_h = np.arange(10, 25)
print("Array arr_h (reversed):", arr_h[::-1])

# Yêu cầu 3: Tạo arr_1 từ arr_k với các phần tử khác 0
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_1 = arr_k[arr_k != 0]
print("Array arr_1 (non-zero elements of arr_k):", arr_1)

# Yêu cầu 4: Thêm 2 phần tử có giá trị 10 và 20 vào cuối arr_1
arr_1 = np.append(arr_1, [10, 20])
print("Array arr_1 after appending 10 and 20:", arr_1)

# Yêu cầu 5: Thêm phần tử có giá trị 100 vào vị trí có index = 5
arr_1 = np.insert(arr_1, 5, 100)
print("Array arr_1 after inserting 100 at index 5:", arr_1)

# Yêu cầu 6: Xóa các phần tử tại vị trí có index = 0, 1, 2
arr_1 = np.delete(arr_1, [0, 1, 2])
print("Array arr_1 after deleting elements at index 0, 1, 2:", arr_1)
