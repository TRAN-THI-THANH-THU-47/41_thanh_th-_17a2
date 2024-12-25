import threading

def print_even_numbers():
    for i in range(30, 51):
        if i % 2 == 0:
            print(f"Even: {i}")

def print_odd_numbers():
    for i in range(30, 51):
        if i % 2 != 0:
            print(f"Odd: {i}")

# Tạo hai luồng cho các số chẵn và lẻ
even_thread = threading.Thread(target=print_even_numbers)
odd_thread = threading.Thread(target=print_odd_numbers)

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()
