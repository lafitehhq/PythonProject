# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

# 自动生成的代码
# class City58SpiderMiddleware(object):
# @classmethod
# def from_crawler(cls, crawler):
#     # This method is used by Scrapy to create your spiders.
#     s = cls()
#     crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#     return s
#
# def process_spider_input(self, response, spider):
#     # Called for each response that goes through the spider
#     # middleware and into the spider.
#
#     # Should return None or raise an exception.
#     return None
#
# def process_spider_output(self, response, result, spider):
#     # Called with the results returned from the Spider, after
#     # it has processed the response.
#
#     # Must return an iterable of Request, dict or Item objects.
#     for i in result:
#         yield i
#
# def process_spider_exception(self, response, exception, spider):
#     # Called when a spider or process_spider_input() method
#     # (from other spider middleware) raises an exception.
#
#     # Should return either None or an iterable of Response, dict
#     # or Item objects.
#     pass
#
# def process_start_requests(self, start_requests, spider):
#     # Called with the start requests of the spider, and works
#     # similarly to the process_spider_output() method, except
#     # that it doesn’t have a response associated.
#
#     # Must return only requests (not items).
#     for r in start_requests:
#         yield r
#
# def spider_opened(self, spider):
#     spider.logger.info('Spider opened: %s' % spider.name)


# 中间件之UAMiddleware：request中加入随机User-Agent
class UAMiddleware(object):
    # 定义一个User-Agent的List
    ua_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ',
        '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    ]

    # 对request进行拦截：
    def process_request(self, request, spider):
        ua = random.choices(self.ua_list)  # 使用random模块，随机在ua_list中选取User-Agent
        request.headers['Users-Agent'] = ua  # 把选取出来的User-Agent赋给request
        print(request.url)  # 打印出request的url
        print(request.headers['User-Agent'])   # 打印出request的headers

    # 对response进行拦截：判断是否连接超时或者 HTTP 500 错误导致失败的页面
    def process_response(self, request, response, spider):
        return response

    # 对process_request方法传出来的异常进行处理
    def process_exception(self, request, exception, spider):
        pass

# 中间件之RetryMiddleware：防止连接超时或者 HTTP 500 错误导致失败的页面。
class RetryMiddleware(object):
    # 判断是都有设置dont_retry以及判断response是否正常返回
    def process_request(self, request, response, spider):
        if




