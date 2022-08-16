# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiTableSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    estimate_2021 = scrapy.Field()
    census_2020 = scrapy.Field()
    change = scrapy.Field()
    location = scrapy.Field()
    city_url = scrapy.Field()
    result_url = scrapy.Field()
