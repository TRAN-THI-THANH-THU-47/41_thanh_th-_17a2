import threading

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    print(f"Factorial of {n} is {result}")

# Tạo luồng để tính giai thừa của số
n = 5
factorial_thread = threading.Thread(target=factorial, args=(n,))
factorial_thread.start()
factorial_thread.join()
