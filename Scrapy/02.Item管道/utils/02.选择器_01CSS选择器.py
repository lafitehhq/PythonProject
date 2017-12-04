# -*- coding: utf-8 -*-

from scrapy import Selector


with open('index.html', encoding='utf-8') as f:
    text = f.read()
# 测试读取html文件
# print(text)
# 声明Scrapy的内置选择器，并将html注入
sel = Selector(text=text)

# 断点测试注入代码(设置断点，右键‘debug as ...’ + 'ALT+F8'时时注入代码)
# 搜索所有包含top的标签的内容 ；sel.css('.top')
# 搜索所有包含top的p标签列的内容；sel.css('p.top')
# 搜索所有包含top的li标签的内容 ；sel.css('li.top')
# 搜索ID标签的内容 ；sel.css('#li_a_div')
# 搜索所有标签的内容 ；sel.css('*
# 模糊搜做包含div标签的内容；sel.css('li div') ---- 4个
# 搜索所有的li标签和div标签的内容 ； sel.css('li,div') ---- 8个
# 搜索所有的li标签下包含div标签（可以是子关系或孙关系）的内容 ； sel.css('li div') ---- 4个
# 搜索所有的li标签下子标签是div标签（只能是子关系）的内容 ； sel.css('li > div') ---- 2个

pass
