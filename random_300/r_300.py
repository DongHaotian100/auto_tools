# -*- coding = utf-8 -*-
# @Time : 2021/7/29 21:19
# @Author : D-code
# @File : r_300.py
# @Software : PyCharm
import random
import os

# 获取随机数列，参数为语料，想要获得的随机数的个数random_number，返回一个无重复元素且包含random_number个元素的随机整数列表
def get_random_number_list(list_1, random_number):
    line_number = len(list_1)
    random_list = random.sample(range(0, line_number), random_number)
    print(random_list)
    return random_list

# 得到一份剔除空行的TXT文件
def delete_blank_line(text_ole_name, text_new_name):
    with open(text_ole_name, 'r', encoding='utf-8') as f1:
        with open(text_new_name, 'w', encoding='utf-8') as f2:
            for text in f1.readlines():
                if text.split():
                    f2.write(text)
        # print('空格已经剔除')

# 抽取300行训练集语料
def get_train_300():
    delete_blank_line('Summary_raw.txt', 'Summary_new.txt')
    all_lines = []
    with open('Summary_new.txt', 'r', encoding='utf-8') as f1:
        for line in f1:
            all_lines.append(line)
    number_300 = get_random_number_list(all_lines, 300)
    with open('train_300.txt', 'w', encoding='utf-8') as f2:
        for i in number_300:
            f2.write(all_lines[i])
            all_lines[i] = '\n'
    with open('after_300_raw.txt', 'w', encoding='utf-8') as f3:
        for i in range(len(all_lines)):
            f3.write(all_lines[i])
    delete_blank_line('after_300_raw.txt', 'Sum_after_300.txt')  # 生成抽取三百条后的文件，已经剔除空格
    os.remove('after_300_raw.txt')


def get_test_700():
    all_lines = []
    with open('Sum_after_300.txt', 'r', encoding='utf-8') as f1:
        for line in f1:
            all_lines.append(line)
    number_700 = get_random_number_list(all_lines, 700)
    with open('test_700.txt', 'w', encoding='utf-8') as f2:
        for i in number_700:
            f2.write(all_lines[i])
            all_lines[i] = '\n'
    with open('after_700_raw.txt', 'w', encoding='utf-8') as f3:
        for i in range(len(all_lines)):
            f3.write(all_lines[i])
    delete_blank_line('after_700_raw.txt', 'Sum_after_700.txt')  # 生成再抽取700条后的文件，已经剔除空格
    os.remove('after_700_raw.txt')


if __name__ == "__main__":
    get_train_300()
    get_test_700()


