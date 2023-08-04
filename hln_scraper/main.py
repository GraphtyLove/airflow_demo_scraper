import requests
from requests.cookies import RequestsCookieJar 
from typing import List 

def cookies_fetcher(url: str = "https://www.hln.be/") -> RequestsCookieJar:
    return requests.get(url).cookies.get_dict()

def get_article(url, session: requests.Session, cookies, article_index: int, number_of_articles: int) -> str:
    print(f"Scraping article {article_index+1}/{number_of_articles}")
    return session.get(url, cookies=cookies).text

def get_all_articles(articles_url: List[str]) -> List[str]:
    cookies = cookies_fetcher()
    session = requests.Session()
    articles = [get_article(article_url, session, cookies, i, len(articles_url)) for i, article_url in enumerate(articles_url)]

    return articles

if __name__ == "__main__":
    print("Start scraping...")
    articles_url = ["https://www.hln.be/deinze/na-levensbedreigende-slangenbeet-in-kroatie-bekomt-thibaut-6-nu-in-het-uz-gent-hij-zal-hier-nog-minstens-tot-het-einde-van-de-week-blijven~a21ad545/"]
    print(f"Scraping {len(articles_url)}")
    articles_conent = get_all_articles(articles_url)
    print("Done Scraping!")
