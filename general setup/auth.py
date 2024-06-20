import requests
from requests_oauthlib import OAuth2Session
import os 

app_id = os.getenv('YOUR_APP_ID_v1')
app_secret = os.getenv('YOUR_APP_SECRET_v1')
redirect_uri = 'https://localhost/'
scope = [ 'public_profile' ]

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

print(data)




# nano ~/.zshrc
# source ~/.zshrc