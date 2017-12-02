# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem

class PricePipeline(object):
    vat_factor = 1.15
    def process_item(self, item, spider):
        if item['price']:  # 有价格则执行，相当于true
            if item['price_excludes_vat']:  # 如果价格不包括增值税，则把价格乘上一个增值税系数
                item['price'] = item['price'] * self.vat_factor
            return item
        else:  # 如果没有价格，则抛弃这个item
            raise DropItem('%s 并无价格,商品被抛弃' % item)


class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()  # 初始化中创建一个空集合
    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem('%s 为重复的商品' %item)
        else:
            self.ids_seen.add(item['id'])
            return item