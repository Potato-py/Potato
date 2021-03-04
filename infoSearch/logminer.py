#!/usr/bin/python
# -*- coding:utf-8

import os
import sys

sys.path.append('..')
from common.font import *
from common.pubOptimization import *
from common.ipConvertor import *
#防止高频调用导致堵塞，可对某些字段进行存储
Processing=str(Processing())
Information=str(Information())
Detected=str(Detected())
Result=str(Result())
Error=str(Error())

import mmap
import contextlib
import re

try:
    from Evtx.Evtx import FileHeader
    from Evtx.Views import evtx_file_xml_view
except:
    print(Processing+'检测出您未安装python-evtx模块，将替您安装此模块，请稍候……')
    os.system('pip install python-evtx')
    from Evtx.Evtx import FileHeader
    from Evtx.Views import evtx_file_xml_view
from xml.dom import minidom

def Logminer():
    ChooseEvtx=input(bold('请选择的日志序号：		（1.应用日志;2.安全日志;3.系统日志）\n\n')+Input())
    if ChooseEvtx == '1':
        EvtxPath= r"C:\WINDOWS\System32\Winevt\Logs\Application.evtx"
    elif ChooseEvtx == '2':
        EvtxPath= r"C:\WINDOWS\System32\Winevt\Logs\Security.evtx"
    else:
        EvtxPath= r"C:\WINDOWS\System32\Winevt\Logs\System.evtx"

    try:#默认选择&&防止转换失败
        EventID=int(input(bold('请输入提取的事件ID：		（默认：4624）\n\n')+Input()))
    except:
        EventID=4624

    try:
        with open(EvtxPath,'r') as f:
            with contextlib.closing(mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)) as buffer:
                bufferHeader = FileHeader(buffer,0)
                for xml, record in evtx_file_xml_view(bufferHeader):
                    InterestEvent(xml,EventID)
                print(Result+"日志审计完毕……")
    except:
        print(Processing+'提示：由于Python权限低无法读取系统文件，需手动复制文件于当前目录,且文件名改为“log.evtx”！')
        with open(r"./log.evtx",'r') as f:#可写死文件目录结局python权限低导致无法读取系统某些目录
            with contextlib.closing(mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)) as buffer:
                bufferHeader = FileHeader(buffer,0)
                print("")
                print(Processing+"读取成功，正在检查数据……")
                for xml, record in evtx_file_xml_view(bufferHeader):
                    InterestEvent(xml,EventID)
                print(Result+"日志审计完毕……")

# 提取事件ID对应内容
def InterestEvent(xml,EventID):
    xmldoc = minidom.parseString(xml)
    # 获取EventID节点事件ID
    events=xmldoc.getElementsByTagName('Event')
    for evt in events:
        eventId = evt.getElementsByTagName('EventID')[0].childNodes[0].data
        if str(EventID) != eventId:
            continue
        timeCreated = evt.getElementsByTagName('TimeCreated')[0].getAttribute('SystemTime')
        eventRecordID= evt.getElementsByTagName('EventRecordID')[0].childNodes[0].data
        eventData = evt.getElementsByTagName('EventData')
        if eventData!=[]:#剔除无事件数据
            for data in eventData[0].getElementsByTagName('Data'):#遍历Data
                IpAddress=""
                ip=""
                targetUsername=""
                ProcessName=""
                if data.getAttribute('Name')=='IpAddress' and data.childNodes!=[]:
                    IpAddress=data.childNodes[0].data
                if data.getAttribute('Name')=='TargetUserName' and data.childNodes!=[]:
                    targetUsername = data.childNodes[0].data 
                if data.getAttribute('Name')=='ProcessName' and data.childNodes!=[]:
                    ProcessName = data.childNodes[0].data
                if re.search('^\d+',IpAddress):
                    ip = ipConvertor(IpAddress)['addr']
                if IpAddress!="":#过滤无IP信息的内容
                    print(Detected+"ID:{:4}\tTime:{}\tIP:{:10}\tlocation:{:8}\tUser:{:5}\tProcess:{}".format(eventRecordID,timeCreated,IpAddress,ip,targetUsername,ProcessName))
                else:
                    print(Information+"ID:"+eventRecordID)
                    print(Detected+xml)
        else:
            print(Information+"ID:"+eventRecordID+' 无相关数据')
if __name__ == '__main__':
    Logminer()
