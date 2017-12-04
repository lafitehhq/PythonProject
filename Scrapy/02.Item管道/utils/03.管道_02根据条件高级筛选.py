# -*- coding: utf-8 -*-

"""
查找重复Item并删除已处理的Item的过滤器。
假设Item具有唯一的ID，但是Spider会返回具有相同id的多个Item：
"""

from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()  #初始化中创建一个空集合用于存储

    def process_item(self, item, spider):  # #查看id是否在ids_seen中，如果在，就抛弃该Item，如果不在就添加到ids_seen中，下一次其它Item有相同的id就抛弃那个Item
        if item['id'] in self.ids_seen:
            raise DropItem('%s 已在集合中存在' %item)
        else:
            self.ids_seen.add(item['id'])
            return item  # 记得一定要返回Item
