# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/ref/settings.html#item-pipelines

class ScraperPipeline(object):
    def process_item(self, domain, item):
        return item