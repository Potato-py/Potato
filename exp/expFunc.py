#!/usr/bin/python
# -*- coding:utf-8

import os,re
import json
import sys,requests,ast

sys.path.append('../../')
from common.font import *
from common.pubOptimization import *
#防止高频调用导致堵塞，可对某些字段进行存储
Processing=str(Processing())
Information=str(Information())
Detected=str(Detected())
Result=str(Result())
Error=str(Error())

def headDict(headers):
    headList=re.split('[:\r\n]',headers)
    for headData in headList:
        headers=headers.replace(headData,'\"'+headData.strip()+'\"')
    headers=headers.replace('rv":"','rv:')
    headers='{'+headers+'}'
    return ast.literal_eval(headers)

def HttpGet(urlPoc,headers):
    try:
        requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
        headersDict=headDict(headers)
        response=requests.get(urlPoc,headers=headersDict,timeout=10,verify=False)
        return [response.content.decode('utf-8'),str(response.headers)]
    except:
        print(Error+'{} 请求超时'.format(urlPoc))
        return ['','']
def HttpPost(urlPoc,data,headers):
    try:
        requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
        headersDict=headDict(headers)
        response=requests.post(urlPoc,data=data,headers=headersDict,timeout=10,verify=False)
        return [response.content.decode('utf-8'),str(response.headers)]
    except:
        print(Error+'{} 请求超时'.format(urlPoc))
        return ['','']