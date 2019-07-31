from bs4 import BeautifulSoup
import requests
import urllib.parse


class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.pages_urls = self.get_pages()
        self.posts_urls = self.get_posts_urls()

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

    def get_posts_urls(self):
        urls = []
        for page in self.pages_urls:
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

    def get_posts(self):
        posts_content = []
        for post_url in self.posts_urls:
            result = requests.get(post_url)
            c = result.content
            soup = BeautifulSoup(c, features="lxml")
            post = soup.find_all("div", "post-content")[0].text
            author = soup.find_all("span", "author-name")[0].text
            posts_content.append((post, author))
        return posts_content




post_url = "https://teonite.com/blog/"
scrapper = Scraper(post_url)
print(scrapper.get_posts()[2])