import requests

# Lấy dữ liệu từ API
url = "https://jsonplaceholder.typicode.com/comments?postId=1"
response = requests.get(url)
comments = response.json()

# Hiển thị danh sách các bài post nổi bật (giới hạn 3 bài)
print("Danh sách các bài post nổi bật:")
for i, comment in enumerate(comments[:3]):
    print(f"Email: {comment['email']}, Name: {comment['name']}, Body: {comment['body']}\n")