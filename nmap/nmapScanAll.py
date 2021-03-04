#!/usr/bin/python
# -*- coding:utf-8

import os
import sys,re

sys.path.append('..')
from common.font import *
from common.pubOptimization import *
#防止高频调用导致堵塞，可对某些字段进行存储
Processing=str(Processing())
Information=str(Information())
Detected=str(Detected())
Result=str(Result())
Error=str(Error())

try:
    import nmap
except:
    print(Processing+'检测出您未安装python-nmap模块（需要已安装nmap），将替您安装此模块，请稍候……')
    os.system('pip install python-nmap')
    import nmap


isHost=1
p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
while isHost:
        host=input('\n'+bold('请输入查询的IP：		（例：127.0.0.1）\n\n')+Input())
        if p.match(host):
            isHost=0
        else:
            print('\n'+Error+'IP格式错误，请重新输入……\n')
print('')
nm = nmap.PortScanner()
print(Processing+'扫描中，请稍等……')
raw_result = nm.scan(hosts=host,arguments ='-v -n -A')
for host,result in raw_result['scan'].items():
    if result['status']['state'] == 'up' :
        print('\n'+Processing+'-'*20 +'Host:' + host + '-'*20)
        print(Result+'操作系统猜测')
        for os in result['osmatch']:
            print(Information+'操作系统为:'+ os['name'] + '准确度为:' + os['accuracy'])
        index =1
        try:
            for port in result['tcp']:
                try :
                    print(Result+ 'TCP服务详情' + '[' + str(index) +']')
                    index=index+1
                    print(Information+'TCP端口号:' + str(port))
                    try:
                        print(Information+'状态:'+ result['tcp'][port]['state '])
                    except :
                        pass
                    try:
                        print(Information+'原因:'+ result['tcp' ][port]['reason'])
                    except :
                        pass
                    try:
                        print(Information+'额外信息:' + result['tcp'][port]['extrainfo'])
                    except :
                        pass
                    try:
                        print(Information+'名字:'+ result['tcp'][port]['name'])
                    except :
                        pass
                    try:
                        print(Information+'版本:'+ result['tcp'][port]['version'])
                    except :
                        pass
                    try:
                        print(Information+'产品:' + result['tcp'][port]['product'])
                    except :
                        pass
                    try:
                        print(Information+'CPE:'+ result['tcp'][port]['cpe'])
                    except :
                        pass
                    try:
                        print(Information+'脚本:'+ result['tcp'][port]['script'])
                    except :
                        pass
                except:
                    pass
        except:
            pass