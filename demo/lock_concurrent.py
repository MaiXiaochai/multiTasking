# -*- encoding: utf-8 -*-

"""
--------------------------------------
@File       : lock_concurrent.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/6 13:49
--------------------------------------
模拟一个账户多次取钱
"""
from time import sleep

from threading import current_thread, Thread, Lock

lock = Lock()


class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    """
        取钱
    """
    if account.balance >= amount:
        sleep(0.1)
        account.balance -= amount
        print(f"{current_thread().name}, 取钱成功")
        print(f"{current_thread().name}, 余额：{account.balance}")

    else:
        print(f"{current_thread().name}, 取钱失败，余额不足")


def draw_with_lock(account, amount):
    """
        取钱
    """
    with lock:
        if account.balance >= amount:
            sleep(0.1)
            account.balance -= amount
            print(f"{current_thread().name}, 取钱成功")
            print(f"{current_thread().name}, 余额：{account.balance}")

        else:
            print(f"{current_thread().name}, 取钱失败，余额不足")


def demo1():
    """
        未加锁
        t2, 取钱成功
        t2, 余额：200
        t1, 取钱成功
        t1, 余额：-600
    """
    account = Account(1000)
    t1 = Thread(name='t1', target=draw, args=(account, 800))
    t2 = Thread(name='t2', target=draw, args=(account, 800))

    t1.start()
    t2.start()


def demo2():
    """
        加锁
    """
    account = Account(1000)
    t1 = Thread(name='t1', target=draw_with_lock, args=(account, 800))
    t2 = Thread(name='t2', target=draw_with_lock, args=(account, 800))

    t1.start()
    t2.start()


if __name__ == '__main__':
    # demo1()
    demo2()
    pass
