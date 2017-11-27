# -*- coding: utf-8 -*-

from selenium import webdriver

# 调用浏览器窗口并连接网站
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
driver.get('http://www.baidu.com')
print('浏览器窗口已打开')


from selenium.webdriver.common.keys import Keys
# 查找输入框
elem = driver.find_element_by_xpath('//*[@id = "kw"]')
# 模拟点击回车
elem.send_keys('Python Selenium', Keys.ENTER)
print(driver.page_source)


