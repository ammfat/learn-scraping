import requests
from bs4 import BeautifulSoup

class ScrapeDetik(object):
    def __init__(self, url, params=None):
        self.__set_website_data(url, params)
        self.__set_popular_news()

    def __set_website_data(self, url, params=None):
        self.response = requests.get(url, params=params)
        self.contents = BeautifulSoup(self.response.text, 'html.parser')
        
    def __set_popular_news(self):
        # self.popular_area_2 = contents.find('div', class_='grid-row list-content')
        self.popular_area = self.contents.find(attrs={'class': 'grid-row list-content'})
        
        titles = self.contents.find_all(attrs={'class': 'media__title'})
        self.titles = [ title.text.strip() for title in titles ]

        images = self.contents.find_all(attrs={'class': 'media__image'})
        self.images = [ image.find('a').find('img')['src'] for image in images ]

        urls = self.contents.find_all(attrs={'class': 'media__image'})
        self.urls = [ url.find('a')['href'] for url in urls ]

        # self.urls = [ url['href'] for url in urls ]


if __name__ == "__main__":
    url = 'https://www.detik.com/terpopuler'
    params = {'tag_from': 'wp_cb_mostPopular_more'}
    
    sd = ScrapeDetik(url, params)

    print('\nVVVVVVVVVVVVVVVVVVVVVVVVVVV')

    # print(sd.popular_area)
    # print(sd.titles)
    # print(sd.images)

    print(len(sd.titles), len(sd.images), len(sd.urls))