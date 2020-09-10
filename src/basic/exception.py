# Python Exception

while True:
    try:
        x = int(input("input a number: "))
        break
    except ValueError:
        print("not a valid number...")

    
import sys

try:
    f = open("file")
    s = f.readline()
    i = int(s/strip())
except OSError as err:
    print("OS Error: ".format(err))
except ValueError:
    print("Value Error")
except:
    print("Unexpected Error: ", sys.exc_info()[0])
    # 允许指定强制发生的异常, 这个参数必须是一个异常实例,或者是一个异常类,
    # raise ValueError
    
    # 若需要确定是否引发了异常但不打算处理,可以使用raise重新引发异常
    raise 
else:  # 可选的else语句,必须放在所有的except语句之后
    print("other logoic")
finally: # try子句结束前的最后一项任务被执行
    pass

# 自定义异常类
class Error(Exception):
    # 异常的基类
    pass

class InputError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

