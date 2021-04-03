# login
# 2021/3/25
# create by grace hu

import requests
import hashlib
def getMd5(psw):
    md5 = hashlib.md5()
    md5.update(psw.encode("utf-8"))
    return md5.hexdigest()

host = 'http://121.41.14.39:8082/'
loginReqData ={"username": "th0349", "password": getMd5('hxl123')}
loginUrl = f'{host}/account/sLogin'
def login(url, reqData):
    resp = requests.post(url, data=reqData)
    return resp.text

print(login(loginUrl,loginReqData))
