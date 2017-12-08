# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import cookiejar

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


# 中间件-UAMiddleware：request中加入随机User-Agent
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

# # 中间件-RetryMiddleware：防止连接超时或者 HTTP 500 错误导致失败的页面。
# class RetryMiddleware(object):
#     # 判断是都有设置dont_retry以及判断response是否正常返回
#     def process_response(self, request, response, spider):
#         if request.meta.get('dont_retry',
#                                 False):  # 从meta中获取dont_retry关键字，如果为True，不重试，直接返回response；如果没有设置dont_retry关键字，则得到False值，继续执行下面判断。即默认重试
#             return response
#         if response.status in self.retry_http_codes:  # 查看response的返回码是否在重试返回码中
#             reason = response_status_message(response.status)  # 报错原因
#             return self._retry(request, reason, spider) or response  # 启用重试
#         return response
#
#     # 判断request异常
#     def process_exception(self, request, exception, spider):
#         if isinstance(exception, self.EXCEPTIONS_TO_RETRY) \
#                 and not request.meta.get('dont_retry', False):  # 判断process_request函数抛出的异常是否在EXCEPTIONS_TO_RETRY中，并且是否启动重试
#             return self._retry(request, exception, spider)
#
#     # 重试函数
#     def _retry(self, request, reason, spider):
#         retries = request.meta.get('retry_times', 0) + 1
#
#         retry_times = self.max_retry_times  # 最大重试次数
#
#         if 'max_retry_times' in request.meta:
#             retry_times = request.meta['max_retry_times']
#
#         stats = spider.crawler.stats
#         if retries <= retry_times:  # 判断是否达到最大重试次数
#             logger.debug("Retrying %(request)s (failed %(retries)d times): %(reason)s",
#                          {'request': request, 'retries': retries, 'reason': reason},
#                          extra={'spider': spider})  # 重试日志
#             retryreq = request.copy()
#             retryreq.meta['retry_times'] = retries  # 累加重试次数
#             retryreq.dont_filter = True  # 设置不过滤
#             retryreq.priority = request.priority + self.priority_adjust
#
#             if isinstance(reason, Exception):
#                 reason = global_object_name(reason.__class__)
#
#             stats.inc_value('retry/count')
#             stats.inc_value('retry/reason_count/%s' % reason)
#             return retryreq
#         else:
#             stats.inc_value('retry/max_reached')
#             logger.debug("Gave up retrying %(request)s (failed %(retries)d times): %(reason)s",
#                          {'request': request, 'retries': retries, 'reason': reason},
#                          extra={'spider': spider})
#
# # 中间件-CookiesMiddleware：追踪了web server发送的cookie，并在之后的request中发送回去
# class CookiesMiddleware(object):
#
#     def __init__(self, debug=False):
#     # 用字典生成多个cookiesjar
#         self.jars = defaultdict(CookieJar)
#         self.debug = debug
#
#     def process_request(self, request, spider):
#         if request.meta.get('dont_merge_cookies', False):
#             return
#         # 每个cookiesjar的key都存储在 meta字典中
#         cookiejarkey = request.meta.get("cookiejar")
#         jar = self.jars[cookiejarkey]
#         cookies = self._get_request_cookies(jar, request)
#         # 把requests的cookies存储到cookiesjar中
#         for cookie in cookies:
#             jar.set_cookie_if_ok(cookie, request)
#
#         # set Cookie header
#         # 删除原有的cookies
#         request.headers.pop('Cookie', None)
#         # 添加cookiesjar中的cookies到requests header
#         jar.add_cookie_header(request)
#         self._debug_cookie(request, spider)
#
#     def process_response(self, request, response, spider):
#         if request.meta.get('dont_merge_cookies', False):
#             return response
#         # extract cookies from Set-Cookie and drop invalid/expired cookies
#         cookiejarkey = request.meta.get("cookiejar")
#         jar = self.jars[cookiejarkey]
#         jar.extract_cookies(response, request)
#         self._debug_set_cookie(response, spider)
#         return response









