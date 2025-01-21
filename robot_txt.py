# coding: utf-8

# ----------------------------------------------------------------
# The code below is a snippet for checking if given URL is possible to crawl 
# ----------------------------------------------------------------


from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

def can_crawl(url):
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    rp = RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp.can_fetch("*", url)

def main():
    url = "http://www.mk.co.kr"
    if can_crawl(url):
        print(f"Can crawl {url}")
    else:
        print(f"Cannot crawl {url}")


if __name__ == '__main__':
    main()