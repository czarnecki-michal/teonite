from bs4 import BeautifulSoup
import requests
import urllib.parse

home_url = "https://teonite.com/blog/"

class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.pages = self.get_pages()
        self.posts = self.get_posts()

    def get_pages(self):
        urls = [self.base_url]
        page = 2
        while True:
            page_url = f"https://teonite.com/blog/page/{page}/index.html"
            result = requests.get(page_url)
            page += 1
            if result.status_code == 200:
                urls.append(page_url)
            else:
                break
        return urls

    def get_posts(self):
        urls = []
        for page in self.pages:
            result = requests.get(page)
            c = result.content
            soup = BeautifulSoup(c, features="lxml")
            samples = soup.find_all("h2", "post-title")

            for sample in samples:
                a = sample.find("a")
                urls.append(a.get("href"))
        return self.create_urls(urls)

    def create_urls(self, relative_urls):
        joined_urls = []
        for url in relative_urls:
            joined_urls.append(urllib.parse.urljoin(self.base_url, url))

        return joined_urls

    def get_posts_content(self):
        posts_content = []
        for post in self.posts:
            result = requests.get(post)
            c = result.content
            soup = BeautifulSoup(c, features="lxml")
            samples = soup.find_all("div", "post-content")
            posts_content.append(samples[0].text)
            print(samples[0].text)
        return posts_content


post_url = "https://teonite.com/blog/"
scrapper = Scrapper(post_url)
scrapper.get_posts_content()