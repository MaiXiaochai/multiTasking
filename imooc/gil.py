# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : gil.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/14 21:13
------------------------------------------
1) GIL: Global Interpreter Lock, 全局解释器锁
2) Python 中的一个线程对应于 C语言中的一个线程
3) GIL 使得同一时刻只有一个线程在一个且只有一个CPU上执行字节码, 无法将多个线程映射到多个CPU上
4) 会根据执行的字节码行数以及时间片释放 GIL；GIL在遇到 I/O操作的时候主动释放
5) 非线程安全

"""
from threading import Thread

total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


thread1 = Thread(target=add)
thread2 = Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)

