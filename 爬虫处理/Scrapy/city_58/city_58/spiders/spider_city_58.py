# -*- coding: utf-8 -*-
import scrapy

class SpiderCity58Spider(scrapy.Spider):
    name = 'spider_city_58'
    allowed_domains = ['58.com']
    start_urls = ['http://58.com/']

    # def parse(self, response):
    #     pass

    def parse(self, response):
        print('进入了解析器,启动Scrapy框架成功。')

