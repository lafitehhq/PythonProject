# -*- coding: utf-8 -*-

import requests
import pandas as pd

url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20'

# response = requests.get(url)
# print(response.headers)

headers = {
      'authorization':'Bearer Mi4xS1FfMEFRQUFBQUFBVU1MTTBjWWdEQmNBQUFCaEFsVk50dmZhV2dCaTdYN1RfYzFQYzRhMkhVZkpSX09DemNob1ZB|1508747702|4012160a02b4ec96b026242c6f91a2388a716468',
      'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36x-udid:AFDCzNHGIAyPTqjy5Y0RvKP7umKDH4MbrRE=' ,
      # 'x-udid':'AFDCzNHGIAyPTqjy5Y0RvKP7umKDH4MbrRE='
}

# response = requests.get(url, headers=headers)
# print(response.status_code)

# response = requests.get(url, headers=headers).json()
# print(response)

# response = requests.get(url, headers=headers).json()['data']
# # print(response)

# import pandas as pd
# df = pd.DataFrame.from_dict(response)
# # print(df.head())
# df.to_csv('06_user.csv')


userData = []  # 将循环获取的数据存放于列表中
def get_user_data(page):
      for i in range(page):
            url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i * 20)
      response = requests.get(url, headers=headers).json()['data']
      userData.extend(response)


      df = pd.DataFrame.from_dict(respose)


if __name__ == '__main__':
    get_user_data()