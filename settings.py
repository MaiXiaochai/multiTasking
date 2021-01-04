# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : setting.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/11/14 16:10
--------------------------------------
"""
from os.path import dirname


class BaseConfig:
    """
    基础配置
    """
    db_info = {
        "user": "truck",
        "passwd": "T_123456",
        "host": "localhost",
        "port": 3306,
        "db": "bjleardock"
    }

    # ================================[ log设置 ]================================
    # log 保存目录的名称(以项目的根目录作为根目录)
    log_dir = "logs"

    # log 文件名
    log_file_name = "multitasking.log"

    base_dir = dirname(dirname(dirname(__file__)))
    log_dir = f"{base_dir}/{log_dir}"


cfg = BaseConfig()
