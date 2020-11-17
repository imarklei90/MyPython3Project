# coding: utf-8

import threading
import time
import queue

"""
    线程优先级队列:Queue
"""

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q= q

    def run(self):
        print("start a thread:" + self.name)
        process_data(self.name, self.q)
        print("退出线程")


def process_data(thread_name, q):
    while not exitFlag:
        queue_lock.acquire()
        if not work_queue.empty():
            data = q.get()
            queue_lock.release()
            print("%s processing %s" % (thread_name, data))
        else:
            queue_lock.release()
        time.sleep(1)


threadLists = ['Thread1', 'Thread2', 'Thread3']
nameLists = ['One', 'Two', 'Three']
queue_lock = threading.Lock()
work_queue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadLists:
    thread = MyThread(threadID, tName, work_queue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queue_lock.acquire()
for word in nameLists:
    work_queue.put(word)
queue_lock.release()

# 等待队列清空
while not work_queue.empty():
    pass

# 通知线程推出
exitFlag = 1

# 等待所有线程完成结束
for t in threads:
    t.join()

print("退出线程")
