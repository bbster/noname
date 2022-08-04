import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        quotes = response.xpath('//*[@class="quotes"]')
        for quote in quotes:
            yield {'auhor': quotes.xpath('.//*[@class="author"]/text()').extract_first(),
                   'text': quotes.xpath('.//*[@class="text"]/text()').extract_first()}
