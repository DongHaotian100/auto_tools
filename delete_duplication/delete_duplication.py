# -*- coding = utf-8 -*-
# @Time : 2021/5/22 15:41
# @Author : D-code
# @File : delete_duplication.py
# @Software : PyCharm

# 解决方案1，直接写一个函数搞定
def delete_duplication():
    a = []
    number = 0
    with open('raw.txt', 'r', encoding='utf-8') as f:
        for line in f:
            number = number + 1
            if line not in a:
                a.append(line)
            else:
                continue
    print(f'原始文本中共有{number}行，除重后剩余{len(a)}行')
    with open('result.txt', 'w', encoding='utf-8') as f:
        for i in range(len(a)):
            f.write(a[i])

# 解决方案2，通过生成器进行剔除，再写入
# 写一个生成器， 可以生成剔除重复后的列表
# key用于传参，可以传数值、函数等参数
def delete(f, key=None):  # 如果被迭代对象中的元素是列表、字典等不可哈希的类型，要设置key参数
    a = []
    for line in f:
        val = line if key is None else key(line)
        if line not in a:
            yield line
            a.append(val)
    return a

# 这个是不更改成可哈希的, 已经可以用了
# 因为我们本次处理的文本列表中的元素是str，是可哈希的
def delete_2(f):
    a = []
    for line in f:
        if line not in a:
            yield line
            a.append(line)
    return a


def delete_duplication2():
    list1 = []
    with open('raw.txt', 'r', encoding='utf-8') as f:
        for i in delete(f):  # 通过生成器进行迭代
            list1.append(i)
        f.seek(0)  # 打开文件只能读取一遍，要把指针重定位到头部才可以第二次遍历
        number = len(f.readlines())  # 获取行数
    with open('result.txt', 'w', encoding='utf-8') as f:
        for i in range(len(list1)):
            f.write(list1[i])
    print(f'原始文本中共有{number}行，除重后剩余{len(list1)}行')

# 尝试整合，发现行数是一样的
def delete_duplication3():
    file_result = open('result.txt', 'w', encoding='utf-8')
    with open('raw.txt', 'r', encoding='utf-8') as f:
        for i in delete(f):  # 通过生成器进行迭代
            file_result.write(i)
        f.seek(0)  # 打开文件只能读取一遍，要把指针重定位到头部才可以第二次遍历
        number_init = len(f.readlines())  # 获取行数
    file_result.close()  # 必须关闭文件，不然后面再以只读模式读取行数时会读出错误数字
    with open('result.txt', 'r', encoding='utf-8') as file_result_read:
        number_end = len(file_result_read.readlines())
    print(f'原始文本中共有{number_init}行，除重后剩余{number_end}行')


if __name__ == "__main__":
    # print(delete_duplication())
    delete_duplication3()

