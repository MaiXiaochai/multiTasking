# -*- encoding: utf-8 -*-

"""
--------------------------------------
@File       : multi_thread_spider.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/5 21:43
--------------------------------------
"""
from threading import Thread
from time import time, sleep

from demo_ant.spider_simple import urls, craw


def timer(func):
    def inner(*args):
        start = time()
        print(f"{func.__name__}, start")
        func(*args)
        print(f"{func.__name__}, end.")
        end = time()

        cost = end - start
        print(f"{func.__name__} cost: {cost}")

    return inner


@timer
def single_thread():
    for url in urls:
        craw(url)


@timer
def multi_thread():
    threads = []
    for url in urls:
        threads.append(
            Thread(target=craw, args=(url,))
        )

    # 启动每个线程
    for thread in threads:
        thread.start()

    # 等待每个线程结束
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    # 7.3s
    multi_thread()

    # 0.6s
    # single_thread()
    pass
