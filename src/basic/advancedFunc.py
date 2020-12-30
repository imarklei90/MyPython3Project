# 高阶函数： 将函数作为参数传入到另一个函数

def add_num(a, b, f):
    return f(a) + f(b)

print(add_num(1, 2, abs))

print(add_num(1.1, 1.5, round))

# map(func, list),将传入的函数变量func作用到list变量的每个元素中，并将结果组成新的列表(python2)/迭代器(python3)

list1 = [1, 2, 3]


def func1(x):
    return x ** 2

print(list(map(func1, list1)))


# reduce(func, list), func必须有两个参数，每次func计算的结果继续和序列的下一个元素做累积计算
import functools

list2 = [1, 2, 3, 4, 5]


def func2(x, y):
    return x + y

print(functools.reduce(func2, list2))

# filter(func, list), 用于过滤序列，过滤掉不符合条件的元素，返回一个Filter对象

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func3(x):
    return x % 2 == 0

print(list(filter(func3, list3)))

