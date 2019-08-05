from bs4 import BeautifulSoup
import requests
import urllib.parse
import unidecode
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


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
        logger.info(f"Found {len(urls)} pages.")
        return urls

    def get_posts_urls(self):
        urls = []
        for page in self.pages_urls:
            result = requests.get(page)
            if result.status_code == requests.codes.ok:
                c = result.content
                soup = BeautifulSoup(c, features="lxml")
                samples = soup.find_all("h2", "post-title")

                for sample in samples:
                    a = sample.find("a")
                    urls.append(a.get("href"))
            else:
                raise ConnectionError("URL is not responding.")

        if urls:
            logger.info(f"Found {len(urls)} articles.")
            return self.create_urls(urls)
        else:
            logger.error("No articles found.")

    def create_urls(self, relative_urls):
        joined_urls = []
        for url in relative_urls:
            joined_urls.append(urllib.parse.urljoin(self.base_url, url))

        return joined_urls

    def get_posts(self):
        posts_content = []
        for post_url in self.posts_urls:
            result = requests.get(post_url)
            if result.status_code == requests.codes.ok:
                c = result.content
                soup = BeautifulSoup(c, features="lxml")
                post = soup.find_all("div", "post-content")[0].text.replace('\n','')
                author = soup.find_all("span", "author-name")[0].text
                posts_content.append((post, (transform_name(author), author)))
            else:
                raise ConnectionError("URL is not responding.")

        return posts_content



def transform_name(name):
    name = unidecode.unidecode(name.lower()).replace(" ", "")
    return name



