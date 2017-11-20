# -*- coding: utf-8 -*-

# --思路版-- #
# import requests
# import pandas as pd
#
# headers = {
#       'authorization':'Bearer Mi4xS1FfMEFRQUFBQUFBVU1MTTBjWWdEQmNBQUFCaEFsVk50dmZhV2dCaTdYN1RfYzFQYzRhMkhVZkpSX09DemNob1ZB|1508747702|4012160a02b4ec96b026242c6f91a2388a716468',
#       'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36x-udid:AFDCzNHGIAyPTqjy5Y0RvKP7umKDH4MbrRE=' ,
#       # 'x-udid':'AFDCzNHGIAyPTqjy5Y0RvKP7umKDH4MbrRE='
# }
#
# url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20'
#
# response = requests.get(url)
# print(response.headers)  # 测试获取响应请求头
# response = requests.get(url, headers=headers)
# print(response.status_code)  # 测试获取响应状态码
# response = requests.get(url, headers=headers).json()
# print(response)  # 将响应请求头转化成json格式
# response = requests.get(url, headers=headers).json()['data']
# print(response)  # 将响应请求头转化成json格式并只获取'data'对象的数据
#
# df = pd.DataFrame.from_dict(response)  # ‘from_dict’函数将response对象转换成DataFrame对象
# print(df.head(2))  # 打印DataFrame对象中的前2行
# print(df.head())  # 打印DataFrame对象中的所有行
# df.head(2).to_csv('06_user.csv')  # 将DataFrame对象前2行保存至csv
# df.to_csv('06_user.csv')  # 将DataFrame对象所有行保存至csv


# --进阶版-- #
import requests
import pandas as pd
import time

headers = {
      'authorization':'Bearer Mi4xS1FfMEFRQUFBQUFBVU1MTTBjWWdEQmNBQUFCaEFsVk50dmZhV2dCaTdYN1RfYzFQYzRhMkhVZkpSX09DemNob1ZB|1508747702|4012160a02b4ec96b026242c6f91a2388a716468',
      'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36x-udid:AFDCzNHGIAyPTqjy5Y0RvKP7umKDH4MbrRE=' ,
      # 'x-udid':'AFDCzNHGIAyPTqjy5Y0RvKP7umKDH4MbrRE='
}

userData = []  # 将循环获取的数据存放于列表中
def get_user_data(page):
      for i in range(page):
            url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i * 20)
            response = requests.get(url, headers=headers).json()['data']
            userData.extend(response)
            print('正在爬取第%s页' % str(i+1))  # 控制台显示抓取进度
            time.sleep(1)  # 设置打印停顿防止被封

if __name__ == '__main__':
    get_user_data(10)
    df = pd.DataFrame.from_dict(userData)
    df.to_csv('06_user_upgrade.csv')