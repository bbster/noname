from scrapy import Spider
from scrapy.loader import ItemLoader
from ..items import QuotesItem


class QuotesSpider(Spider):
    name = 'quotes' # 고유이름
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        load = ItemLoader(item=QuotesItem(), response=response)
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        load.add_value('h1_tag', h1_tag)
        load.add_value('tags', tags)

        return load.load_item()
        # yield {'H1 Tag': h1_tag, 'Tags': tags}

        # quotes = response.xpath('//*[@class="quote"]')
        #
        # for quote in quotes:
        #     text = quote.xpath('.//*[@class="text"]/text()').extract()
        #     author = quote.xpath('.//*[@class="author"]/text()').extract()
        #     tags = quote.xpath('.//*[@class="tag"]/text()').extract()
        #
        #     yield {'Text': text,
        #            'Author': author,
        #            'Tags': tags,
        #     }
        #
        # next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        # absolute_next_page_url = response.urljoin(next_page_url)
        #
        # yield scrapy.Request(absolute_next_page_url)
