# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# from scrapy_spider.models import OoyyoDB, db_connect, create_table

class ScrapySpiderPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        # engine = db_connect()
        # create_table(engine)
        # self.Session = sessionmaker(bind=engine)
        pass

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        # session = self.Session()
        # ooyyodb = OoyyoDB()
        # ooyyodb.ooyyo = item["ooyyo"]
        # ooyyodb.author = item["author"]

        # try:
        #     session.add(ooyyodb)
        #     session.commit()
        # except:
        #     session.rollback()
        #     raise
        # finally:
        #     session.close()

        return item
