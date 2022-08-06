from scrapy.http import Request
from scrapy import Spider
from scrapy.loader import ItemLoader
from ..items import BooksCrawlerItem
import os
import glob

def product_info(response, value):
    return response.xpath('//th[text()="'+ value +'"]/following-sibling::td/text()').extract_first()


class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    # def __init__(self, category):
    #     self.start_urls = [category]
    #     pass

    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()

        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)

        # next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        # next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        # absolute_next_page_url = response.urljoin(next_page_url)
        # yield Request(absolute_next_page_url)

    def parse_book(self, response):
        item_loader = ItemLoader(item=BooksCrawlerItem(), response=response)
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()

        image_urls = response.xpath('//img/@src').extract_first()
        image_urls = image_urls.replace('../..', 'http://books.toscrape.com/')

        item_loader.add_value('title', title)
        item_loader.add_value('price', price)
        item_loader.add_value('image_urls', image_urls)

        return item_loader.load_item()
    #
    #     rating = response.xpath('//*[contains(@class, "star-rating")]/@class').extract_first()
    #     rating = rating.replace('star-rating', '')
    #
    #     description = response.xpath('//*[@id="product_description"]/following-sibling::p/text()').extract_first()
    #
    #     upc = product_info(response, "UPC")
    #     product_type = product_info(response, "Product Type")
    #     price_excl = product_info(response, "Price (excl. tax)")
    #     price_incl = product_info(response, "Price (incl. tax)")
    #     tax = product_info(response, "Tax")
    #     availability = product_info(response, "Availability")
    #     number_of_reviews = product_info(response, "Number of reviews")
    #
    #     yield {
    #         'title': title,
    #         'price': price,
    #         'image_url': image_url,
    #         'rating': rating,
    #         'description': description,
    #         'upc': upc,
    #         'product_type': product_type,
    #         'price_excl': price_excl,
    #         'price_incl': price_incl,
    #         'tax': tax,
    #         'availability': availability,
    #         'number_of_reviews': number_of_reviews,
    #     }
    #
    # def close(self, reason):
    #     csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
    #     os.rename(csv_file, 'foobar.csv')
