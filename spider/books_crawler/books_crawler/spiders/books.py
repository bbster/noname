from scrapy.http import Request
from scrapy import Spider

def product_info(response, value):
    return response.xpath('//th[text()="'+ value +'"]/following-sibling::td/text()').extract_first()


class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()

        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)

        # next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)

    def parse_book(self, response):
        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()

        image_url = response.xpath('//img/@src').extract_first()
        image_url = image_url.replace('../..', 'http://books.toscrape.com/')

        rating = response.xpath('//*[contains(@class, "star-rating")]/@class').extract_first()
        rating = rating.replace('star-rating', '')

        description = response.xpath('//*[@id="product_description"]/following-sibling::p/text()').extract_first()

        upc = product_info(response, "UPC")
        product_type = product_info(response, "Product Type")
        price_excl = product_info(response, "Price (excl. tax)")
        price_incl = product_info(response, "Price (incl. tax)")
        tax = product_info(response, "Tax")
        availability = product_info(response, "Availability")
        number_of_reviews = product_info(response, "Number of reviews")

        yield {
            'title': title,
            'price': price,
            'image_url': image_url,
            'rating': rating,
            'description': description,
            'upc': upc,
            'product_type': product_type,
            'price_excl': price_excl,
            'price_incl': price_incl,
            'tax': tax,
            'availability': availability,
            'number_of_reviews': number_of_reviews,
        }
