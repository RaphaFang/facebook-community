import requests

# 使用您獲取的訪問權杖和社團ID
access_token = 'YOUR_ACCESS_TOKEN'
group_id = 'YOUR_GROUP_ID'

# 設置請求URL
url = f'https://graph.facebook.com/v13.0/{group_id}/feed'
params = {
    'access_token': access_token,
    'fields': 'message,created_time,from,attachments{media}'
}

# 發送GET請求
response = requests.get(url, params=params)
data = response.json()

# 輸出文章內容和照片連結
for post in data['data']:
    print(f"Post from {post['from']['name']} at {post['created_time']}:")
    if 'message' in post:
        print(post['message'])
    if 'attachments' in post:
        for attachment in post['attachments']['data']:
            if 'media' in attachment:
                print(f"Photo: {attachment['media']['image']['src']}")
    print()
