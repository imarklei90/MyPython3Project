# coding: utf-8

"""
    url:https://hf.anjuke.com/sale/gaoxinqud/?from=SearchBar
    安居客中合肥高新区的所有二手房信息：反爬

    贝壳找房：
        https://hf.fang.ke.com/loupan/gaoxin8/#gaoxin8
"""

import requests
from requests import Response
from lxml import etree


url = 'https://hf.ke.com/ershoufang/gaoxin8/'


def download(url: str) -> str:
    #response: Response = requests.get(url, params={'from': 'SearchBar'})
    #response: Response = requests.get(url)
    response = requests.request('GET', url)
    if response.status_code == 200:
        return response.text # 文本, response.content返回的是字节码，通过read()获取到的
    return '下载失败'


result = download(url)
#print(result)


def get(url):
    response = requests.get(url, proxies={'https': 'https://123.163.117.239:9999'})
    if response.status_code == 200:
        parse(response.text)
    else:
        raise Exception('请求失败')


def parse(html):
    # 使用xpath进行解析
    root = etree.HTML(html)
    divs = root.xpath('//div[class="clear"]')  # List<Element>
    print(divs)
    for div in divs:
        cover_url = div.xpath('.//img/@src').extract()[0]  # List<String> 提取属性值
        title = div.xpath('.//div[class="VIEWDATA CLICKDATA maidian-detail"]').extract()[0]
        print(f"{cover_url, title}")


if __name__ == '__main__':
    get(url)
