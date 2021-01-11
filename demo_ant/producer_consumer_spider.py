# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : producer_consumer_spider.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/5 22:15
------------------------------------------
"""
from queue import Queue
from threading import current_thread, Thread
from time import sleep
from random import randint

from demo_ant.spider_simple import craw, parser, urls


def do_craw(url_queue: Queue, html_queue: Queue):
    """
        获取从队列获取 url，并将爬取的 html放入 html_queue
    """
    while True:
        url = url_queue.get()
        html = craw(url)
        html_queue.put(html)

        print(current_thread().name, f"{url}", f"url_queue.size={url_queue.qsize()}")
        sleep(randint(1, 2))


def do_parse(html_queue: Queue, fout):
    """
        解析队列中的 html
    """
    while True:
        html = html_queue.get()
        results = parser(html)

        for result in results:
            fout.write(f"{result}\n")

        print(current_thread().name, f"result.size: {len(results)}", f"html_queue.size={html_queue.qsize()}")
        sleep(randint(1, 2))


if __name__ == '__main__':
    file = "spider.log"
    fout = open(file, 'a', encoding='utf8')

    url_queue = Queue()
    html_queue = Queue()

    for url in urls:
        url_queue.put(url)

    # producer threads: 3
    for idx in range(3):
        t = Thread(target=do_craw, args=(url_queue, html_queue), name=f"craw-{idx}")
        t.start()

    # consumer threads: 2
    for idx in range(2):
        t = Thread(target=do_parse, args=(html_queue, fout), name=f"parser-{idx}")
        t.start()

    # fout.close()
