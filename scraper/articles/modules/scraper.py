import logging
import urllib.parse

import requests
import unidecode
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Scraper:
    """Class for scraping data from blog
    Arguments:
        base_url {string}: blog url
    """

    def __init__(self, base_url):
        self.base_url = base_url
        self.pages_urls = self.get_pages()
        self.posts_urls = self.get_posts_urls()

    def get_pages(self):
        """Gets URL of each page on a blog
        Returns:
            list -- list of urls
        """

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
        logger.info("Found %s pages.", len(urls))
        return urls

    def get_posts_urls(self):
        """Gets a list of URLs of each articles on a blog
        Raises:
            ConnectionError -- if URL is not responding
        Returns:
            list -- list of urls
        """

        urls = []
        for page in self.pages_urls:
            result = requests.get(page)
            if result.status_code == 200:
                c = result.content
                soup = BeautifulSoup(c, features="lxml")
                samples = soup.find_all("h2", "post-title")

                for sample in samples:
                    a = sample.find("a")
                    urls.append(a.get("href"))
            else:
                raise ConnectionError("URL is not responding.")

        if urls:
            logger.info("Found %s articles.", len(urls))
            return self.create_urls(urls)
        logger.error("No articles found.")
        return 0

    def create_urls(self, relative_urls):
        """Creates absolute URLs from relative
        Arguments:
            relative_urls {list} -- list of relative urls
        Returns:
            list -- list of absolute urls
        """

        joined_urls = []
        for url in relative_urls:
            joined_urls.append(urllib.parse.urljoin(self.base_url, url))

        return joined_urls

    def get_posts(self):
        """Gets content of each article and it's author
        Raises:
            ConnectionError: if URL is not responding
        Returns:
            list -- list of articles content and author
        """

        posts_content = []
        for post_url in self.posts_urls:
            result = requests.get(post_url)
            if result.status_code == 200:
                c = result.content
                soup = BeautifulSoup(c, features="lxml")
                post = soup.find_all("div", "post-content")[0].text.replace('\n','')
                author = soup.find_all("span", "author-name")[0].text
                posts_content.append((post, (transform_name(author), author)))
            else:
                raise ConnectionError("URL is not responding.")

        return posts_content


def transform_name(name):
    """Makes text lower case, converts unicode characters and removes space
    Arguments:
        name {string} -- a name
    Returns:
        string -- string without whitespace and unicode characters
    """
    name = unidecode.unidecode(name.lower()).replace(" ", "")
    return name
