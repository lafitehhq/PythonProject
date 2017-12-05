# -*- coding: utf-8 -*-

""" 
以下假设的管道，它调整 price那些不包括增值税（price_excludes_vat属性）的项目的价格，并删除那些不包含价格的项目
"""
from scrapy.exceptions import DropItem

class PricePipeline(object):
    vat_factor = 1.15  # 增值税系数
    def process_iten(self, item, spider):
        if item['price']:  # 价格存在；相当于‘price’=true，
            if item['price_excludes_vat']:  # 如果价格不包括增值税，则把价格乘上一个增值税系数
                item['price'] = item['price'] * self.vat_factor
            return  item
        else:  # 如果没有价格，则抛弃这个item
            raise DropItem('%s 没有显示价格' % item)