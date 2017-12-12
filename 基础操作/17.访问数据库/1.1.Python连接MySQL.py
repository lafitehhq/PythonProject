# -*- coding: utf-8 -*-

import pymysql

# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='ConnectMySQLTest',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
print('MySQl链接成功')
