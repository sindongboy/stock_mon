# coding: utf-8

# ----------------------------------------------------------------
# 매일 경제: 증권 색션 - 많이 본 뉴스
# url = "https://www.mk.co.kr/news/stock"
# section: news_list type_num best_view_news_list
# ----------------------------------------------------------------

import re
import requests
from bs4 import BeautifulSoup
from llm_interface import OpenAIClient


def get_top_10_news_url():
    """
    Fetch the top 10 news URLs from the Maeil Business Newspaper's stock section.

    This function sends a GET request to the specified URL, parses the HTML content using BeautifulSoup,
    and extracts the URLs of the top 10 news articles based on the best view count.

    Parameters:
    None

    Returns:
    list: A list of tuples containing the title and URL of each top 10 news article.
        If no articles are found, an empty list is returned.
    """

    url = "https://www.mk.co.kr/news/stock"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    url_list = []

    # Find top 10 news elements (adjust selector based on actual page structure)
    top_news_section = soup.find('ul', class_='news_list type_num best_view_news_list')
    if top_news_section:
        for item in top_news_section.find_all('a', limit=10):
            link = item['href']
            url_list.append((link))
    else:
        print("Could not find the top news section.")

    return url_list

def get_news_body(url):
    """
    Fetches the title and body of a news article from the given URL.

    This function sends a GET request to the specified URL, parses the HTML content using BeautifulSoup,
    and extracts the title and body of the news article.

    Parameters:
    url (str): The URL of the news article to fetch.

    Returns:
    tuple: A tuple containing the title and body of the news article.
        If the request fails or the article is not found, returns None.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h2', class_='news_ttl').get_text()
        body = soup.find('div', class_='news_cnt_detail_wrap', itemprop='articleBody').get_text()
        body = re.sub(r'\s+', ' ', body).strip()
        return title, body
    else:
        return None, None


def get_news_articles():
    """
    Fetches the top 10 news articles from the Maeil Business Newspaper's stock section.

    This function fetches the top 10 news URLs, then retrieves the title and body of each news article.

    Parameters:
    None

    Returns:
    list: A list of tuples containing the title and body of each news article.
        If no articles are found, an empty list is returned.
    """
    news_urls = get_top_10_news_url()

    return news_urls


if __name__ == "__main__":
    llm_client = OpenAIClient()
    top_news = get_news_articles()
    if top_news != None:
        for url in top_news:
            title, body = get_news_body(url)
            print(title+ '\n')
            print(body + '\n\n')
            print("Summary: " + llm_client.get_summary(body) + '\n\n')
            print("Opinion: " + llm_client.invest_opinions(body) + '\n\n')
            break
    else:
        print("No news found.")