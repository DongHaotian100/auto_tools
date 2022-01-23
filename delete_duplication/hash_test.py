# -*- coding = utf-8 -*-
# @Time : 2021/5/24 22:51
# @Author : D-code
# @File : hash_test.py
# @Software : PyCharm
"""
在阅读生成器相关知识时，发现了关于hash的一些问题
在此从头到尾努力了解一波
"""

# 首先研究一下什么是可变对象mutable，什么是不可变immutable
# 比如元组是不可变的，因为它没有可以添加元素的操作，列表是可以改变的
# a = (1, 2, 3)
# b = []
# for i in range(2):
#     b.append(i)
# print(b)

# 整数型是不可变的，看看整数型是否是可哈希的
# c = 1
# d = 1
# e = 'str'

# print(id(e))
# print(id(c))
# print(id(d))  # 发现值相同其地址也相同，不同值的地址不相同，可见整数这个不可变对象是可哈希的
# # hash值不是地址值，要通过python内置魔法函数进行计算得出
# print(hash(c))  # 有趣的是魔法函数一般把整数型变量的hash值就是其本身
# print(hash(e))  #

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item
    # print(a)
    # return seen

def dedupe_2(items, key=None):  # 如果被迭代对象中的元素是列表、字典等不可哈希的类型，要设置key参数
    seen = set()
    for item in items:
        # print(type(item))
        # 如果没有设置转化的函数key，就直接等于item，若有转化函数，就等于转化后的类型
        val = item if key is None else key(item)  # 用val获取item值变为tuple不可变类型
        # print(type(val))
        if val not in seen:  # 说白了就是这个in导致的必须可哈希元素才能判断是不是in seen
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [1, 2, 3, 8, 9, 9, 4, 4]
    b = [[1, 2], [3, 4], [1, 2], [6, 9]]
    c = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedupe(a)))
    # print(list(dedupe(b)))
    # key后的匿名函数功能是把dict转化成tuple
    print(list(dedupe_2(c, key=lambda d: (d['x'], d['y']))))





