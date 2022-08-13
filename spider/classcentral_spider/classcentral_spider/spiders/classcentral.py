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

        for i in range(len(cources)):

            cource_name = cources[i].xpath('//*[@itemprop="name"]/text()').extract()[i]
            # cource_name = cource.xpath('//*[@class="color-charcoal course-name"]/h2/text()').extract()
            cource_url = cources[i].xpath('//*[@class="color-charcoal course-name"]/@href').extract()[i]
            absolute_cource_url = response.urljoin(cource_url)

            yield {
                'subject_name': subject_name,
                'cource_name': cource_name,
                'absolute_cour_url': absolute_cource_url
            }

        next_page = cources[0].xpath('//link[@rel="next"]/@href').extract_first()
        if next_page:
            absolute_next_page = response.urljoin(next_page)
            yield Request(absolute_next_page, callback=self.parse_subject)
