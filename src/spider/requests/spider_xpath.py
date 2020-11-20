# coding: utf-8

"""
    古诗文网站：https://www.gushiwen.cn/

"""
import uuid

import requests
from lxml import etree
import pymysql
from utils import header


def itempipeline(item):
    """
        存储数据
        将数据存储到MYSQL中
    """

    # 获取连接
    db = pymysql.connect(host='192.168.28.41', port=3306, user='apt', password='apt1234!@#$',
                         database='test')

    # 获取cursor
    db_cursor = db.cursor()

    # 插入语句
    insert_sql = 'INSERT INTO gushici(id, title, author, content) values(%s, %s, %s, %s)'
    id = item.get('id')
    title = item.get('title')
    author = item.get('author')
    content = item.get('content')

    print(f"{id}, {title}, {author}, {content}")

    values = (id, title, author, content)
    db_cursor.execute(insert_sql, values)

    # 提交操作
    db.commit()

    # 关闭连接
    db_cursor.close()
    db.close()


def parse(text):
    root = etree.HTML(text)
    divs = root.xpath('//div[@class="left"]/div[@class="sons"]')
    item = {}
    for div in divs:
        item['id'] = uuid.uuid4().hex
        item['title'] = div.xpath('.//p[1]//text()')[0]
        item['author'] = " ".join(div.xpath('.//p[2]/a//text()'))
        item['content'] = '<br>'.join(div.xpath('.//div[@class="contson"]/text()'))
        itempipeline(item)


def get(url):
    response = requests.get(url, headers={'User-Agent': header.get_user_agent()})
    if response.status_code == 200:
        parse(response.text)
    else:
        raise Exception('request failed')


if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/shiwens/'
    get(url)

