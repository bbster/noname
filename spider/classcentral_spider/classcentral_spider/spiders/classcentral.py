from scrapy import Spider
from scrapy.http import Request


class ClasscentralSpider(Spider):
    name = 'classcentral'
    allowed_domains = ['classcentral.com']
    start_urls = ['https://www.classcentral.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            subject_url = response.xpath('//a[contains(@title, "'+self.subject +'")]/@href').extract_first()
            absolute_subject_url = response.urljoin(subject_url)
            yield Request(absolute_subject_url, callback=self.parse_subject)
        else:
            self.log("Scraping all subjects.")
            subjects = response.xpath('//*[@class="border-box align-middle color-charcoal hover-no-underline"]/@href').extract()
            for subject in subjects:
                absolute_subject_url = response.urljoin(subject)
                yield Request(absolute_subject_url, callback=self.parse_subject)

    def parse_subject(self, response):
        subject_name = response.xpath('//h1/text()').extract_first()
        cources = response.xpath('//li[@itemtype="http://schema.org/Event"]')

        for cource in cources:
            cource_name = cource.xpath('.//*[@itemprop="name"]/text()').extract_first()
            cource_url = cource.xpath('.//*[@class="color-charcoal course-name"]/@href').extract_first()
            absolute_cource_url = response.urljoin(cource_url)

            yield {
                'subject_name': subject_name,
                'cource_name': cource_name,
                'absolute_cour_url': absolute_cource_url
            }

        next_page = cource.xpath('//link[@rel="next"]/@href').extract_first()
        if next_page:
            absolute_next_page = response.urljoin(next_page)
            yield Request(absolute_next_page, callback=self.parse_subject)
