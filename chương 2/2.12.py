import requests

# Lấy dữ liệu từ API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()

# Hiển thị tổng số bài post và danh sách các bài post
print(f"Tổng số bài post: {len(posts)}")
for post in posts:
    print(f"UserID: {post['userId']}, ID: {post['id']}, Title: {post['title']}, Body: {post['body']}\n")
