import re
"""
输入：Category.txt （你直接把word的copy到txt文件就行）
输出：test.txt （自己改一下名字）
"""
dict_core_path = "data/myData/Category.txt"
list_Category = []
with open(dict_core_path) as file:
    next(file)
    line = file.readline()
    while line:
        list_Category.append(re.split(': |; ',line[3:].strip().replace('\n', '')))
        line = file.readline()
for l in list_Category:
    print(l)
input_list = []
for l in list_Category:
    topic = l[0] + '\t'
    for voc in l[1:]:
        input = topic + voc
        print(input)
        input_list.append(input)
with open("data/myData/test.txt","w") as f:
    for instr in input_list:
        f.write(instr + '\n')

