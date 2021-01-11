# -*- encoding: utf-8 -*-

"""
--------------------------------------------
@File       : thread_process_cpu_bound.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/6 19:00
--------------------------------------------
"""
from math import floor, sqrt
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from multi_thread_spider import timer

PRIMES = [112272535095293] * 100


def is_prime(n):
    """
        判断一个数是不是素数
        素数：只能被 1和自身整除的数
    """

    if n < 2:
        return False

    elif n == 2:
        return True

    elif n % 2 == 0:
        return False

    # 开平方，然后从3开始尝试能不能被n整除
    sqrt_n = int(floor(sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False

    return True


@timer
def single_thread():
    """
        单线程
    """
    for number in PRIMES:
        is_prime(number)


@timer
def multi_thread():
    """
        多线程
    """
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


@timer
def multi_process():
    """
        多线程
    """
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


if __name__ == '__main__':
    """
        cost:
            single_thread:  64.32s
            multi_thread:   61.52s
            multi_process:  22.34s
    """
    single_thread()
    multi_thread()
    multi_process()
