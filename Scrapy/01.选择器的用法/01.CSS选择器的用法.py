# -*- coding: utf-8 -*-

from scrapy import Selector
with open('test.html', encoding='utf-8') as f:
    text = f.read()
sel = Selector(text=text)
print(sel.css('top'))