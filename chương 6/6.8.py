import threading

def sum_part_of_list(numbers, result, index):
    result[index] = sum(numbers)

numbers = [177, 4, 6, 2, 1, 7, 7, 7, 4, 7, 8, 7, 2, 3, 4, 5, 6, 8, 2, 5, 8, 8, 5, 4, 7, 3, 4, 3, 8, 8, 9, 6, 5, 4, 3, 9]
n_threads = 3
threads = []
result = [0] * n_threads

# Chia list thành các phần nhỏ
sub_lists = [numbers[i::n_threads] for i in range(n_threads)]

for i in range(n_threads):
    thread = threading.Thread(target=sum_part_of_list, args=(sub_lists[i], result, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Tính tổng tất cả các phần tử
total_sum = sum(result)
print(f"Total sum: {total_sum}")
