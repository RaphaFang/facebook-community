import requests
from requests_oauthlib import OAuth2Session

# 替換為您的應用程式ID和應用程式密鑰
app_id = 'YOUR_APP_ID'
app_secret = 'YOUR_APP_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'
scope = ['groups_access_member_info', 'user_posts']

oauth = OAuth2Session(app_id, redirect_uri=redirect_uri, scope=scope)
authorization_url, state = oauth.authorization_url('https://www.facebook.com/v13.0/dialog/oauth')

print('Please go to %s and authorize access.' % authorization_url)

# 在瀏覽器中打開上述URL並進行授權，然後將回調URL輸入到終端中
response_url = input('Enter the full callback URL: ')
token = oauth.fetch_token('https://graph.facebook.com/v13.0/oauth/access_token',
                          authorization_response=response_url,
                          client_secret=app_secret)

print('Access Token:', token)