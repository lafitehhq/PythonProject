# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class City5802Pipeline(object):
    # 系统自动生成的代码
    # def process_item(self, item, spider):
    #     return item

    # 打开文件
    def open_spider(self, spider):
        self.file = open('58_chuzu.txt', 'w', encoding='utf-8')
        print('已打开文件')

    # 关闭文件
    def close_spider(self, spider):
        self.file.close()
        print('已关闭文件')

    # 编写管道
    def process_item(self, item, spider):
        line = '{}\n'.format(json.dumps(dict(item)))  # 将item对象转换成一个字符串；json.dumps()方法将字典序列化成字符串；format()函数用于拼接；'{}\n'表示一个换行符
        self.file.write(line)  # 把字符串写进文件
        return item