# coding: utf-8

list1 = ['physics', 'chemistry', 200, 'chemistry']

list2 = [1, 2, 3]

# 访问元素的值
print(list1[0])
# 使用切片的方式访问
print(list2[1:2])

# 添加元素
list1.append('haha')
print(list1)

# 删除元素：删除列表中匹配的第一个匹配项
list1.remove('chemistry')
print(list1)