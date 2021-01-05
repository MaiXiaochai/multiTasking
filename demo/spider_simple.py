# -*- encoding: utf-8 -*-

"""
--------------------------------------
@File       : spider_simple.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/5 21:36
--------------------------------------
"""
from requests import get
from bs4 import BeautifulSoup as BS

urls = (f'https://www.cnblogs.com/#p{i}' for i in range(1, 51))


def craw(url):
    """
        爬取单个页面
    """
    r = get(url)
    return r.text


def parser(html):
    """
        简单的解析网页
        class="post-item-title"
    """
    soup = BS(html, 'html.parser')
    links = soup.find_all("a", class_="post-item-title")
    return [(link['href'], link.get_text()) for link in links]


if __name__ == '__main__':
    url = []
    for i in urls:
        url = i
        break

    for result in parser(craw(url)):
        print(result)

