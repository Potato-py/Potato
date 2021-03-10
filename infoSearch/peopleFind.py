#coding=utf-8
#!/usr/bin/python

import re,sys,requests,time,colorama

sys.path.append('..')
from common.font import *
from common.pubOptimization import *
from common.aesEn import PrpCrypt
#防止高频调用导致堵塞，可对某些字段进行存储
Processing=str(Processing())
Information=str(Information())
Detected=str(Detected())
Result=str(Result())
Error=str(Error())
pc=PrpCrypt('potatopotatopota','1234567890123456')

def getData(url):
    try:
        requests.packages.urllib3.disable_warnings()
        response=requests.get(url,timeout=10,verify=False)
        res = response.content.decode('utf-8')
        print(Result+res);
    except:
        print(Error+'请求超时，接口服务器已关闭')

if __name__ == '__main__':
    print('')
    print(Information+'测试阶段只在HW期间打开接口服务器\n')
    print(bold('\n   功能介绍：\n'+"""\033[1m 
	1.通过qq号查绑定的手机号	参数：qq号
	2.通过手机号查绑定的qq		参数：手机号
	3.通过qq号查LOL信息		参数：qq号
	4.通过qq查旧密码		参数：qq号
	5.通过微博ID查手机号		参数：微博号
	6.通过手机号查微博ID		参数：手机号
\033[0m"""))
    isMode=1
    isData=1
    while isMode:
        inputMode=input('\n'+bold('请输入选择的模式序号：		（默认：1）\n\n')+Input())
        if not inputMode:
            print(Error+'模式序号不可为空！\n')
        else:
            isMode=0
    while isData:
        inputData=input('\n'+bold('请输入对应参数：		（例：2438111111）\n\n')+Input())
        if not inputData:
            print(Error+'对应参数不可为空！\n')
        else:
            isData=0
    print('')
    request = getData(pc.decrypt("Nzg5NmFkZGUyYzA4YjQyMDM3YjIxMmY5ODA2NzJlNDYzZTUzODAzZjljZDdiMDM3MmZkOTc1NWIwNjAyODQzNjBkNzdkYTRiYjdjMmM1MjMwNzc5ODMxZDRhZTk3NDBj")+inputMode+'&data='+inputData)