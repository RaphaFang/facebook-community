import requests
from requests_oauthlib import OAuth2Session
import os 

app_id = os.getenv('YOUR_APP_ID')
app_secret = os.getenv('YOUR_APP_SECRET')
redirect_uri = 'https://localhost/'
scope = ['public_profile', 'user_posts', 'user_videos', 'user_photos']

# 前往url授權
oauth = OAuth2Session(app_id, redirect_uri=redirect_uri, scope=scope)
authorization_url, state = oauth.authorization_url('https://www.facebook.com/v20.0/dialog/oauth')
print('Please go to %s and authorize access.' % authorization_url)

# fetch 授權後返回的url，目的得到得到 token（理論上未來接一個api自動去作這件事）
response_url = input('Enter the full callback URL: ')
token = oauth.fetch_token('https://graph.facebook.com/v20.0/oauth/access_token',
                          authorization_response=response_url,
                          client_secret=app_secret)
print('Access Token:', token)

# 使用訪問權杖進行API請求
access_token = token['access_token']
url = 'https://graph.facebook.com/me'
params = {
    'access_token': access_token,
    'fields': 'id,name,posts,videos,photos'
}
response = requests.get(url, params=params)
data = response.json()


print(f"User ID: {data['id']}")
print(f"Name: {data['name']}")
if 'posts' in data:
    print("User Posts:", data['posts'])
if 'videos' in data:
    print("User Videos:", data['videos'])
if 'photos' in data:
    print("User Photos:", data['photos'])

# 將資料存在 env : 
# nano ~/.zshrc
# export SQL_USER='當初設定的使用名稱'
# export SQL_PASSWORD='當初設定的密碼'
# 直接離開即可，他會詢問是否儲存？
# 離開後，到vscode python terminal介面輸入以下：
# source ~/.zshrc
# 接著import os 就可以正常召喚 env
