# coding: utf-8

import threading
import time

"""
    使用threading模块创建线程
        从threading.Thread继承创建一个新的子类，并实例化后调用start()方法启动线程，即调用run()
"""

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("start a thread:" + self.name)
        # 获取锁，用于线程同步
        thread_lock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        thread_lock.release()


def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            thread_name.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


thread_lock = threading.Lock()
threads = []

# 创建新线程
thread1 = MyThread(1, 'Thread-1', 1)
thread2 = MyThread(2, 'Thread-2', 2)

# 开启线程
thread1.start()
thread2.start()


# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成结束
for t in threads:
    t.join()

print("退出线程")