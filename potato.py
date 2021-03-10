#!/usr/bin/python
# -*- coding:utf-8

import os
import sys,json
import signal

from common.font import *
#防止高频调用导致堵塞，可对返回字段进行存储
Processing=str(Processing())
Information=str(Information())
Detected=str(Detected())
Result=str(Result())
Error=str(Error())

os.system("cls")#Linux使用clear

print(Processing+'正在读取配置文件')
with open(r'.\route.json', 'r',encoding='utf-8') as q:# 读取配置文档 路由json文档
    jsonData=json.load(q)
    routeMenu=jsonData["routeMenu"]#菜单
    routeData=jsonData["routeData"]#菜单选项及其执行命令


#遍历菜单
menu=''
menuList=['\t'+routeMenu[i]+('\t' if (i+1)%3!=0 else '\n\n') for i in range(len(routeMenu))]
for i in menuList:
    menu=menu+i
	
#解决Ctrl+c报错
def Quit_1(signum, frame):#模式1 
    print ('\n'+Error+'已主动结束任务\n')
    sys.exit()
def Quit_2(signum, frame):	#模式2 
    global quitFunc
    quitFunc=Quit_2
    isCls=input('\n'+bold('即将返回主界面，是否清除以上输出：		（ Y/N	【默认y】）\n\n')+Input())
    if isCls.lower()!='n':
        os.system("cls")
    print ('\n'+Processing+'经返回主界面\n')
    signal.signal(signal.SIGINT, Quit_1)#主动终止ctrl+c
    signal.signal(signal.SIGTERM, Quit_1)#被迫中止


def main():
    signal.signal(signal.SIGINT, Quit_1)#主动终止ctrl+c
    signal.signal(signal.SIGTERM, Quit_1)#被迫中止
    startChose=1#开始选择
    noOption=1#无选择菜单选项
    while startChose:
        param=''
        logo_2()
        print ("\n"+Information+"欢迎使用Potato，请选择:\n")
        print(menu)
        action = input("\n"+Input())
        if action == '1':
            logo_1()
            describe()
        elif action in ('9','9.1','9.2'):
            param=" "+input(bold("\n请输入后缀参数:\n\n")+Input())
        for menuData in routeData:
            if action in menuData["id"]:
                signal.signal(signal.SIGINT, Quit_2)#主动终止ctrl+c
                signal.signal(signal.SIGTERM, Quit_2)#被迫中止
                os.system("cls")
                print ("\n"+Processing+"-------------------%s模块加载中---------------------\n"%menuData["describe"])
                os.system(menuData["cmd"]+param)
                noOption=0
                break
            else:
                noOption=1
        if noOption and action!='1':
            os.system(action)
try:
    main()
except Exception as error:
    print(error)