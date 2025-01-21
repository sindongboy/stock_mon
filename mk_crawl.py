# coding: utf-8


import requests
from bs4 import BeautifulSoup

def get_top_10_news():
    url = "https://www.mk.co.kr"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = []

    # Find top 10 news elements (adjust selector based on actual page structure)
    top_news_section = soup.find('ul', class_='top_news_list')
    if top_news_section:
        for item in top_news_section.find_all('a', limit=10):
            title = item.get_text(strip=True)
            link = url + item['href']
            news_list.append((title, link))
    else:
        print("Could not find the top news section.")

    return news_list

if __name__ == "__main__":
    top_news = get_top_10_news()
    if top_news:
        print("Top 10 News from Maeil Business Newspaper:")
        for idx, (title, link) in enumerate(top_news, start=1):
            print(f"{idx}. {title} - {link}")
    else:
        print("No news found.")
