import requests
from bs4 import BeautifulSoup
from datetime import date

def get_sitemap(sitemap_url):
    sitemap = requests.get(sitemap_url)
    soup = BeautifulSoup(sitemap.content, 'html.parser')
    urls = soup.find_all('loc')
    list_url = []
    for url in urls:
        list_url.append(url.get_text())
    return list_url

if __name__ == "__main__":
    sitemap_url ='test.com'
    get_sitemap(sitemap_url)

