"""
Python 模块：
    是一个Python文件，以.py结尾，包含了Python对象定义和Python语句；能定义函数、类、变量，也可以包含可执行的代码

    1. 导入模块
        import 模块名
        from 模块名 import 模块
        from 模块名 import *
        import 模块名 as 别名
        from 模块名 import 功能名 as 别名

    2. 使用模块
        # __name__是系统变量，是模块的标识符，只有在当前文件中调用该函数，是自身模块的值：__main__,
        其它导入的文件内不符合该条件，是当前模块的名字，则不会执行函数调用
        if __name__ == '__main__':
            func()

    3. 模块定位顺序
        Python解释器对模块位置的搜索顺序：
            1. 当前目录
            2. 如果不在当前目录，Python则搜索在Shell变量PYTHONPATH下的每个目录
            3. 如果都找不到，Python会查看默认路径，UNIX下，默认路径一般为：/usr/local/lib/python/
        模块搜索路径存储在system模块的sys.path变量中，变量包含当前目录，PYTHONPATH和由安装过程决定的默认目录
        注：
            自己的模块名不能和已有的模块重名，否则无法使用
            使用 from 模块名 import 功能的时候，如果功能名字重复，调用到的是最后定义或者导入的功能

    4. __all__列表：控制导入行为
        如果一个模块文件中有__all__变量，当使用 from xx import * 时，只能导入这个列表的元素

Python 包：
    1. 包将有联系的模块组织在一起，即放到同一个文件夹下，并且在这个文件夹中创建一个名字为__init__.py的文件，这个文件夹就称为包
    2. 导入包
        方法一：import 包名.模块名
            包名.模块名.目标
        方法二：必须在__init__.py文件中添加__all__=[],控制允许导入的模块列表
            from 包名 import *
            模块名.目标
"""