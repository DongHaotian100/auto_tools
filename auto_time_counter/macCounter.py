# -*- coding = utf-8 -*-
# @Time : 2022/4/27 21:32
# @Author : D-code
# @File : macCounter.py
# @Software : PyCharm


import pyttsx3
import time

LAST_SECONDS = 30
SHOW_TIME = 3
QA_TIME = 3


# 提醒开始计时
def ppt_begin():
    engine = pyttsx3.init()
    print('%s 分钟展示计时开始' % SHOW_TIME)
    engine.say('%s 分钟展示计时开始' % SHOW_TIME)
    engine.runAndWait()


# 提醒ppt时间结束
def ppt_end():
    time.sleep(LAST_SECONDS)
    print('展示时间结束...')
    engine = pyttsx3.init()
    engine.say('展示时间结束')
    engine.runAndWait()


# 提醒剩余时间
def seconds_last():
    time.sleep(SHOW_TIME*60 - LAST_SECONDS)
    print('还有 %s 秒' % LAST_SECONDS)
    engine = pyttsx3.init()
    engine.say('还有 %s 秒' % LAST_SECONDS)
    engine.runAndWait()


# 提问开始计时
def qa_begin():
    engine = pyttsx3.init()
    engine.say('%s 分钟提问开始' % QA_TIME)
    engine.runAndWait()
    time.sleep(QA_TIME*60)


# 提问结束计时
def qa_end():
    engine = pyttsx3.init()
    engine.say('提问结束')
    engine.runAndWait()
    time.sleep(QA_TIME * 60)


# 主函数
def main():
    ppt_begin()   # 展示计时开始
    seconds_last()    # 提醒剩余时间
    ppt_end()         # 计时结束
    qa_begin()        # 提问计时
    qa_end()          # 提问结束


if __name__ == '__main__':
    main()
