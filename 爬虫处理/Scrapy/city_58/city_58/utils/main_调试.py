# -*- coding: utf-8 -*-

from scrapy import cmdline

# cmdline.execute('Scrapy crawl spider_city_58'.split())  # 不写默认以空格间隔
cmdline.execute('Scrapy crawl spider_city_58'.split(' '))  # 测试spider_city_58文件
