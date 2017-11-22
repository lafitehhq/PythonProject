# -*- coding: utf-8 -*-

from pymongo import MongoClient
client = MongoClient()
db = client.ConnectMongoDBTest  # 链接test数据库，没有则新建
my_set = db.set  # 使用set集合，没有则新建
my_set.insert({'name': 'Vito', 'age': '25'})  # 插入一条数据