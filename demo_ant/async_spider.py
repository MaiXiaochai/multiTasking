# -*- encoding: utf-8 -*-

"""
--------------------------------------
@File       : async_spider.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/6 20:53
--------------------------------------
"""
from time import time
from asyncio import get_event_loop, wait

from aiohttp import ClientSession

from demo_ant.spider_simple import urls


async def async_craw(url):
    """
        异步爬虫
    """
    async with ClientSession() as session:
        print(f"craw url: ", url)
        async with session.get(url) as resp:
            # await: 超级循环不会一直等待，而是切换到下一个url的爬取
            result = await resp.text()
            print(f"craw url: {url}, {len(result)}")


loop = get_event_loop()
tasks = [
    loop.create_task(async_craw(url))
    for url in urls
]

start = time()
loop.run_until_complete(wait(tasks))
end = time()

print(f"Time cost: {end - start}")
