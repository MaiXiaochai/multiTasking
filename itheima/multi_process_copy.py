# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : multi_process_copy.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/11 22:39
------------------------------------------
高并发文件拷贝器
    1) 目标文件夹是否存在，不存在则创建
    2) 遍历源文件夹中所有文件，并拷贝到目标文件夹
    3) 采用多进程实现任务，完成高并发
"""
from time import time
from os import makedirs, listdir
from os.path import exists, join
from shutil import copy
from multiprocessing import Process

SRC_DIR = r'E:\study\python多任务\Python3 核心技术讲解【高级篇】'
DEST_DIR = r'E:\study\python多任务\copy_dest'

if not exists(DEST_DIR):
    makedirs(DEST_DIR)


def copy_file(file, src_dir, dest_dir):
    src_file = join(src_dir, file)
    copy(src_file, dest_dir)


if __name__ == '__main__':
    """
        单进程：23.78s
        多进程：8.06s
    """
    start = time()
    for file_name in listdir(SRC_DIR):
        # copy_file(file_name, SRC_DIR, DEST_DIR)
        sub_process = Process(target=copy_file, args=(file_name, SRC_DIR, DEST_DIR))
        sub_process.start()

    end = time()
    print(f"Time cost: {round(end - start, 2)}s.")
