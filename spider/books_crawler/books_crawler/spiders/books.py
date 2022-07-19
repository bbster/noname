from scrapy import Selector, Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = webdriver.Chrome("C:\chromedriver")
        self.driver.get("http://books.toscrape.com/")

        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        for book in books:
            url = 'http://books.toscrape.com/' + book
            yield Request(url, callback=self.parse_book)

    def parse_book(self, response):
        pass

