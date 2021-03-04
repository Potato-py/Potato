#!/usr/bin/python
# -*- coding:gbk

from optparse import OptionParser  
import queue #队列
import os
import time
import re 
import socket
import threading
import dns.resolver # 安装dnspython模块，来解析dns

que=queue.Queue()    #初始化
portSum=0#需要跑的端口数
runSum=0#跑完的端口数
USAGE='''
Usage:python port_scan.py 127.0.0.1
      python port_scan.py 127.0.0.1 -p 21,135
      python port_scan.py 127.0.0.1 -p 21,138,3306 -n 20
      python port_scan.py -i 127.0.0.1 -p 21,22,80,445 -o lsq.txt
      python port_scan.py -f saomiao.txt -p 21,22,80,445 -o lsq.txt
'''

class Scan(object):  #定义扫描类
    def __init__(self,target,port,theadnum=100,write_file=""):  #构造函数，传入ip，端口，线程，正则判断ip地址
        if re.match(r"^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$",target): #正则匹配IP地址
            self.target = target
        else:
            print("IP地址错误!!!!")
            exit()

        self.port = port  #赋值端口号
        self.theadnum = theadnum #赋值线程赋值
        self.write_file = write_file #判断是否需要写入文件，1为写入，0为不写，默认为0
    
    def startscan(self): #对外接口，给予用户的使用
        global portSum
        if '65535' in self.port:
            portSum=65536
            for i in range(0,65536):
                que.put(i) #放入队列
        else:
            for i in self.port: #端口不是默认65535，则说明可能对方指定端口，循环扫描指定端口
                if int(i)<0 or int(i)>65535:
                    print("请确认端口号正确")
                    exit()
                portSum=len(self.port)
                que.put(i)

        try:
            print("正在扫描%s"%self.target)
            Theadpool = []
            for i in range(0,int(self.theadnum)): #从0到地址池循环多线程
                lsq_th = threading.Thread(target=self.run(),args=())
                Theadpool.append(lsq_th) #将线程放入地址池
            
            for st in Theadpool:
                st.setDaemon(True)
                st.start() #开始跑线程
            que.join() #阻塞线程
            print("扫描完成！！")

        except Exception as a:
            print(a)
        except KeyboardInterrupt:
            print("用户自行退出")
    def run(self):
        while not que.empty():
            port = int(que.get())
            #print(self.ScanPort(port))  #测试ScanPort的返回值
            if self.ScanPort(port):
                banner = self.RecvBanner(port)
                if banner:
                    print("[*]%d------------open\t%s"%(port,banner))
                    if self.write_file != "":
                        with open(self.write_file,"a") as s:
                            s.write("[*]%d------------open\t%s"%(port,banner))
                            s.write("\n")
                else:
                    print("[*]%d------------open\t"%(port))
                    if self.write_file != "":
                        print("开始创建文件")
                        with open(self.write_file,"a") as s:
                            s.write("[*]%d------------open\t%s"%(port,banner))
                            s.write("\n")
            que.task_done()    
            


    def ScanPort(self,port): #扫描端口，预留线程位
        global runSum
        runSum=runSum+1
        print('\r当前进度：{0}{1}%'.format('▉'*int((runSum/portSum)*10)+'▓'*(10-int((runSum/portSum)*10)),round((runSum/portSum)*100,2)), end='')#\r是将光标移到一行的开始，所以\r之后的内容会覆盖掉上次打印的内容，形成动态打印。
        try:
            lsq_sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            lsq_sk.settimeout(0.5)
            # print("ip地址的是：",self.target)
            # print("ip地址的类型是：",type(self.target))
            # print("扫描的端口是：",port)
            # print("端口的类型是：",type(port))
            #target = self.target.replace("\n","")  #消除回车
            
            connect = lsq_sk.connect_ex((self.target,port))
            #print("当前扫描端口为：%s,返回值为：%s"%(port,connect)) #测试扫描值
            if connect ==0:
                return True
            else:
                return False
        except Exception as a:
            print("scanport抛出异常：%s"%a)
            pass
        except KeyboardInterrupt:
            print("用户自行退出")
            exit()
        finally:
            lsq_sk.close()
    
    def  RecvBanner(self,port): #接收返回信息，预留线程位
        try:
            lsq_sk1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            lsq_sk1.settimeout(0.5)
            lsq_sk1.connect((self.target,port))
            lsq_sk1.send("Hello\r\n".encode("utf-8"))
            return lsq_sk1.recv(2048).decode("utf-8")
        except Exception as z:
            print(z)
            pass
        except KeyboardInterrupt:
            print("用户自行退出")
            exit()
        finally:
            lsq_sk1.close()
        


