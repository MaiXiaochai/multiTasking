# -*- encoding: utf-8 -*-

"""
--------------------------------------
@File       : flask_process_pool.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/6 20:20
--------------------------------------
"""
from json import dumps
from math import floor, sqrt
from concurrent.futures import ProcessPoolExecutor

from flask import Flask

app = Flask(__name__)

# 初始化一个全局使用的 进程池
process_pool = ProcessPoolExecutor()


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


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    numbers = [int(x) for x in numbers.split(',')]
    results = process_pool.map(is_prime, numbers)
    return dumps(dict(zip(numbers, results)))


if __name__ == '__main__':
    """
        使用Postman测试：
            1) 不用线程池: 612 ms (顺序运行，三个时间相加)
            2) 使用线程池: 317 ms (并发，最大运行时间)
    """
    app.run(port=9000)
