# coding:utf-8

# python连接redis

import redis
from redis import ConnectionPool

"""
    redis模块提供了两个类：
        StrictRedis:实现大部分官方的命令
        Redis:是StrictRedisd子类，用于向后兼容旧版本
"""

# 连接Redis:decode_responses设置为True，取出的结果是字符串，否则是字节
# r_inst = redis.Redis(host='192.168.28.48', port=6379, db=0, decode_responses=True)
# print(r_inst)
# print(r_inst.get("k1"))
# print(type(r_inst.get("k1")))

# 连接池
pool = ConnectionPool(host='192.168.28.48', port=6379, db=0)
redis_pool_inst = redis.Redis(connection_pool=pool)
print(redis_pool_inst)

# 设置key的过期时间
redis_pool_inst.set("K", "V", "3")
