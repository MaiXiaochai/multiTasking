# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : __init__.py.
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/11/14 15:47
--------------------------------------
"""
from .mysql_utils import MySQLUtils
from .logger import Logger

from settings import cfg

log = Logger(log_dir=cfg.log_dir, filename=cfg.log_file_name).log
