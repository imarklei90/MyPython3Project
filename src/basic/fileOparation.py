# File Operations

# first param: 文件名
# second param: 文件的使用方式,取值为：r -> 只读, w -> 只写（已存在的同名文件会被删除）, a -> 打开文件以追加内容, r+ -> 打开文件进行读写; 默认值为r 
# f = open("mypython3project/data", "w")

# 处理文件对象，建议使用 with关键字，表示当子句体结束后文件会正确关闭，即使在某个时刻产生了异常
with open("F:/MyProjects/MyPython3Project/data/data") as f:
    # 读文件操作 : 如果文件到达末尾, f.read()将返回一个空的字符串('')
    read_data = f.read() 
    # 从文件中读取一行数据：\n留在字符串的末尾，如果文件不以\n结尾，则文件的最后一行被省略；readline()返回一个空字符串表示文件已经达到末尾，
    line_data = f.readline
f.close

# 循环读取文件
with open("F:/MyProjects/MyPython3Project/data/data") as f:
    for line in f:
        print(line, end="")

# 以列表的方式读取文件中的所有行
with open("f:/MyProjects/MyPython3Project/data/data") as f:
    list_data = f.readlines
    print(list_data)

# 写文件: 打开文件时先设置文件的执行权限为w,表示可写
with open("f:/MyProjects/MyPython3Project/data/writedata", "w") as f:
    f.write("data from python")

# 处理JSON文件
import json
json.dumps([1, "a", "b"])
print(json)