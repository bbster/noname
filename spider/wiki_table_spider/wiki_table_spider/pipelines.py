from itemadapter import ItemAdapter
import os
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings

class WikiTableSpiderPipeline:

    def __init__(self):
        settings = get_project_settings()
        connection = MongoClient(
                settings['MONGODB_SERVER'],
                settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item

