from bs4 import BeautifulSoup
import requests
import urllib.parse

import time
start = time.time()


home_url = "https://teonite.com/blog/"


def get_article_url(base_url):
    result = requests.get(base_url)
    c = result.content
    soup = BeautifulSoup(c, features="lxml")
    articles = soup.find_all("h2", "post-title")
    for article in articles:
        a = article.find("a")
        url = a.get("href")
        get_content(url)


def get_content(url):
    article_url = urllib.parse.urljoin(home_url, url)
    result = requests.get(article_url)
    c = result.content
    soup = BeautifulSoup(c, features="lxml")
    article_content = soup.find_all("div", "post-content")[0].text.replace('\n','')
    print(article_content, 0)

get_article_url(home_url)
for page_number in range(2,8):
    page = f"https://teonite.com/blog/page/{page_number}/index.html"
    get_article_url(page)

end = time.time()
print(end - start)