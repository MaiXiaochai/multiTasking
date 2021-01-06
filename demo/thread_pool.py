# -*- encoding: utf-8 -*-

"""
--------------------------------------
@File       : thread_pool.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/6 14:27
--------------------------------------
"""
from concurrent.futures import ThreadPoolExecutor, as_completed

# craw
# 用了map的方式
from demo.spider_simple import craw, urls, parser

with ThreadPoolExecutor() as pool:
    htmls = pool.map(craw, urls)

    # 这一步纯粹是为了将url和html对应起来，展示结果的时候看起来比较直观，与线程池无关
    htmls = list(zip(urls, htmls))
    for url, html in htmls:
        print(url, len(html))

# parse
# 用了submit的方式
with ThreadPoolExecutor() as p_pool:
    futures = {}
    for p_url, p_html in htmls:
        future = p_pool.submit(parser, p_html)
        futures[future] = p_url

    # 展示结果
    # for s_future, s_url in futures.items():
    #     print(s_url, s_future.result())

    # 展示结果
    # as_completed
    for future in as_completed(futures):
        url = futures[future]
        print(url, future.result())
