#!/usr/bin/python
# -*- coding:utf-8

import os,re
import json
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

#获取所有EXP脚本
filesNameList=[]
for root, dirs,files in os.walk('./exp/'):
    filesNameList=files
	
#配置全局url
isUrl=1
p=re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
while isUrl:
    url=input(bold('请输入全局url：		（例：http://www.baidu.com）\n\n')+Input())
    if p.match(url):
        isUrl=0
    else:
        print('\n'+Error+'url格式错误，请重新输入……\n')

#扫描所有EXP脚本
print('\n'+Processing+'正在扫描中，请稍候……\n')
[os.system('cd ./exp && python "./'+filesName+'" '+url) for filesName in  filesNameList]
print('\n'+Result+'扫描完毕！\n')