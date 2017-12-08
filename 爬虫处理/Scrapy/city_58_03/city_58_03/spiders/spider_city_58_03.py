# -*- coding: utf-8 -*-
import scrapy

from pyquery import PyQuery
from ..items import City58Item
from scrapy.http import Request


class SpiderCity5803Spider(scrapy.Spider):
    name = 'spider_city_58_03'
    allowed_domains = ['58.com']
    start_urls = ['http://58.com/']

    # 判断项目运行是否可行代码
    # def parse(self, response):
    #     print('成功进入了解析器')

    # 生产环境代码
    def parse(self, response):
        jpy = PyQuery(response.text)
        li_list = jpy('body > div.mainbox > div.main > div.content > div.listBox > ul > li').items()
        for it in li_list:
            a_tag = it('div.des > h2 > a')
            item = City58Item()
            item['name'] = a_tag.text()
            item['url'] = a_tag.attr('href')
            item['price'] = it('div.listliright > div.money > b').text()

            if item['url']:  # 判断url是否为空
                yield Request(item['url'],
                              callback=self.detail_parse,
                              meta={'item': item},  # 使用meta参数，把item传给detail_parse()
                              priority=10,  # 优先级设为10
                              dont_filter=True  # 强制不过滤)
                              )

        url = jpy('#bottom_ad_li > div.pager > a.next').attr('href')  # 提取翻页链接
        test_request = Request(url,
                               callback=self.parse,
                               priority=10,
                               # meta={'dont_redirect': True}
                               dont_filter=True  # 对url不过滤
                               )
        yield test_request  # 实现翻页

    def detail_parse(self, response):
        jpy = PyQuery(response.text)
        item = response.meta['item']  # 接收item
        item['introduce_item'] = jpy(
            'body > div.main-wrap > div.house-detail-desc > div.main-detail-info.fl > div.house-word-introduce.f16.c_555 > ul > li:nth-child(1) > span.a2').text()  # 提取房屋亮点
        item['address'] = jpy(
            'body > div.main-wrap > div.house-basic-info > div.house-basic-right.fr > div.house-basic-desc > div.house-desc-item.fl.c_333 > ul > li:nth-child(6) > span.dz').text()  # 房屋详情地址
        item['phone_number'] = jpy(
            'body > div.main-wrap > div.house-basic-info > div.house-basic-right.fr > div.house-fraud-tip > div.house-chat-phone > span').text()  # 电话号码
        return item