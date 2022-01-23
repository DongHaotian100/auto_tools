# -*- coding = utf-8 -*-
# @Time : 2021/4/14 16:15
# @Author : D-code
# @File : project_test.py
# @Software : PyCharm


def gen1():
    for i in range(2, 5):
        yield i
        print(i*10)


g1 = gen1()
g = (i*i for i in range(4))
# print(next(g))
print(next(g1))
print(next(gen1()))
a = next(gen1)

if __name__ == '__main__':
    print(next(gen1()))
    print(a)

