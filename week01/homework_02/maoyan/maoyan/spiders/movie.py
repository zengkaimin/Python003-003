import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:10]
        for movie in movies:
            item = MaoyanItem()
            movie_name = movie.xpath('./div[1]/span[@class="name "]/text()')
            movie_type = movie.xpath('./div[2]/span/following-sibling::text()')
            movie_date = movie.xpath('./div[4]/span/following-sibling::text()')
            item['movie_name'] = movie_name.extract_first()
            item['movie_type'] = movie_type.extract_first().strip()
            item['movie_date'] = movie_date.extract_first().strip()
            yield item

