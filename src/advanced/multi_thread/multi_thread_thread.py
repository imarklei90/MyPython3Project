# coding: utf-8

import _thread
import time


# 为线程定义一个函数
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread_name, time.ctime(time.time())))


# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("thread-1", 2))
    _thread.start_new_thread(print_time, ("thread-2", 3))
except:
    print("Error: can not start thread")

