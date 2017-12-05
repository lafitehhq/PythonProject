# -*- coding: utf-8 -*-

""" 
将所有抓取的Item（来自所有蜘蛛）存储到单个items.json文件中，
每行包含一个项目，以JSON格式序列化
"""

import json
class JsonWritePipeline(object):
    def open_spider(self, spider):  # 在爬虫开始时打开文件
        self.file = open('items.json', 'w')

    def close_spider(self, spider):  # 在爬虫结束时关闭文件
        self.file.close()

    def process_item(self, item, spider):  # 把爬取到的item转换为json格式，保存进文件
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item  # 注意要返回item