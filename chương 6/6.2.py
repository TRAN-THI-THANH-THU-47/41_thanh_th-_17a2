import threading
import requests

def download_file(url):
    response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {file_name}")

urls = ['http://example.com/file1', 'http://example.com/file2']

threads = []
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
