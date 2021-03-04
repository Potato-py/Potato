#!/usr/bin/python
# -*- coding:utf-8

import os
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

import socket,threadpool,threading

#使用socket对目标+端口创建连接，如果存在则代表端口开放

ports=[]
runIndex=0
result=[]
isIp=1
while isIp:
    ip=input(bold('请输入扫描的IP：		（例：127.0.0.1）\n\n')+Input())
    if ipaddressData=='':
        print(Error+'IP不可为空！\n')
    else:
        isIp=0
if ip=="":
    ip="127.0.0.1"
def scan_poort(port):
    global runIndex,result
    Lock.acquire()#多线程锁
    runIndex=runIndex+1
    portSum=len(ports)
    print('\r当前进度：{0}{1}%'.format('▉'*int((runIndex/portSum)*10)+'▓'*(10-int((runIndex/portSum)*10)),round((runIndex/portSum)*100,2)), end='')#\r是将光标移到一行的开始，所以\r之后的内容会覆盖掉上次打印的内容，形成动态打印。
    Lock.release()#多线程解锁
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        statu=s.connect_ex((ip,port))
        if statu==0:
            Lock.acquire()#多线程锁
            msg=str(port)+' is open'
            print(Detected+msg)
            result.append(msg)
            Lock.release()#多线程锁
    except:
        pass

def get_port():
    global ports
    inputPort=input(bold('请输入扫描的端口号：		（例如：21-80,445	默认65535）\n\n')+Input())
    if inputPort=="" or inputPort=="65535":
        print(Information+"端口错误/已设置为所有：65535")
        for p in range(65535):
            ports.append(p)
    else:
        portList=inputPort.split(",")
        for portData in portList:
            try:
                intPortData=int(portData)
                ports.append(intPortData)
            except:
                intoMorePort=0
                if "-" in portData:
                    morePort=portData.split("-")
                    try:
                        starPort=int(morePort[0])
                        overPort=int(morePort[1])
                        intoMorePort=1
                        for intPortData in range(starPort,overPort+1):
                            ports.append(intPortData)
                    except:
                        print(Error+"端口输入错误！！！")
                        get_port()
                if intoMorePort==0:
                    print(Error+"端口输入错误！！！")
                    get_port()
    #print(ports)

get_port()

try:    #以防无法转int报错
    ThreadNum=int(input(bold('请输入扫描的线程数：		（默认：100）\n\n')+Input()))
except:
    ThreadNum=100
Lock = threading.Lock()
pool=threadpool.ThreadPool(ThreadNum)
reqs=threadpool.makeRequests(scan_poort,ports)
[pool.putRequest(req) for req in reqs]
pool.wait()
print('\n')
print(Information+bold('---------------扫描完毕，结果如下：----------------'))
for msg in result:
    print(Result+msg)