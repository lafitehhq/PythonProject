# -*- coding: utf-8 -*-

import json

class JsonWriterPipline(object):

    def open_spider(self, spider):
        self.file = open('items.json', 'w')  # 在爬虫开始时打开文件

    def close_spider(self, spider):
        self.file.close()  # 在爬虫结束时关闭文件

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item