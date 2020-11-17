# coding:utf-8

"""
    python操作json：
        1) json.dumps():对数据进行编码
        2) json.loads(): 对数据进行解码

"""

import json


data = {
    'no': 1,
    'name': 'python',
    'url': 'https://www.python.org'
}

# 对json数据进行编码
json_str = json.dumps(data)
print('原始数据:', repr(data))
print('json编码数据:', json_str)

# 对python对象进行解码
json_data = json.loads(json_str)
print(json_data['name'])
print(json_data['url'])

# 对文件进行操作
# 写数据
with open('../../../data/json_data_write.json', 'w') as f:
    json.dump(data, f)

# 读数据
with open('../../../data/json_data.json', 'r') as f:
    data = json.load(f)
    print(data)
