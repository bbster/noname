import scrapy
from ..items import ScarpyItemsExampleItem


class SampleItemsSpiderSpider(scrapy.Spider):
    name = 'sample_items_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        authors = response.xpath('//*[@class="author"]/text()').extract()

        item = ScarpyItemsExampleItem()
        item['authors'] = authors
        return item
