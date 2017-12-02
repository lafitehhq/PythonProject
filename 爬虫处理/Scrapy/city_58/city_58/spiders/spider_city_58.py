# -*- coding: utf-8 -*-
import scrapy


class SpiderCity58Spider(scrapy.Spider):
    name = 'spider_city_58'  # 爬虫名
    allowed_domains = ['58.com']  # 允许的站点
    start_urls = ['http://58.com/']  # 启动链

    def parse(self, response):
        print('成功进入了解析器')