#用户操作界面
parser = OptionParser()

parser.add_option('-p','--port',action="store",type="str",dest="port",help="请输入端口")  #输入指定端口
parser.add_option('-u','--url',action="store",type="str",dest="url",help="请输入域名地址") #输入域名地址
parser.add_option('-i','--ip',action="store",type="str",dest="ipaddress",help="请输入ip地址") #输入ip地址
parser.add_option('-n','--number',action="store",type="int",dest="threadnum",help="请输入线程数")  #输入指定线程
parser.add_option('-f','--filename',action="store",type="string",dest="file",help="请输入一个含有扫描信息的文档") #输入文档扫描
parser.add_option('-o','--write',action="store",type="str",dest="writefile",help="指定存储文件") #将扫描结果存储为文件
#args返回的是所以option未指定的信息
(option,args) = parser.parse_args() #接收ip地址以及字典中的内容

if option.port == None and option.threadnum == None and option.writefile!=None and len(args) == 1: #直接输入ip地址
    scan = Scan(args[0],65535,100,option.writefile)
    scan.startscan()
elif option.port != None and option.threadnum == None and len(args) == 1: #直接输入ip地址和端口号
    port = option.port.split(",")
    scan = Scan(args[0],port)
    scan.startscan()
elif option.port != None and option.threadnum == None and option.writefile!=None and len(args) == 1: #s输入端口和ip地址
    port = option.port.split(",")
    scan = Scan(args[0],port,100,option.writefile)
    scan.startscan()
elif option.port == None and option.threadnum != None and len(args) == 1: #输入ip地址和线程
    scan = Scan(args[0],65535,option.threadnum)
    scan.startscan()
elif option.port != None and option.threadnum != None and len(args) == 1: #输入端口号，ip地址和线程
    port = option.port.split(",")
    scan = Scan(args[0],port,option.threadnum)
    scan.startscan()
elif option.file == None and option.url == None and option.ipaddress != None and option.port == None: #仅输入-i 的ip地址
    scan = Scan(option.ipaddress,65535)
    scan.startscan()
elif option.file == None and option.url == None and option.ipaddress != None and option.port != None: #输入-i，-p
    port = option.port.split(",")
    scan = Scan(option.ipaddress,port)
    scan.startscan()
elif option.file == None and option.url != None and option.ipaddress == None and option.port == None: #输入url域名
    sum = 0 #域名解析出的ip总数
    lsq_url = dns.resolver.query(option.url,'A')
    for i in lsq_url.response.answer: #dns解析后的class
        for j in i.items:
            if j.rdtype == 1: 
                Url = j.address
                sum += 1
    if sum == 1:
        scan = Scan(Url,65535)
        scan.startscan()
    else:
        print("该域名存在域名CDN防护!!")
        parser.print_help()
elif option.file == None and option.url != None and option.ipaddress == None and option.port != None: #输入域名和端口
    port = option.port.split(",")
    sum = 0 #域名解析出的ip总数
    lsq_url = dns.resolver.query(option.url,'A')
    for i in lsq_url.response.answer:
        for j in i.items:
            if j.rdtype == 1: 
                Url = j.address
                sum+=1
            else:
                continue
    if sum == 1:
        scan = Scan(Url,port)
        scan.startscan()
    else:
        print("该域名存在域名CDN防护！！")
        parser.print_help()    
elif option.file != None and option.port !=None and option.writefile != None:
    port = option.port.split(",")
    with open(option.file,"r") as l:
        lsq_read = l.readline()
        while lsq_read:
            if re.match(r"^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$",lsq_read):  #判断是否为ip地址
                read_ip = lsq_read.replace("\n","")
                with open(option.writefile,"a") as q:
                    q.write("开始扫描"+read_ip+"，扫描结果如下：")
                    q.write("\n")
                scan = Scan(read_ip,port,100,option.writefile)
                scan.startscan()
            else:  #扫描dns
                sum = 0 #域名解析出的ip总数
                lsq_url = dns.resolver.query(lsq_read,'A')
                for i in lsq_url.response.answer:
                    for j in i.items:
                        if j.rdtype == 1: 
                            Url = j.address   #没有CDN保护
                            sum+=1
                        else:
                            continue
                if sum == 1:
                    with open(option.writefile,"a") as q:
                        q.write("开始扫描"+Url+"，扫描结果如下：")
                        q.write("\n")
                    scan = Scan(Url,port,100,option.writefile)
                    scan.startscan()
                else:   
                    print("该域名存在域名CDN防护！！")   #有CND保护
            lsq_read = l.readline()
            
else:
    parser.print_help()