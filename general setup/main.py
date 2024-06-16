import requests

# 使用您獲取的訪問權杖和社團ID
access_token = 'EAA2YE5RVrNQBO118YJvH6fDj30T9RZAbXSkyj0RXzps24ZCMyRtBKJZBNV3FSGH4iqPZBZAQC0ZAjXESIKKkaAnUB3eeaJb4UaxXC1XsgXn2peKbdTkd1XyQLp7OWvp5fu8oqeT3eZC42TeTP0EOnBS5giDMpTJsykabMIm7fRYUhgoervbrFmCc1xORZBSzAdYSPnDSERZBzpo4UEFhvbalb6SocCfATsSvlGTTCzNL6u9gYjMaAHjwH'
group_id = 'Psf6e1b1xfnz33'

# 设置请求URL
url = f'https://graph.facebook.com/v20.0/{group_id}/feed'
params = {
    'access_token': access_token,
    'fields': 'message,created_time,from,comments{message,from,created_time},attachments{media}'
}

# 发送GET请求
response = requests.get(url, params=params)
data = response.json()

print(data)

# 输出文章内容和照片链接
# for post in data['data']:
#     print(f"Post from {post['from']['name']} at {post['created_time']}:")
#     if 'message' in post:
#         print(post['message'])
#     if 'attachments' in post:
#         for attachment in post['attachments']['data']:
#             if 'media' in attachment:
#                 print(f"Photo: {attachment['media']['image']['src']}")
#     if 'comments' in post:
#         print("Comments:")
#         for comment in post['comments']['data']:
#             print(f"  Comment from {comment['from']['name']} at {comment['created_time']}: {comment['message']}")
#     print()
