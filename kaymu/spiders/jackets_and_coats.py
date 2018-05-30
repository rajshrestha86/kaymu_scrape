# -*- coding: utf-8 -*-
import scrapy
import random
from time import sleep
from kaymu.items import ProductLoader


class JacketsAndCoatsSpider(scrapy.Spider):
    name = 'jackets_and_coats'
    allowed_domains = ['daraz.com.np']
    start_urls = ['http://daraz.com.np/mens-jackets-coats/','https://www.daraz.com.np/mens-sweaters-sweatshirts/','https://www.daraz.com.np/mens-hoodies/']

    def parse(self, response):
        products=response.xpath('//*[@class="products "]')
        links=products.xpath('.//*[@class="link"]')
	
        for item in links:
            loader=ProductLoader(selector=item)
            loader.add_xpath('brand','.//*[@class="brand "]/text()')
            loader.add_xpath('name','.//*[@class="name"]/text()')
            loader.add_xpath('price','.//*[@class="price"]/span[2]/text()')
            yield loader.load_item()
        
        sleep(random.randrange(1,3))
        next_page=response.xpath('//*[@title="Next"]/@href').extract_first()
        print(next_page)
        if next_page==None:
            return
        yield scrapy.Request(str(next_page))
