
# 列表推导式
list1 = [i for i in range(0, 10) if i % 2 == 0]
print(list1)


list2 = [(i, j) for i in range(0, 2) for j in range(1, 3)]
print(list2)

# 字典推导式：快速合并列表未字典或者提取字典中目标数据
dict1 = {i: i * i for i in range(1, 5)}
print(dict1)

listA = ['name', 'age', 'gender']
listB = ['Python', 20, '男']
dict2 = {listA[i]: listB[i] for i in range(len(listA))}
print(dict2)

# 提取数据
counts = {'MBP': 100, 'HP': 200, 'Lenovo': 300}
# 提取>=200的数据
computers = {key:value for key, value in counts.items() if value >= 200}
print(computers)

# 集合推导式
list3 = [1, 2, 2, 3]
set1 = {i * i for i in list3}
print(set1)
