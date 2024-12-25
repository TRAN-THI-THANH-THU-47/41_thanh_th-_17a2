import threading

def print_even_numbers(limit):
    for i in range(2, limit + 1, 2):
        print(i)

def print_odd_numbers(limit):
    for i in range(1, limit + 1, 2):
        print(i)

# Tạo hai luồng để in số chẵn và lẻ
limit = 20
even_thread = threading.Thread(target=print_even_numbers, args=(limit,))
odd_thread = threading.Thread(target=print_odd_numbers, args=(limit,))

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()
