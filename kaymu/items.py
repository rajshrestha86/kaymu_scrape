# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, MapCompose, Join, TakeFirst
class KaymuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Product(scrapy.Item):
    name=scrapy.Field()
    brand=scrapy.Field()
    price=scrapy.Field()

 
to_int = Compose(TakeFirst(), int)
class ProductLoader(ItemLoader):
    default_item_class=Product
    name_out=str()
    brand_out=str()
    price_out=int()
