from indexser import indexer
from url_status import noindex_google_url
from sitemap_crawler import get_sitemap
from time import sleep

def main(sitemap_url,domain,url_limit:int = 2000, index_limit:int=200):
    list_url = get_sitemap(sitemap_url)[0:url_limit]
    noindex_list = []
    for my_url in list_url:
        url_noindex = noindex_google_url(my_url,domain)
        print ('url_noindex',my_url)
        noindex_list.append(my_url)
    print (F'Look noindex_list# {len(noindex_list)}')
    for add_url in noindex_list[0:index_limit]:
        print ('START INDEX')
        print('add_url',add_url)
        indexer(add_url)
        sleep(2)






if __name__ == "__main__":
    sitemap_url = 'https://sitema.url'
    domain = 'domain.name'
    main(sitemap_url, domain, url_limit = 5, index_limit=3)

