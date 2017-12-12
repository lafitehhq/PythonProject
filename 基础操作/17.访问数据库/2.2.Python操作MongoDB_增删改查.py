# -*- coding: utf-8 -*-

import pymongo
client = pymongo.MongoClient('localhost', 27017)  # 端口号是数值型
db = client.ConnectMongoDBTest  # 连接ConnectMongoDBTest数据库，没有则新建

print("-----------华丽分割线------------")
my_set = db.users  # 连接名为users的集合，没有则新建

print("-----------华丽分割线------------")
# --添加数据-- #
# my_set.insert({'name': 'Yanira', 'age': '22'})  # 插入一条数据

print("-----------华丽分割线------------")
# --修改数据-- #
my_set.update({"name": "Vito"}, {"$set": {"age": '25'}})  # 前面的索引，后面是要修改的值

print("-----------华丽分割线------------")
# --查询数据-- #
# 查询数据库数据总数
num = my_set.find().count()
print(num)
# 查询数据库单条数据
result = my_set.find_one()
print(result)
# 查询数据库多条数据
result2 = my_set.find()
for data in result2:
    print(data)
# 按字段默认排序显示
result3 = my_set.find().sort('age')
for data in result3:
    print(data)
# 按字段降序显示
result4 = my_set.find().sort('age', pymongo.DESCENDING)
for data in result4:
    print(data)
# 按字段升序显示
result4 = my_set.find().sort('age', pymongo.ASCENDING)
for data in result4:
    print(data)


print("-----------华丽分割线------------")
# 打印数据库中某些关键字段
import pandas as pd
result5 = my_set.find()
for data in result5:
    print(data['name'] + ' ' + data['age'])
    # print(type(data))
    # print(type(data['name'] + ' ' + data['age']))










