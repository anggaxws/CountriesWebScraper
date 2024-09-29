# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class CountryscraperPipeline:
    def process_item(self, item, spider):
        return item

from sqlalchemy.orm import sessionmaker
from .models import Country, db_connect, create_table

class SQLPipeline:

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        country = Country(
            name=item['name'],
            capital=item['capital'],
            population=item['population'],
            area=item['area']
        )
        try:
            session.add(country)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item