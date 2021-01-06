# -*- encoding: utf-8 -*-

"""
--------------------------------------
@File       : async_spider.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/6 20:53
--------------------------------------
"""
from aiohttp import ClientSession


async def async_craw(url):
    """
        异步爬虫
    """
    async with ClientSession() as session:
        async with session.get(url) as resp:
            # await: 超级循环不会一直等待，而是切换到下一个url的爬取
            result = await resp.text()
