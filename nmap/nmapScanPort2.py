#!/usr/bin/python
# -*- coding:gbk

from optparse import OptionParser  
import queue #����
import os
import time
import re 
import socket
import threading
import dns.resolver # ��װdnspythonģ�飬������dns

que=queue.Queue()    #��ʼ��
portSum=0#��Ҫ�ܵĶ˿���
runSum=0#����Ķ˿���
USAGE='''
Usage:python port_scan.py 127.0.0.1
      python port_scan.py 127.0.0.1 -p 21,135
      python port_scan.py 127.0.0.1 -p 21,138,3306 -n 20
      python port_scan.py -i 127.0.0.1 -p 21,22,80,445 -o lsq.txt
      python port_scan.py -f saomiao.txt -p 21,22,80,445 -o lsq.txt
'''

class Scan(object):  #����ɨ����
    def __init__(self,target,port,theadnum=100,write_file=""):  #���캯��������ip���˿ڣ��̣߳������ж�ip��ַ
        if re.match(r"^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$",target): #����ƥ��IP��ַ
            self.target = target
        else:
            print("IP��ַ����!!!!")
            exit()

        self.port = port  #��ֵ�˿ں�
        self.theadnum = theadnum #��ֵ�̸߳�ֵ
        self.write_file = write_file #�ж��Ƿ���Ҫд���ļ���1Ϊд�룬0Ϊ��д��Ĭ��Ϊ0
    
    def startscan(self): #����ӿڣ������û���ʹ��
        global portSum
        if '65535' in self.port:
            portSum=65536
            for i in range(0,65536):
                que.put(i) #�������
        else:
            for i in self.port: #�˿ڲ���Ĭ��65535����˵�����ܶԷ�ָ���˿ڣ�ѭ��ɨ��ָ���˿�
                if int(i)<0 or int(i)>65535:
                    print("��ȷ�϶˿ں���ȷ")
                    exit()
                portSum=len(self.port)
                que.put(i)

        try:
            print("����ɨ��%s"%self.target)
            Theadpool = []
            for i in range(0,int(self.theadnum)): #��0����ַ��ѭ�����߳�
                lsq_th = threading.Thread(target=self.run(),args=())
                Theadpool.append(lsq_th) #���̷߳����ַ��
            
            for st in Theadpool:
                st.setDaemon(True)
                st.start() #��ʼ���߳�
            que.join() #�����߳�
            print("ɨ����ɣ���")

        except Exception as a:
            print(a)
        except KeyboardInterrupt:
            print("�û������˳�")
    def run(self):
        while not que.empty():
            port = int(que.get())
            #print(self.ScanPort(port))  #����ScanPort�ķ���ֵ
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
                        print("��ʼ�����ļ�")
                        with open(self.write_file,"a") as s:
                            s.write("[*]%d------------open\t%s"%(port,banner))
                            s.write("\n")
            que.task_done()    
            


    def ScanPort(self,port): #ɨ��˿ڣ�Ԥ���߳�λ
        global runSum
        runSum=runSum+1
        print('\r��ǰ���ȣ�{0}{1}%'.format('��'*int((runSum/portSum)*10)+'��'*(10-int((runSum/portSum)*10)),round((runSum/portSum)*100,2)), end='')#\r�ǽ�����Ƶ�һ�еĿ�ʼ������\r֮������ݻḲ�ǵ��ϴδ�ӡ�����ݣ��γɶ�̬��ӡ��
        try:
            lsq_sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            lsq_sk.settimeout(0.5)
            # print("ip��ַ���ǣ�",self.target)
            # print("ip��ַ�������ǣ�",type(self.target))
            # print("ɨ��Ķ˿��ǣ�",port)
            # print("�˿ڵ������ǣ�",type(port))
            #target = self.target.replace("\n","")  #�����س�
            
            connect = lsq_sk.connect_ex((self.target,port))
            #print("��ǰɨ��˿�Ϊ��%s,����ֵΪ��%s"%(port,connect)) #����ɨ��ֵ
            if connect ==0:
                return True
            else:
                return False
        except Exception as a:
            print("scanport�׳��쳣��%s"%a)
            pass
        except KeyboardInterrupt:
            print("�û������˳�")
            exit()
        finally:
            lsq_sk.close()
    
    def  RecvBanner(self,port): #���շ�����Ϣ��Ԥ���߳�λ
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
            print("�û������˳�")
            exit()
        finally:
            lsq_sk1.close()
        


