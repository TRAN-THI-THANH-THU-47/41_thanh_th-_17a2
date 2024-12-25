import threading
import time

def task(name):
    print(f"Starting {name}")
    time.sleep(1)
    print(f"{name}: Web {time.strftime('%b %d %H:%M:%S %Y')}")
    print(f"Exiting {name}")

# Tạo và khởi chạy các luồng
sites = ['Google', 'Yahoo', 'Facebook']
threads = []

for site in sites:
    thread = threading.Thread(target=task, args=(site,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Exiting Main Thread")
