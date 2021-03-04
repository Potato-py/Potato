#!/usr/bin/python
# -*- coding:utf-8
#文件完整性hash验证
import os
import sys
import hashlib
import json

sys.path.append('..')
from common.font import *
from common.pubOptimization import *
#防止高频调用导致堵塞，可对某些字段进行存储
Processing=str(Processing())
Information=str(Information())
Detected=str(Detected())
Result=str(Result())
Error=str(Error())


#网站目录所有文件列表
path_list=[]
#不做hash效验列（一般指定静态文件）
White_list=['.js','.jpg','.png','.html','.htm']

def GetFile(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:  
            dir=os.path.join(dirpath, dirname)
            path_list.append(dir)
        for filename in filenames:
            file=os.path.join(dirpath, filename)
            if os.path.splitext(file)[1] not in White_list:
                path_list.append(file)
    return path_list

#文件迭代获取数据
def md5sum(file):
    m=hashlib.md5()
    if os.path.isfile(file):
        f=open(file,'rb')
        for line in f:
            m.update(line)
        f.close
    else:
        m.update(file.encode("utf8"))
    return (m.hexdigest())

def Get_md5result(webpath,fileName):
    pathlist=GetFile(webpath)
    md5_file={}
    for file in pathlist:
        md5_file[file]=md5sum(file)
    json_data=json.dumps(md5_file)
    fileObject = open(fileName, 'w')  
    fileObject.write(json_data)  
    fileObject.close()

def load_data(json_file):
    model={}
    with open(json_file,'r') as json_file:
        model=json.load(json_file)
    return model

def Analysis_dicts(dict1,dict2):
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    ret1 = [ i for i in keys1 if i not in keys2]
    ret2 = [ i for i in keys2 if i not in keys1]
    print('')
    print(Result+"可能被删除的文件有:")
    for i in ret1:
        print(i)
    print('')
    print(Result+"新增的文件有:")
    for i in ret2:
        print(i)
    print('')
    print(Result+"可能被篡改的文件有：")
    ret3=list((set(keys1).union(set(keys2)))^(set(keys1)^set(keys2)))
    for key in ret3:
        if key in keys1 and key in keys2:
            if dict1[key] == dict2[key]:
                pass
            else:
                print(key)
 
if __name__ == '__main__':
    fileIndex=1
    isHash=1
    while isHash:
        fileName="result"+str(fileIndex)+".json"
        webpath = input(bold('\n请输入需要检查的目录物理路径：		例：C:\\wwww\ \n\n')+Input()).lower()
        Get_md5result(webpath,fileName)
        dict2=load_data(fileName)
        print("")
        print(Information+"该目录下文件HashJson信息已导入./"+fileName)
        hashChose= input(bold('\n是否需要继续检查其他目录: 		(Y/N): \n\n')+Input()).lower()
        if hashChose=='y':
            fileIndex=fileIndex+1
        else:
            isHash=0

    methodselect= input(bold('\n是否需要检查文件的完整性: 		(Y/N): \n\n')+Input()).lower()
    if methodselect == 'y':
        file=input(bold('\n请输入要比较的哈希json文件路径: 		例：result2.json \n\n')+Input()).lower()
        dict1=load_data(file)
        Analysis_dicts(dict1,dict2)
    elif methodselect == 'n':
        exit()