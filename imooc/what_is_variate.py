# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : what_is_variate.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/14 20:57
------------------------------------------
variate：变量
1）Java中的变量类似一个盒子，盒子里能装什么，一开始就固定了
2）Python中的变量类似于一个便利贴（可以贴在 int上，也可以贴在 str上），实质上是一个指针
"""

# # a = 1 的声明过程
# 1. a 贴在1上
# 2. 先生成对象1，然后将便利贴a 贴在 1上
a = 1

# # demo
# out: [1, 2, 3, 4]
# 过程：
# 1) 先生成 [1, 2, 3] 对象
# 2) 把 m贴在 [1, 2, 3] 上
# 3) 把 n贴在 [1, 2, 3] 上
# 4) 操作 n，添加元素4, 因为 m和 n贴的是同一个对象，所以结果 [1, 2, 3, 4]
m = [1, 2, 3]
n = m
n.append(4)
print(n)

ids = f"m 的 id: {id(m)}, n 的 id: {id(n)} | 两个 id{'相等' if id(m) == id(n) else '不等'}"

print(ids)
