# coding:utf-8

import time
import calendar

current_time = time.time()

# 获取当前时间戳
print(current_time)

# 获取当前时间:使用元组封装的9组数字处理时间
localtime = time.localtime(time.time())
print(localtime)

# 获取格式化时间
format_time = time.asctime(time.localtime(time.time()))
print(format_time)

# 格式化日期
t_time =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(t_time)


""
# 获取某月日历
cal = calendar.month(2020, 10)
print(cal)





