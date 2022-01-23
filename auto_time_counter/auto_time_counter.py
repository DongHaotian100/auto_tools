# -*- coding = utf-8 -*-
# @Time : 2021/4/13 13:16
# @Author : D-code
# @File : auto_time_counter.py
# @Software : PyCharm
# 计时器，可以在结束前某时刻提醒剩余时间，可以在结束时播报提示
import time
import datetime
import win32com.client

# 计时器函数
def auto_count_time():
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    # speaker.Speak("计时开始")
    start = time.time()
    print('开始时刻：%s' % datetime.datetime.now())
    # 设置计时总时长
    minute = 3  # 分钟
    whole = 60*minute
    for i in range(whole):
        print('还有%d秒' % (whole-i))
        time.sleep(1)
        if i == whole-30:
            speaker.Speak("还有30秒")
    speaker.Speak("答辩时间到")
    end = time.time()
    print('结束时刻：%s' % datetime.datetime.now())
    x = end - start
    print('共计%d秒' % x)


if __name__ == '__main__':
    auto_count_time()




