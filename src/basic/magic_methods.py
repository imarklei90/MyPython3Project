# coding: utf-8

"""
 Python魔法方法的使用：# 20201124
        1. 构造与初始化
            __init__: 在初始化对象时,定义这个对象的初始值
            __new__: 真正的构造方法,创建对象
                区别:
                    __new__的第一个参数是cls,__init__的第一个参数时self
                    __new__返回值是一个实例对象,可以给所有的实例进行统一的初始化操作,__init__没有返回值,只做初始化操作
                    __new__优先于__init__被调用
                使用场景:
                    1. 可以在__new__实现一个单例类,每次返回同一个实例
                    2. 需要继承内置类(如：int、str、tuple等)时,只能通过new来初始化数据
                    3. 配合’元类‘使用
            __del__: 析构方法,在对象被垃圾回收时调用
                python的垃圾回收方式：引用计数,如果这个实例在del时，还被其它对象引用，就不会触发__del__方法
                使用场景：执行特殊清理逻辑的场景
        2. 类的表示
            __str__: 强调可读性,目标人群是用户,占位符%s调用的是__str__,%r调用的是__repr__
            __repr__: 强调准确性/标准性,目标人群是机器,返回的结果是可执行的,通过eval(repr(obj))可以正确运行
                如果只定义了__str__,那么repr(person)输出:<__main__.Person object at 0x10bee9390>
                如果只定义了__repr__,那么str(person)和repr(person)输出是相同的
                __repr__在表示类时,是一级的,如果只定义__repr__,那么__str__ = __repr__
                __str__展示类时是次级的,如果没有定义__repr__,那么repr(person)将会展示缺省定义
            __unicode__: 类中定义了此方法,在调用unicode(obj)时,此方法将被调用,但是器返回值类型是unicode[很少使用]
            __hash__/__eq__: __hash__返回一个整数,用来表示实例对象的唯一标识,配合__eq__使用,可以判断两个对象是否相等
                使用场景:
                    1. 判断两个对象是否相等,只需要重写__hash__和__eq__即可;
                    2. Set集合中是根据这两个方法进行去重的
            __nozero__: 当调用bool(obj)时,会调用__nozero__方法,返回True或者False
                python3中__nozero__被重命名为__bool__
        3. 访问控制
            __setattr__: 通过[.]设置属性或者setattr(key, value)设置属性时调用
            __getattr__: 访问不存在的属性时调用
            __delattr__: 删除某个属性时调用
            __getattribute__: 访问任意属性或方法时调用
        4. 比较操作
        5. 容器类比较
        6. 可调用对象
        7. 序列化
"""

import datetime

# --------------------------------------构造与初始化----------------------------------

print('--------------------------------------构造与初始化----------------------------------')


class Person(object):

    # 创建对象
    def __new__(cls, name, age,*args, **kwargs):
        print('call __new__')
        return object.__new__(cls, *args, **kwargs)

    # 初始化对象
    def __init__(self, name, age):
        print('call __init__')
        self.name = name
        self.age = age


p1 = Person('张三', 1)
p2 = Person('李四', 2)


class Singleton(object):
    """单例"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MySingleton(Singleton):
    pass


a = MySingleton()
b = MySingleton()

print('a:', a)
print('b:', b)

assert a is b  # True

# --------------------------------------类的表示----------------------------------

print('--------------------------------------类的表示----------------------------------')
a = 'hello'
print(str(a))  # hello
print(repr(a))  # 'hello'


b = datetime.datetime.now()
print(str(b))  # 2020-11-24 10:25:35.822923
print(repr(b))  # datetime.datetime(2020, 11, 24, 10, 25, 35, 822923)


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # 格式化 友好对用户展示
        return 'name: %s, age: %s' % (self.name, self.age)

    def __repr__(self):
        # 标准化展示
        return "Person('%s', %s)" % (self.name, self.age)


person = Person('zhangsan', 20)

# 强调对用户友好
print(str(person))       # name: zhangsan, age: 20
print('%s' % person)     # name: zhangsan, age: 20

# 强调对机器友好 结果 eval 可执行
print(repr(person))	    # Person('zhangsan', 20)
print('%r' % person)     # Person('zhangsan', 20)


class Person(object):
    def __init__(self, uid):
        self.uid = uid

        def __repr__(self):
            return 'Person(%s)' % self.uid

    def __hash__(self):
        return self.uid

    def __eq__(self, other):
        return self.uid == other.uid


p1 = Person(1)
p2 = Person(1)
p1 == p2  # True

p3 = Person(2)
print(set([p1, p2, p3]))  # 根据唯一标识去重输出 set([Person(1), Person(2)])

# --------------------------------------访问控制----------------------------------

print('--------------------------------------访问控制----------------------------------')


class Person(object):

    def __setattr__(self, key, value):
        """属性赋值"""
        if key not in ('name', 'age'):
            return
        if key == 'age' and value < 0:
            raise ValueError()
        super(Person, self).__setattr__(key, value)

    def __getattr__(self, key):
        """访问某个不存在的属性"""
        return 'unknown'

    def __delattr__(self, key):
        """删除某个属性"""
        if key == 'name':
            raise AttributeError()
        super(Person, self).__delattr__(key)

    def __getattribute__(self, key):
        """所有属性/方法调用都经过这里"""
        if key == 'money':
            return 100
        if key == 'hello':
            return self.say
        return super(Person, self).__getattribute__(key)

    def say(self):
        return 'hello'


p1 = Person()
p1.name = 'zhangsan'  # 调用__setattr__
p1.age = 20  # 调用__setattr__
print(p1.name)  # zhangsan
print(p1.age)  # 20

setattr(p1, 'name', 'lisi')  # 调用__setattr__
setattr(p1, 'age', 30)  # 调用__setattr__
print(p1.name)  # lisi
print(p1.age)  # 30

p1.gender = 'male'  # __setattr__中忽略对gender赋值
print(p1.gender)  # gender不存在 所以会调用__getattr__返回unknown

print(p1.money)  # money不存在 在__getattribute__中返回100

print(p1.say())  # hello
print(p1.hello())  # hello 调用__getattribute__ 间接调用say方法

del p1.name  # __delattr__中引发AttributeError

p2 = Person()
p2.age = -1  # __setattr__中引发ValueError

