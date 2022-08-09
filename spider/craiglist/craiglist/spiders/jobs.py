import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ['https://newyork.craigslist.org/search/egr']

    def parse(self, response):
        listings = response.xpath('//li[@class="result-row"]')
        for listing in listings:
            date = listing.xpath('.//*[@class="result-date"]/@datetime').extract_first()
            link = listing.xpath('.//a[@class="result-title hdrlnk"]/@href').extract_first()
            text = listing.xpath('.//a[@class="result-title hdrlnk"]/text()').extract_first()

            yield scrapy.Request(link, callback=self.parse_listing, meta={'date': date,
                                                                          'link': link,
                                                                          'text': text})
            # yield {'date': date,
            #        'link': link,
            #        'text': text}

        next_page_url = response.xpath('//a[text()="next > "]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

    def parse_listing(self, response):
        date = response.meta['date']
        link = response.meta['link']
        text = response.meta['text']

        compensation = response.xpath('//*[@class="attrgroup"]/span[1]/b/text()').extract_first()
        employment_type = response.xpath('//*[@class="attrgroup"]/span[2]/b/text()').extract_first()
        job_title = response.xpath('//*[@class="attrgroup"]/span[3]/b/text()').extract_first()

        images = response.xpath('//*[@id="thumbs"]//@src').extract()
        images = [image.replace('50x50c', '600x450') for image in images]

        requirements = response.xpath('//*[@id="postingbody"]/text()').extract()
        yield {'date': date,
                'link': link,
                'text': text,
                'compensation': compensation,
                'employment_type': employment_type,
                'job_title': job_title,
                'images': images,
                'requirements': requirements}