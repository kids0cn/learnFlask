'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-08 19:11:38
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-08 20:47:59
FilePath: /learnFlask/3_鱼书/app/test/jincheng.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

'''
资源是稀缺的，进程是竞争计算机资源的基本单位，线程是进程的执行单位。
单核cpu是假并行，多核cpu是真并行。不停的在不同进程之间切换。
切换进程的开销很大。

# 锁
多线程编程，由于共享资源，所以存在多个线程同时修改一个资源的情况，
也就是线程是不安全的。
细粒度的锁：主动加锁
粗粒度的锁：GIL全局解释器锁，多线程情况下，同一时间只有一个线程执行。
        但是在cpu执行bytecode的时候，有可能执行一半被线程挂起切换了，
        所以GIL只能保障一定程度的安全

但是python可以用多进程，一个是无法共享数据，另一个是开销大，需要进程间通信

# IO密集型的程序，适合用python的多线程，因为IO操作不占用cpu，可以一边执行一边等待

# flask web框架
   webserver决定了开启多少个线程

'''


import threading
import time

def worker():
    print('i am working')
    t = threading.current_thread()
    time.sleep(100)
    print(t.name)


new_t = threading.Thread(target=worker,name="测试")
new_t.start() # 启动线程
# new_t.join() # 等待线程结束

# 启动线程之后，主线程和子线程是并行执行的，主线程不会等待子线程执行完毕。
t = threading.current_thread() # 当前线程
print(t.name)
