# coding:utf-8

dict = {'name': 'zhangsan', 'age': 123}

#print(dict)

#print(dict['name'])

# 修改
dict['name'] = 'lisi'
dict['age'] = 2

#print(dict)

# 删除
#del dict['age']
#print(dict)

# 清空
#dict.clear()
#print(dict)

# 输出key
for i in dict:
    print(i)

# 同时输出key、value
for k, v in dict.items():
    print(f'{k, v}')