#�û���������
parser = OptionParser()

parser.add_option('-p','--port',action="store",type="str",dest="port",help="������˿�")  #����ָ���˿�
parser.add_option('-u','--url',action="store",type="str",dest="url",help="������������ַ") #����������ַ
parser.add_option('-i','--ip',action="store",type="str",dest="ipaddress",help="������ip��ַ") #����ip��ַ
parser.add_option('-n','--number',action="store",type="int",dest="threadnum",help="�������߳���")  #����ָ���߳�
parser.add_option('-f','--filename',action="store",type="string",dest="file",help="������һ������ɨ����Ϣ���ĵ�") #�����ĵ�ɨ��
parser.add_option('-o','--write',action="store",type="str",dest="writefile",help="ָ���洢�ļ�") #��ɨ�����洢Ϊ�ļ�
#args���ص�������optionδָ������Ϣ
(option,args) = parser.parse_args() #����ip��ַ�Լ��ֵ��е�����

if option.port == None and option.threadnum == None and option.writefile!=None and len(args) == 1: #ֱ������ip��ַ
    scan = Scan(args[0],65535,100,option.writefile)
    scan.startscan()
elif option.port != None and option.threadnum == None and len(args) == 1: #ֱ������ip��ַ�Ͷ˿ں�
    port = option.port.split(",")
    scan = Scan(args[0],port)
    scan.startscan()
elif option.port != None and option.threadnum == None and option.writefile!=None and len(args) == 1: #s����˿ں�ip��ַ
    port = option.port.split(",")
    scan = Scan(args[0],port,100,option.writefile)
    scan.startscan()
elif option.port == None and option.threadnum != None and len(args) == 1: #����ip��ַ���߳�
    scan = Scan(args[0],65535,option.threadnum)
    scan.startscan()
elif option.port != None and option.threadnum != None and len(args) == 1: #����˿ںţ�ip��ַ���߳�
    port = option.port.split(",")
    scan = Scan(args[0],port,option.threadnum)
    scan.startscan()
elif option.file == None and option.url == None and option.ipaddress != None and option.port == None: #������-i ��ip��ַ
    scan = Scan(option.ipaddress,65535)
    scan.startscan()
elif option.file == None and option.url == None and option.ipaddress != None and option.port != None: #����-i��-p
    port = option.port.split(",")
    scan = Scan(option.ipaddress,port)
    scan.startscan()
elif option.file == None and option.url != None and option.ipaddress == None and option.port == None: #����url����
    sum = 0 #������������ip����
    lsq_url = dns.resolver.query(option.url,'A')
    for i in lsq_url.response.answer: #dns�������class
        for j in i.items:
            if j.rdtype == 1: 
                Url = j.address
                sum += 1
    if sum == 1:
        scan = Scan(Url,65535)
        scan.startscan()
    else:
        print("��������������CDN����!!")
        parser.print_help()
elif option.file == None and option.url != None and option.ipaddress == None and option.port != None: #���������Ͷ˿�
    port = option.port.split(",")
    sum = 0 #������������ip����
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
        print("��������������CDN��������")
        parser.print_help()    
elif option.file != None and option.port !=None and option.writefile != None:
    port = option.port.split(",")
    with open(option.file,"r") as l:
        lsq_read = l.readline()
        while lsq_read:
            if re.match(r"^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$",lsq_read):  #�ж��Ƿ�Ϊip��ַ
                read_ip = lsq_read.replace("\n","")
                with open(option.writefile,"a") as q:
                    q.write("��ʼɨ��"+read_ip+"��ɨ�������£�")
                    q.write("\n")
                scan = Scan(read_ip,port,100,option.writefile)
                scan.startscan()
            else:  #ɨ��dns
                sum = 0 #������������ip����
                lsq_url = dns.resolver.query(lsq_read,'A')
                for i in lsq_url.response.answer:
                    for j in i.items:
                        if j.rdtype == 1: 
                            Url = j.address   #û��CDN����
                            sum+=1
                        else:
                            continue
                if sum == 1:
                    with open(option.writefile,"a") as q:
                        q.write("��ʼɨ��"+Url+"��ɨ�������£�")
                        q.write("\n")
                    scan = Scan(Url,port,100,option.writefile)
                    scan.startscan()
                else:   
                    print("��������������CDN��������")   #��CND����
            lsq_read = l.readline()
            
else:
    parser.print_help()