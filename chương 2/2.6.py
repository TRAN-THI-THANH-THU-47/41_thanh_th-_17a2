import requests
import xml.etree.ElementTree as ET

# Tải RSS feed từ URL
url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
response = requests.get(url)

# Lưu dữ liệu XML vào file
with open("rss_feed.xml", "wb") as file:
    file.write(response.content)

# Phân tích cú pháp tệp XML
tree = ET.parse("rss_feed.xml")
root = tree.getroot()

# Lấy danh sách tin tức và lưu vào dictionary
news_list = []
for item in root.findall(".//item"):
    news_dict = {
        'title': item.find('title').text,
        'link': item.find('link').text,
        'description': item.find('description').text
    }
    news_list.append(news_dict)

# In ra danh sách tin tức
for news in news_list:
    print(news)
