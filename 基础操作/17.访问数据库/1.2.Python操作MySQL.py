# -*- coding: utf-8 -*-
"""
参考链接：https://www.cnblogs.com/fnng/p/6863616.html
"""

import pymysql

# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='ConnectMySQLTest',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

# --创建表-- #
# # 通过cursor创建游标
# cursor = connection.cursor()
# # 创建sql 语句，并执行
# try:
#     sql = 'CREATE TABLE `users` (' \
#               '`id` INT(11) NOT NULL AUTO_INCREMENT,' \
#               '`email` VARCHAR(255) COLLATE utf8_bin NOT NULL,' \
#               '`password` VARCHAR(255) COLLATE utf8_bin NOT NULL,' \
#               'PRIMARY KEY (`id`)' \
#               ') ENGINE=INNODB DEFAULT CHARSET=utf8 ' \
#               'AUTO_INCREMENT=1 ;'
#     cursor.execute(sql)
#     # 提交SQL
#     connection.commit()
#     print('创建表完成')
# except pymysql.err.InternalError:
#     print('数据表已存在')

print("-----------华丽分割线------------")
# # --插入数据-- #
# # 通过cursor创建游标
# cursor = connection.cursor()
# # 创建sql 语句，并执行
# sql = "INSERT INTO `users` (`email`, `password`) VALUES ('648725844@qq.com', '123456')"
# cursor.execute(sql)
# # 提交SQL
# connection.commit()
# print('插入数据完成')

print("-----------华丽分割线------------")
# --查询数据--#
# 通过cursor创建游标
cursor = connection.cursor()
# 创建sql 语句，并执行
# 查询数据库单条数据
sql = "SELECT `id`, `password` FROM `users` WHERE `email`='lafitehhq@126.com'"
cursor.execute(sql)
result1 = cursor.fetchone()
print(result1)
# 查询数据库多条数据
sql = "SELECT `id`, `password` FROM `users`"
cursor.execute(sql)
result2 = cursor.fetchall()
for data in result2:
    print(data)

print("-----------华丽分割线------------")
# 关闭数据连接
connection.close()



