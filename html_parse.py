import urllib3
from bs4 import BeautifulSoup


# Beautiful Soup implementation   -- ** Make sure ToS of website allow scraping**
# Also using urllib3
# -------------------------
http = urllib3.PoolManager()
#### ENTER URL BELOW
url = 'http://'
response = http.request('GET', url)
soup = BeautifulSoup(response.data, features="html.parser")

# Posts variable to search for specific HTML class. Tune to specific website
posts = soup.findAll(class_='blog-entry-content')

for post in posts:
    title = post.find(class_='blog-entry-title entry-title').get_text().replace('\n', '')
    link = post.find('a')['href']
    date = post.select('.blog-entry-date.clr')[0].get_text()
    print(title + link + date)