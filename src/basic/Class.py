"""
    1. namespace:一个从名字到对象的映射,不同命名空间中的名称之间绝对没有关系
        在不同时刻创建的命名空间拥有不同的生存期,包含：
            存放内置函数的集合：在Python解释器启动时创建的,永远不会被删除,存放在buintins模块中  
            模块中的全局名称：在模块定义被读入时创建
            函数调用中的局部名称：在函数被调用时创建,并在函数返回或者抛出一个不在函数内部处理的错误时被删除
    2. 作用域：是一个命名空间可直接访问的Python程序的文本区域
        作用域被静态确定,但是被动态使用,三个命名空间可以被直接访问的嵌套作用域：
            最先搜索的最内部作用域包含局部名称
            从最近的封闭作用域开始搜索的任何封闭函数的作用域包含非局部名称,也包含非全局名称
            倒数第二个作业域包含当前模块的全局名称
            最后搜索的最外面的作用域是包含内置名称的命名空间

    3. 类
        定义：
            class className:
                statement
                ...
                statement
        类对象：
            支持的操作：
            属性引用：
                使用Python中所有属性引用所使用的标准语法:obj.name
            实例化：
                使用函数表示法：x= MyClass(),返回该类的一个新实例的不带参数的函数
                实例化操作会创建一个空对象
                __init()__:实例化时被调用,用于对实例进行初始化
        实例对象：
            唯一操作：属性引用,包含数据属性、方法
        方法对象：
        类和实例变量：
        
    4. 继承
        定义：
            class DerivedClassName(BaseClassName):
                statement
                ...
                statement
        在派生类的重载方法中调用基类的方法：
            BaseClassName.methodName(self,arguments)
        可用于继承机制的Python内置函数：
            isinstance(): 检查一个实例的类型:isinstance(obj,int)仅会在obj.__class__为int或某个派生自int的类时为True
            issubclass(): 检查类的继承关系: issubclass(bool,int)为True,因为bool是int的子类,issubclass(float,int)为False
        多重继承：
            定义：
                class DevivedClass(Base1, Base2, Base3):
                    statement
                    ...
                    statement
    
    5. 私有变量
    6. 迭代器
    7. 生成器：用于创建迭代器
        示例：
            def reverse(data):
                for index in range(len(data) -1, -1, -1)
                    yield data[index]

"""