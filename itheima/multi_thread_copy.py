# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : multi_thread_copy.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/13 20:44
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
from threading import Thread

SRC_DIR = r'E:\study\python多任务\2小时玩转python多线程编程'
DEST_DIR = r'E:\study\python多任务\copy_dest'

if not exists(DEST_DIR):
    makedirs(DEST_DIR)


def copy_file(file, src_dir, dest_dir):
    src_file = join(src_dir, file)
    # copy(src_file, dest_dir)

    dest_file = join(dest_dir, file)
    with open(src_file, "rb") as f_in:
        with open(dest_file, 'wb') as f_out:

            while True:
                data = f_in.read(1024)
                if data:
                    f_out.write(data)

                else:
                    break


if __name__ == '__main__':
    """
        单进程：23.78s
        多进程：8.06s
    """

    for file_name in listdir(SRC_DIR):
        # copy_file(file_name, SRC_DIR, DEST_DIR)
        sub_thread = Thread(target=copy_file, args=(file_name, SRC_DIR, DEST_DIR))
        sub_thread.start()
