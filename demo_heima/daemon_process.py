# -*- encoding: utf-8 -*-

"""
--------------------------------------
@File       : daemon_process.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/11 22:32
--------------------------------------
设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程中的代码
"""
from time import sleep
from multiprocessing import Process


def work():
    for i in range(10):
        print('工作中...')
        sleep(0.2)


if __name__ == '__main__':
    # 创建子进程
    work_process = Process(target=work)
    work_process.daemon = True

    # 主进程等1s
    work_process.start()
    sleep(1)
    print('主进程执行完成')
