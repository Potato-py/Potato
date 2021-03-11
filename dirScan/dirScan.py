#!/usr/bin/python
# -*- coding:utf-8

import time
import requests
import threadpool
import threading
import sys

sys.path.append('..')
from common.font import *
from common.pubOptimization import *
#防止高频调用导致堵塞，可对某些字段进行存储
Processing=str(Processing())
Information=str(Information())
Detected=str(Detected())
Result=str(Result())
Error=str(Error())


dir=[]
isUrl=1
while isUrl:
    urlHead=input(bold('请输入url：      例如：https://www.baidu.com \n\n')+Input()).strip()
    if not urlHead:
        print(Error+'url不可为空！\n')
    else:
        isUrl=0

def req(dir):           
    try:
        urlTest=urlHead+"/"+dir
        s=requests.get(urlTest,timeout=5)
        if  s.status_code==200:
            Lock.acquire()#多线程锁
            print(Detected+"目录爆破成功："+urlTest)
            Lock.release()#多线程解锁
    except BaseException as error:
        print(Error+error)

if __name__ == '__main__':
    dirPath=input(bold('请输入dir字典：      默认：.\dir.txt \n\n')+Input())
    try:
        file=open(dirPath)
    except:
        print(Information+'输入字典有误，将使用默认字典')
        file=open(r'.\dir.txt',encoding='utf-8')
    for url in file.readlines():
        dir.append(url.rstrip('\n'))
    print(Processing+'正在进行目录爆破……')
    Lock = threading.Lock()
    pool = threadpool.ThreadPool(100)
    requ = threadpool.makeRequests(req,dir) 
    [pool.putRequest(req) for req in requ] 
    pool.wait()
    print(Processing+'目录爆破结束')