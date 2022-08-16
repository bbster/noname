import scrapy


class TableSpider(scrapy.Spider):
    name = 'table'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']

    def parse(self, response):
        table = response.xpath('//table[contains(@class, "wikitable sortable")]')[0]
        trs = table.xpath('.//tr')[1:]
        for tr in trs:
            rank = tr.xpath('.//th/text()').extract_first().strip()
            city = tr.xpath('.//td[1]//text()').extract_first()
            state = tr.xpath('.//td[2]//text()').extract_first()
            estimate_2021 = tr.xpath('.//td[3]//text()').extract_first()
            census_2020 = tr.xpath('.//td[4]//text()').extract_first()
            change = tr.xpath('.//td[5]//text()').extract_first()
            location = tr.xpath('.//td[10]//span[@class="geo-dec"]//text()').extract_first()
            city_url = tr.xpath('.//td[1]//a/@href').extract_first()
            result_url = response.urljoin(city_url)
            breakpoint()
            yield {
                    "rank": rank,
                    "city": city,
                    "state": state,
                    "estimate_2021": estimate_2021,
                    "census_2020": census_2020,
                    "change": change,
                    "location": location,
                    "state_url": result_url,
            }
