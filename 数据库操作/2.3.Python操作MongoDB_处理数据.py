# -*- coding: utf-8 -*-

import pymongo
client = pymongo.MongoClient('localhost', 27017)  # 端口号是数值型
db = client.lagou  # 连接ConnectMongoDBTest数据库，没有则新建

print("-----------华丽分割线------------")
# my_set = db.job  # 连接名为users的集合，没有则新建
my_set = db.PythonJobs  # 连接名为users的集合，没有则新建

print("-----------华丽分割线------------")
# --查询数据-- #
# 查询数据库数据总数
num = my_set.find().count()
print(num)
# 按字段降序显示
result3 = my_set.find()
for data in result3:
    # print(type(data))
    # print(data)
    print(data['city'], '       ', data['industryField'], '       ', data['workYear'], '       ', data['salary'], '       ', data['companyFullName'])











