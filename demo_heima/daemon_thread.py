# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : daemon_thread.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/13 20:22
------------------------------------------
试验守护线程
    结论：主线程会等待所有的线程执行结束再结束
"""
from time import sleep
from threading import Thread


def work():
    for i in range(1, 11):
        print(f"NO.{i}, 工作...")
        sleep(0.2)


if __name__ == '__main__':
    # 设置守护线程方法一:
    sub_thread = Thread(target=work, daemon=True)

    # 设置守护线程方法二: 一定要在 start前设置
    # sub_thread.setDaemon(True)
    sub_thread.start()

    # 主线程等待1s后结束
    sleep(1)
    print("主线程结束")
