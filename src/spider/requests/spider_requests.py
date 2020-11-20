# coding: utf-8

"""
    Requests库:

"""

import requests
from PIL import Image
from io import BytesIO

params = {'key':'value', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=params)
print(r.url)
print(r.content)
print(r.status_code == requests.codes.ok)
print(r.json())
print(r.raise_for_status())
requests.request()


p = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(p.headers.get('content-type'))

# 以请求返回的二进制数据创建一张图片
#i = Image.open(BytesIO(r.content))
