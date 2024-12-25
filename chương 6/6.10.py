import threading

def find_max(numbers, result, index):
    result[index] = max(numbers)

numbers = [34, 5, 7, 29, 99, 2, 8, 50, 30, 88]
n_threads = 3
threads = []
result = [0] * n_threads

# Chia list thành các phần nhỏ
sub_lists = [numbers[i::n_threads] for i in range(n_threads)]

for i in range(n_threads):
    thread = threading.Thread(target=find_max, args=(sub_lists[i], result, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Tìm giá trị lớn nhất
max_value = max(result)
print(f"Max value: {max_value}")
