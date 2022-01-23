# -*- coding = utf-8 -*-
# @Time : 2021/4/14 14:34
# @Author : D-code
# @File : make_pro_into_initial.py
# @Software : PyCharm
# 通过修改本代码可以实现由待替换文本和替换文本的转换
# 比如要把文章中的au to全都改成au_to，就要先利用au to来生成au_to

def change_tool():
    # 加了下划线的
    f1 = open("replace_text.txt", 'r', encoding='utf-8')
    # 空格链接的
    f2 = open("replaced_text.txt", 'w', encoding='utf-8')
    for line in f1:
        f2.write(line.replace('_', ' '))
    f1.close()
    f2.close()


if __name__ == '__main__':
    change_tool()
