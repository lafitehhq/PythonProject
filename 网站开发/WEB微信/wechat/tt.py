#__author:  Administrator
#date:  2017/2/13

# r = {'k': '%(content)s'}
# import json
# v = json.dumps(r)
# print(v)
# v = v %{'content': '中国'}
# print(v)
# r = {'l': "%(content)s"}
# import json
# v = json.dumps(r)
# print(v)
# v = v %{'content': '中国'}
# print(v)
# b = bytes(v, encoding='utf-8')
# print(b)


import requests


requests.post('url',json={'k1': 'v1'})

requests.post('url',data=bytes("{'k1': 'v1'}",encoding='utf-8'),headers={'application/json'})