# coding: utf-8

"""
    Python连接MongoDB
"""

import pymongo

# 创建一个mongodb的连接
mongo_client = pymongo.MongoClient(host='192.168.28.48', port=27017)
#print(mongo_client)

#print(mongo_client.list_databases())

print(mongo_client.list_database_names())

# 创建db
my_db = mongo_client['testdb']

# 创建collection
my_coll = my_db['test']

# 创建document
mydict = {'name':'Google', 'url':'https://google.com'}

# 添加数据
#my_coll.insert_one(mydict)

# 查询文档
data = my_coll.find_one()
print(data)

# 修改文档
my_query = {'name':'Google'}
new_values = {'$set': {'name':'GOOGLE'}}
my_coll.update_one(my_query, new_values)

# 删除文档
delete_query = {'name': 'GOOGLE'}
my_coll.delete_one(delete_query)

# 删除集合
my_coll.drop()