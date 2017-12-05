# -*- coding: utf-8 -*-

from scrapy import Selector


with open('index.html', encoding='utf-8') as f:
    text = f.read()
# 测试读取html文件
print(text)
# 声明Scrapy的内置选择器，并将html注入
sel = Selector(text=text)

# 断点测试注入代码(设置断点，右键‘debug as ...’ + 'ALT+F8'时时注入代码)
# 模糊搜索所有包含div标签下的内容,等效于css选择器中sel.css('div') ；sel.xpath('//li')  -- 4个
# 搜索某个路径下的某个标签下的内容 ；sel.xpath('/html/body/ul/li')  -- 4个
# 搜索某个路径下的某个标签下的内容 ；sel.xpath('/html/body/ul/li/a/div/text()')  -- 4个
# 搜索某个路径下的第2个标签下的P标签的内容 ；sel.xpath('//li')[2].xpath('./p')
# 脱壳操作取文本信息：sel.xpath('//li')[2].xpath('./p').extract_first()
# 脱壳操作取文本属性：sel.xpath('/html/body/ul/li')[0].xpath('./@class').extract_first()

pass
