# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : self_examination.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/14 20:38
------------------------------------------
todo: 未完
Python自省
自省：通过一定的机制查询到对象的内部结构
"""


class Person:
    name = 'person'


class Student(Person):
    def __int__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student()
    print(user.__dict__)
    print(user.name)
