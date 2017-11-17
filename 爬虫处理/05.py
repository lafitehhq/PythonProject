# -*- coding: utf-8 -*-

url = 'https://book.douban.com/subject/1084336/comments/hot?p=2'

import requests
r = requests.get(url).text

from lxml import etree
s = etree.HTML(r)
file = s.xpath('//div[@class="comment"]/p/text()')
name = s.xpath('//*[@id="comments"]/ul/li/div[2]/h3/span[2]/a/text()')

# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(7, 5))  # 7行5列
# print(df)
# print(df.head())  # 打印前5行


import pandas as pd
df = pd.DataFrame(file)
df.to_excel('05_comment.xlsx')
http://www.zkh360.com/Product/SearchProduct?brandId=240&pageIndex=2&pageSize=20
http://www.zkh360.com/Product/SearchProduct?brandId=240&pageIndex=3&pageSize=20




