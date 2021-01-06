# -*- encoding: utf-8 -*-

"""
--------------------------------------
@File       : flask_thread_pool.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/6 18:21
--------------------------------------
"""
from json import dumps
from time import sleep
from concurrent.futures import ThreadPoolExecutor

from flask import Flask

# 初始化一个全局使用的 线程池
pool = ThreadPoolExecutor()

app = Flask(__name__)


def read_file():
    sleep(0.1)
    return 'file data'


def read_db():
    sleep(0.2)
    return 'db data'


def read_api():
    sleep(0.3)
    return 'api data'


@app.route("/")
def index():
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)

    return dumps({
        'file': result_file.result(),
        'db': result_db.result(),
        'api': result_api.result()
    })


if __name__ == '__main__':
    """
        使用Postman测试：
            1) 不用线程池: 612 ms (顺序运行，三个时间相加)
            2) 使用线程池: 317 ms (并发，最大运行时间)
    """
    app.run()
