# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from pyquery import PyQuery

class City58Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()

    #
    def parse(self, response):
        jpy = PyQuery(response.text)
        li_list = jpy('div[3]/div[1]/div[5]/div[2]/ul/li[1]')