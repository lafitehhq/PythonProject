# -*- coding: utf-8 -*-

url = 'https://book.douban.com/subject/1084336/comments/'

import requests
r = requests.get(url).text

from lxml import etree
s = etree.HTML(r)
# 方式1：从浏览器直接复制
print(s.xpath('//*[@id="comments"]/ul/li[1]/div[2]/p/text()'))  # 从浏览器复制第一条评论的Xpath
# print(s.xpath('//*[@id="comments"]/ul/li/div[2]/p/text()'))  # 掌握规律，删除li[]的括号，获取全部短评
# 方式2：手写Xpath
print(s.xpath('//div[@class="comment"]/p/text()')[0])  # 手写Xpath获取第一条评论
# print(s.xpath('//div[@class="comment"]/p/text()'))  # 手写Xpath获取全部短评
print('---'*20)
