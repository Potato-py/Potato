#!/usr/bin/python
# -*- coding:utf-8

import itertools as its
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

def writeDic(r,maxLength):
    for i in r:
        dataLength=0
        for j in range(len(i)):
            dataLength=dataLength+len(i[j])
        if dataLength<maxLength:
            print(Detected+str(i))
            dic.write("".join(i))
            dic.write("".join("\n"))

#固定字典
# words = "1234568790QWERTYUqwet"
# r =its.product(words,repeat=4) #迭代器中循环4次
# dic = open("pass.txt","w") #w重写,a追加
# writeDic(r,overLength)
# dic.close()

# 生成社工字典
words=[]
wMode='w'#写入方式：w重写,a追加
print(Information+'未知的可跳过……')
shortName=input(bold('1、请输入姓名简拼(小写)：\n\n')+Input())
if shortName:
    words.append(shortName)
    words.append(shortName+"521")
    words.append(shortName+"520")
    words.append(shortName+"1314")
    words.append(shortName+"5201314")
    words.append(shortName+"5211314")
    words.append(shortName+"1314520")
    words.append(shortName+"1314521")
    words.append("521"+shortName)
    words.append("520"+shortName)
    words.append("1314"+shortName)
    words.append("5201314"+shortName)
    words.append("5211314"+shortName)
    words.append("1314520"+shortName)
    words.append("1314521"+shortName)
print('')
name=input(bold('2、请输入姓名全拼(小写)：\n\n')+Input())
if name:
    words.append(name)
    words.append(name+"521")
    words.append(name+"520")
    words.append(name+"1314")
    words.append(name+"5201314")
    words.append(name+"5211314")
    words.append(name+"1314520")
    words.append(name+"1314521")
    words.append("521"+name)
    words.append("520"+name)
    words.append("1314"+name)
    words.append("5201314"+name)
    words.append("5211314"+name)
    words.append("1314520"+name)
    words.append("1314521"+name)
print('')
EnglishName=input(bold('3、请输入英文名：\n\n')+Input())
if EnglishName:
    words.append(EnglishName)
print('')
phoneNum=input(bold('4、请输入手机号：\n\n')+Input())
if phoneNum:
    words.append(phoneNum)
print('')
birthDay=input(bold('5、请输入出生年月日：\n\n')+Input())
if birthDay:
    words.append(birthDay)
print('')
eMile=input(bold('6、请输入邮箱：\n\n')+Input())
if eMile:
    words.append(eMile)
print('')
qq=input(bold('7、请输入QQ账号：\n\n')+Input())
if qq:
    words.append(qq)
print('')
qqName=input(bold('8、请输入网名\绰号：\n\n')+Input())
if qqName:
    words.append(qqName)
print('')
oldPassword=input(bold('9、请输入历史密码：\n\n')+Input())
if oldPassword:
    words.append(oldPassword)
print('')
mateShortName=input(bold('10、请输入配偶简称：\n\n')+Input())
if mateShortName:
    words.append(mateShortName)
    words.append(mateShortName+"521")
    words.append(mateShortName+"520")
    words.append(mateShortName+"1314")
    words.append(mateShortName+"5201314")
    words.append(mateShortName+"5211314")
    words.append(mateShortName+"1314520")
    words.append(mateShortName+"1314521")
    words.append("521"+mateShortName)
    words.append("520"+mateShortName)
    words.append("1314"+mateShortName)
    words.append("5201314"+mateShortName)
    words.append("5211314"+mateShortName)
    words.append("1314520"+mateShortName)
    words.append("1314521"+mateShortName)
print('')
mateName=input(bold('11、请输入配偶全称：\n\n')+Input())
if mateName:
    words.append(mateName)
    words.append(mateName+"521")
    words.append(mateName+"520")
    words.append(mateName+"1314")
    words.append(mateName+"5201314")
    words.append(mateName+"5211314")
    words.append(mateName+"1314520")
    words.append(mateName+"1314521")
    words.append("521"+mateName)
    words.append("520"+mateName)
    words.append("1314"+mateName)
    words.append("5201314"+mateName)
    words.append("5211314"+mateName)
    words.append("1314520"+mateName)
    words.append("1314521"+mateName)
print('')
print(Information+'----------------------------------------------------------------- \n\n')
isOther=1
while isOther:
    any=input(bold('是否还有其他可能含有的字符?  请输入Y/N \n\n')+Input())
    print('')
    if any=='y' or any=='yes' or any=='Y' or any=='YES' or any=='Yes':
        other=input(bold(str(i+12)+'、请输入其他可能含有的字符：\n\n')+Input())
        if other:
            words.append(other)
        print('')
    else:
        isOther=0

#进行系统设置
#print(str(words))
fileName=input(bold('请输入您想导出的密码字典名称：        (默认为：password) \n\n')+Input())
if not fileName:
    fileName='password'
if os.path.exists('./'+fileName+'.txt'):
    wModeChoose=input(bold('!!!!!!“./'+fileName+'”已存在，是否在此文件内容上追加，否则将覆盖 [Y/N] !!!!!\n\n')+Input())
    if wModeChoose=='y' or any=='yes' or any=='Y' or any=='YES' or any=='Yes':
        wMode='a'
    else:
        wMode='w'
    print('')
print(Information+'--------------------将在“./'+fileName+'”生成密码字典--------------------')
print('')

try:    #以防字符串/空格无法转int报错
    maxLength=int(input(bold('请输入密码最长位数：        (默认最长：20)\n\n')+Input()))
except:
    maxLength=20
newWords=[]#用于剔除单个元素超出密码最长位数及重复项
for i in words:
    if len(i)<maxLength and (i not in newWords):
        newWords.append(i)
#print(newWords)

#开始生成
dic = open(fileName+".txt",wMode)
for i in range(1,5):#每5轮组合
    rData =its.combinations(newWords,i)
    writeDic(rData,maxLength)


dic.close()
print(Result+'-----------------------已成功“./'+fileName+'”生成密码字典-----------------------')
