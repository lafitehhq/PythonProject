# -*- coding: utf-8 -*-


from pyquery import PyQuery

with open('index.html', encoding='utf-8') as f:
    text = f.read()


# 断点测试注入代码(设置断点，右键‘debug as ...’ + 'ALT+F8'时时注入代码)
jpy = PyQuery(text)

# # 取文本信息；搜索li标签下的a标签下的div标签的内容 ；jpy('li a > div').text()
# # 取文本属性；jpy('.top').attr('class')
# pass

# 取文本信息；遍历li标签下的文本
items = jpy('li')
for i in items.items():
    print(i.text())

print('--'*20)
# 取文本属性；遍历li标签下的class属性
items = jpy('li')
for i in items.items():
    print(i.attr('class'))