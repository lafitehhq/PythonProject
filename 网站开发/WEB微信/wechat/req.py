#__author:  Administrator
#date:  2017/2/13
import requests

form_data = {'Msg': {'Content': 'test', 'Type': 1, 'LocalID': '1486974995.6695778', 'FromUserName': '@1a119658667d4bc105023f927976baf3', 'ClientMsgId': '1486974995.6695778', 'ToUserName': '@@451ba2bcc77b3f14a548fc8ca46a54d4ae4368d670ba71b620863bcfbbb2010e'}, 'Scene': 0, 'BaseRequest': {'Skey': '@crypt_2ccf8ab9_db45072ad19a2c26e6064b5b76ba6f85', 'Sid': '/GjX1pkzj0BVL9FS', 'DeviceID': 'e531777446530354', 'Uin': '981579400'}}
send_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket=6AhlLCiJg%2B289VNxVVCuivEkJLzJjmrPnpPwRFsimpTYwnqMyCmpbDQhWr8vSalq"
response = requests.post(send_url, json=form_data,  headers={
        'Content-Type': 'application/json;charset=UTF-8',
        'Referer': 'https://wx.qq.com/?&lang=zh_CN',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://wx.qq.com',
    })
print(response.text)
