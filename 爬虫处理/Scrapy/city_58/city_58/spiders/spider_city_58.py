# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import City58Item


class SpiderCity58Spider(scrapy.Spider):
    name = 'spider_city_58'  # 爬虫名
    allowed_domains = ['58.com']  # 允许的站点

    # 测试Scrapy项目
    # start_urls = ['http://58.com/']  # 启动链
    #
    # def parse(self, response):
    #     print('成功进入了解析器')

    # 实战
    start_urls = ['http://sz.58.com/chuzu/']  # 开始爬取的链接

    def parse(self, response):
        jpy = PyQuery(response.text)
        # 获得房屋介绍与文本
        li_list = jpy('body > div.mainbox > div.main > div.content > div.listBox > ul > li').items()  # 获得所有的li标签
        for it in li_list:  # 遍历li标签
            a_tag = it('div.des > h2 > a')  # 获得每个li标签下的a标签
            item = City58Item()
            item['name'] = a_tag.text()  # 获取租房的名称；获取a标签下的文本
            item['url'] = a_tag.attr('href')  # 获取租房的跳转链接属性；获取a标签下的‘href属性’
            item['price'] = it('div.listliright > div.money > b').text()  # 获取租房的价格；获得每个li标签下的a标签
            yield item  # yield方法返回一系列结果值到管道，但函数不会结束（return函数会结束）；把Item返回给引擎
