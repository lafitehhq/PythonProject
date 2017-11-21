
# -*- coding:utf-8 -*-

from pymongo import MongoClient
import requests

client = MongoClient()
db = client.lagou #创建一个lagou数据库
my_set = db.job #创建job集合

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
payload = {
    'first':'true',
    'pn':'1',
    'kd':'爬虫',
}

headers = {
    'Cookie': 'user_trace_token=20171023155946-00f54b89-6fcf-4b28-9ba4-b3b680ca7a99; LGUID=20171023155947-239cc366-b7c8-11e7-a555-525400f775ce; JSESSIONID=ABAAABAACDBABJB0DE5B2C86AD665A241647A0F88C05676; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%2588%25AC%25E8%2599%25AB%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508745588,1508745610,1511255868; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511256006; _ga=GA1.2.1934887961.1508745588; LGSID=20171121171747-d6f924ac-ce9c-11e7-9972-5254005c3644; LGRID=20171121172005-29700940-ce9d-11e7-9b58-525400f775ce; SEARCH_ID=25336192c62d4c3dae475a114d186bfb',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Referer' :'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
} #填入对应的headers信息

response = requests.post(url, data=payload, headers=headers)  # 使用POST方法请求数据，加上payload和headers信息
my_set.insert(response.json()['content']['positionResult']['result'])  # 把对应的数据保存到MOngoDB
