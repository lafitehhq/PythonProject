#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 字符串转义
print("I\'m \"OK\"!")
print("I\'m learning \nPython!")  # \n表示换行
print("I\'m learning \tPython!")  # \t表示制表符
print(r'\\\\\\n\\\\')  # r''表示''内部的字符串默认不转义


s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
