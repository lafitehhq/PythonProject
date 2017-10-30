# # -*- coding: utf-8 -*-

# 加载包

import urllib
import urllib2
import json
import pandas as pd
import numpy as np

# 定义取数据函数
def get_raw_data(x):
    return json.loads(urllib2.urlopen(x).read())

# 提取案例数据网址
url = 'http://future.liangyee.com/bus-api/future/freeSHFE/getDailyKBar?userKey={6FD630C3FBA9493FB2B5FDEDAD538F63&startDate=2016-01-01&symbol=600300&endDate=2016-02-20&type=0}&product=cu&startDate=2017-04-19&endDate=2017-05-25'

# 提取数据
data_day = get_raw_data(url)

# # 转换可数据分析的dataframe格式
# # 定义转换dataframe函数
# all_colnames=['code','open','high','low','close','volume','amount','avp','openvolume','closevolume','opentime','closetime','date']
# def to_dataframe(x):
#     df=pd.DataFrame(columns=all_colnames)
#     for s in x:
#         l=len(df)
#         df.loc[l,:]=s.split(',')
#     for f in['open','high','low','close','volume','amount','avp','openvolume','closevolume']:
#         df[f][df[f]=='']=0
#         df[f]=df[f].astype(float).fillna(0.0)
#     df=df[all_colnames]
#     return df
#
# # 数据转换
# df_day=to_dataframe(data_day)