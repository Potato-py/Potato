#!/usr/bin/python
# -*- coding:utf-8

import os
import sys,threading
try:
    import signal
except:
    print('检测出您未安装signal模块，将替您安装此模块，请稍候……')
    os.system('pip install signal')
    import signal
#自定义目录使用sys.path.append(sys.path[0]+r'../common')
#上层目录使用sys.path.append('..')
#当前目录下可忽略添加环境地址
from common.font import *

Lock = threading.Lock()

def Quit(signum, frame):	#解决Ctrl+c报错
    Lock.acquire()#多线程锁
    print ('\n'+Error()+'已主动结束当前模块任务\n')
    sys.exit()
signal.signal(signal.SIGINT, Quit)#主动终止
signal.signal(signal.SIGTERM, Quit)#被迫中止