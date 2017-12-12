# -*-coding:utf-8-*-

"""
'字典'：{}表示； 键值(key=>value)对用冒号(:)分隔，每个对之间用逗号(,)分割；可存储任意类型对象。
'元组'：()表示；值用逗号分隔；值不能修改。
'列表'：[]表示；值用逗号分隔；可存储任意类型的值；值能修改。
'字符串'：
"""

# 1、字典
dict = {'name': 'Zara', 'age': 7, 'general': 'Female'}
# 字典转为字符串，
print(str(dict))  # {'name': 'Zara', 'general': 'Female', 'age': 7}
print(type(str(dict)))  # <class 'str'>
print('--'*5)
# 字典可以转为元组
print(tuple(dict))  # ('name', 'general', 'age')
print(type(tuple(dict)))  # <class 'tuple'>
print('--'*5)
# 字典可以转为元组的值
print(tuple(dict.values()))  # (7, 'Zara', 'Female')
print(type(tuple(dict.values())))  # <class 'tuple'>
print('--'*5)
# 字典转为列表的键
print(list(dict))  # ['name', 'general', 'age']
print(type(list(dict)))  # <class 'list'>
print('--'*5)
# 字典转为列表的值
print(dict.values)
print(type(dict.values))
print('--'*5)

print("-----------华丽分割线------------")
# 2、元组
tup = (1, 2, 3, 4, 5)
# 元组转为字符串
print(tup.__str__())  # (1, 2, 3, 4, 5)
print(type(tup.__str__()))  # <class 'str'>
print('--'*5)
# 元组转为列表，返回：[1, 2, 3, 4, 5]
print(list(tup))  # [1, 2, 3, 4, 5]
print(type(list(tup)))  # <class 'list'>
print('--'*5)
# 元组不可以转为字典

print("-----------华丽分割线------------")
# 3、列表
nums = [1, 3, 5, 7, 8, 13, 20]
# 列表转为字符串
print(str(nums))  # [1, 3, 5, 7, 8, 13, 20]
print(type(str(nums)))  # <class 'str'>
print('--'*5)
# 列表转为元组
print(tuple(nums))  # (1, 3, 5, 7, 8, 13, 20)
print(type(tuple(nums)))  # <class 'tuple'>
print('--'*5)
# 列表不可以转为字典

print("-----------华丽分割线------------")
# 4、字符串
# 字符串转为元组
print(tuple(eval("(1,2,3)")))  # (1, 2, 3)
print(type(tuple(eval("(1,2,3)"))))
# 字符串转为列表
print(list(eval("(1,2,3)")))  # [1, 2, 3]
print(type(list(eval("(1,2,3)"))))
# 字符串转为字典
print(eval("{'name':'ljq', 'age':24}"))  # {'age': 24, 'name': 'ljq'}
print(type(eval("{'name':'ljq', 'age':24}")))