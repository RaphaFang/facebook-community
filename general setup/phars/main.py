from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import csv
import os

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(10)

email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
email.send_keys(os.getenv('FB_EMAIL'))
password.send_keys(os.getenv('FB_PASSWORD'))


password.send_keys(Keys.RETURN)
time.sleep(10)


driver.get("https://www.facebook.com/groups/519698198656273")
time.sleep(15)

for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)


page_content = driver.page_source
driver.quit()

soup = BeautifulSoup(page_content, 'html.parser')
posts_container = soup.find('div', {'class': 'x9f619 x1n2onr6 x1ja2u2z xeuugli xs83m0k x1xmf6yo x1emribx x1e56ztr x1i64zmx xjl7jj x19h7ccj xu9j1y6 x7ep2pv'})
posts = posts_container.find_all('div', {'class': 'x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z'}, limit=10)

# 寫入CSV
with open('facebook_posts.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Author', 'Date', 'Content', 'Images'])

    for post in posts:
        try:
            author_element = post.find('strong')
            author = author_element.text if author_element else 'No author found'
        except AttributeError:
            author = 'No author found'

        try:
            date_element = post.find('abbr')
            date = date_element.text if date_element else 'No date found'
        except AttributeError:
            date = 'No date found'

        try:
            content_element = post.find('div', {'data-ad-preview': 'message'})
            content = content_element.text if content_element else 'No content found'
        except AttributeError:
            content = 'No content found'

        images = post.find_all('img')
        image_urls = [img['src'] for img in images]

        writer.writerow([author, date, content, ', '.join(image_urls)])

        print(f"Author: {author}")
        print(f"Date: {date}")
        print(f"Content: {content}")
        print(f"Images: {image_urls}")
        print("\n")

print("Data has been written to facebook_posts.csv")

# nano ~/.zshrc
# source ~/.zshrc