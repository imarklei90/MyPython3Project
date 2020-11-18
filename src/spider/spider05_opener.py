# coding:utf-8

"""
    Handler：
        模拟浏览器，增加不同的handler
        urllib.request.build_opener(handlers)
        urllib.request.HTTPHandler

"""

from urllib.request import HTTPHandler, build_opener
from collections import namedtuple

# 声明类
Response = namedtuple('Response', field_names=['headers', 'code', 'text', 'body', 'encoding'])


def get(url):
    opener = build_opener(HTTPHandler())
    resp = opener.open(url)
    # 返回类对象，带有handlers、code等
    headers = dict(resp.getheaders())
    try:
        encoding = response.headers['Content-Type'].split('=')[-1]
        print('encoding:', encoding)
    except:
        encoding = 'utf-8'
    code = resp.code
    body = resp.read()
    text = body.decode(encoding)
    return Response(headers, code, text, body, encoding)


if __name__ == '__main__':
    response = get('http://www.jd.com')
    print(response.code)
    print(response.encoding)
