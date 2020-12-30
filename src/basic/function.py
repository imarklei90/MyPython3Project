# coding:utf-8

var1 = 2


def method(str):
    """
        这是一个简单的方法
    :return:
    """
    print(str)
    global var1
    var1 = var1 + 100

    return str + "AAAA"

# lambda函数
sum = lambda arg1, arg2: arg1 + arg2


# 定义带有返回值类型的函数
def method2(s: str) -> str:
    return s



if __name__ == '__main__':
    retValue = method("python")
    print(retValue)
    result = sum(1,2)
    print(result)

    # 调用带有返回值类型的函数
    result2 = method2('aaa')
    # 可以调用str类型的所有方法
    print(result2.upper())


print("---------------------修改全局变量的值----------------------")

# 全局变量
a = 100


def A():
    print(a)


def B():
    # 声明变量a为全局变量
    global a
    a = 200
    print(a)


A()
B()

print(a)


print("---------------------函数参数----------------------")
# 位置参数
def user_info(name, age, gender):
    print(f'姓名：{name}, 年龄：{age} , 性别：{gender}')

user_info("张三", 20, '男')

# 关键字参数: 函数调用时，如果有位置参数，位置参数必须在关键字参数的前面，但是关键字参数之间没有顺序关系
user_info(age=100, gender='女', name='zhangsan')

# 缺省参数:位置参数必须在缺省参数的前面
def user_info_default(name, age, gender='男'):
    print(f'姓名:{name}, 年龄:{age}, 性别：{gender}')

user_info_default('zhangsan', 12)

# 不定长参数：都是组包的过程，包括；
# 包裹位置传递: 所有的参数被args收集，根据传进参数的位置合并为一个元组
# 包裹关键字传递: 所有的参数被kwargs收集，根据传进的参数合并为一个字典


def user_infos(*agrs):
    print(agrs)

user_infos(1)
user_infos(1,2,3)

def user_infos2(**kwargs):
    print(kwargs)

user_infos2()
user_infos2(name='zhangsan', age=10)

