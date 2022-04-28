# -*- coding = utf-8 -*-
# @Time : 2022/4/27 23:04
# @Author : D-code
# @File : test.py
# @Software : PyCharm
# 语音播报模块
import pyttsx3

msg = '''今天我，寒夜里看雪飘过,
怀着冷却了的心窝漂远方,
风雨里追赶，雾里分不清影踪,
天空海阔你与我
'''

# 模块初始化
engine = pyttsx3.init()
volume = engine.getProperty('volume')


voices = engine.setProperty('voice', "com.apple.speech.synthesis.voice.satu")


print('准备开始语音播报...')
# 输入语音播报词语
engine.say(msg)
engine.runAndWait()
engine.stop()

