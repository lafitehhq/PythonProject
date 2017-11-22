# -*- coding: utf-8 -*-

import pymongo
client = pymongo.MongoClient('localhost', 27017)  # 端口号是数值型
db = client.ConnectMongoDBTest  # 连接ConnectMongoDBTest数据库，没有则新建
print('MongoDB链接成功')

