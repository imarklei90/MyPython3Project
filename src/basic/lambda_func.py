# 如果一个函数有一个返回值，并且只有一句代码，可以使用Lambad表达式简化
# 语法：lambda [参数列表]：表达式

def func():
    return 100

# lambda 匿名函数
result = lambda: 100

print(func())

print(result)  # lambda内存地址
print(result())  # lambda 表达式的值

sum = lambda a, b: a + b

print(sum)
print(sum(1, 2))

# -----Lambda的参数形式-----
# 无参数
fn1 = lambda: 100

# 一个参数
fn2 = lambda a: a + 100

# 默认参数
fn3 = lambda a, b, c = 100: a + b + c

# 可变参数 *args
fn4 = lambda *args: args
print(fn4(1, 2, 3))

# 可变关键字参数 **kwargs
fn5 = lambda **kwargs: kwargs
print(fn5(name='python', age=20))

# ----- Lambda的判断 -----
fn6 = lambda a, b: a if a > b else b
print(fn6(10, 2))

# ----- Lambda 按字典顺序排序 -----
students = [
    {'name': 'Mark', 'age': 1},
    {'name': 'Jack', 'age': 30},
    {'name': 'Anna', 'age': 20}
]

# 按照name值升序排序
students.sort(key=lambda x: x['name'])
print(students)

# 按照name值降序排序
students.sort(key=lambda x: x['name'], reverse=True)
print(students)