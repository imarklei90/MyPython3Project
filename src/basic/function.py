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

print()
