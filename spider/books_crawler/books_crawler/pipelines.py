# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os


class BooksCrawlerPipeline:
    def process_item(self, item, spider):
        os.chdir('C:/Project/noname/spider/books_crawler/image_dir')

        if item['images'][0]['path']:
            new_image_name = item['title'][0] + '.jpg'
            new_image_name = new_image_name.replace(':', ' ')
            new_image_name = 'full/' + new_image_name
            os.rename(item['images'][0]['path'], new_image_name)
