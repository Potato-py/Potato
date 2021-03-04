#!/usr/bin/python
# -*- coding:utf-8

import os
import csv
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

# 1、读取配置文档中危险函数及描述；
# 2、遍历所有的目录，所有php的文件路径存入数组；
# 2、对数组中的每个php文件进行读取，扫描敏感函数详情且打印；
# 3、写入到csv文件中进行保存；
# 4、统计每个函数出现的次数。

php_files = list()#存放所有php的文件路径
func_num = dict()#存放各个危险函数个数

print(Processing+'正在读取配置文件')
with open(r'.\conf\codeAuditFunc.json', 'r') as q:# 读取配置文档中危险函数及描述
    jsonData=json.load(q)
    funcs=jsonData["funcs"]
    descriptions=jsonData["descriptions"]

for funcsList in funcs:#初始化危险函数个数
    for func in funcsList:
        func_num[func.strip('(').strip(' ').split('($')[0]] = 0
print(Information+'配置文件读取成功\n')
isPath=1
while isPath:
    projectPath=input(bold('请输入项目的目录：		（例：D:\phpstudy_pro\WWW\cms）\n\n')+Input())#r"D:\phpstudy_pro\WWW\cms\xinhu"
    if not projectPath:
        print(Error+'目录不可为空！\n')
    else:
        isPath=0
for root, dirs, files in os.walk(projectPath, topdown=False):#遍历所有php的文件路径
    for name in files:
        file = str(os.path.join(root, name))
        if file.endswith('.php'):
            php_files.append(file)
print(Information+'共发现%d个文件' % len(php_files))
print(Processing+'开始进行内容审计')

filename='./代码审计-'+projectPath.split('\\')[-1]+'.csv'
with open(filename, 'w', encoding='utf-8', newline='') as q:
    csv_writer = csv.writer(q)
    csv_writer.writerow([ 'ID','敏感函数', '漏洞描述','文件路径', '漏洞代码行', '漏洞详情'])
    fileIndex = 0
    funcIndex = 0
    for file in php_files:
        fileIndex = fileIndex+1 
        with open(file, 'r', encoding='UTF-8', errors='ignore') as f:#对生成报告进行操作
            data = f.readlines()
            print(Information+"当前正在扫描%s" % file.split('\\')[-1])
            print(Information+"任务进度%d/%d" % (fileIndex, len(php_files)))
            for aline in data:
                aline = aline.encode('utf-8').decode('utf-8')
                code_line = int((data.index(aline) + 1))  # 代码行数
                funcsListIndex=0#列表一层索引下标
                for funcsList in funcs:#遍历列表一层
                    description=descriptions[funcsListIndex]
                    funcsListIndex=funcsListIndex+1
                    for func in funcsList:
                        clear_func = func.strip('(').strip(' ').split('($')[0]
                        if func in aline:
                            func_num[clear_func] += 1
                            funcIndex = funcIndex+1
                            print(Detected+'第%d行发现敏感函数：%s' % (code_line, func.strip('(').strip(' ').split('($')[0]))
                            csv_writer.writerow([funcIndex,func.strip('(').strip(' ').split('($')[0], description, file, '第'+str(code_line)+'行',  aline])
    csv_writer.writerow(['所涉及敏感函数', '漏洞描述', '共计个数'])
    funcsListIndex=0#列表一层索引下标
    for funcsList in funcs:
        description=descriptions[funcsListIndex]
        funcsListIndex=funcsListIndex+1
        for func in funcsList:
            clear_func = func.strip('(').strip(' ').split('($')[0]
            if func_num[clear_func]!=0:
                csv_writer.writerow([clear_func, description, func_num[clear_func]])
    print(Result+'共计发现敏感函数%d处' % funcIndex)
    print(Information+'报告已生成于：%s' % filename)
