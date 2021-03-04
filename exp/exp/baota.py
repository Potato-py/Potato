#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
find ="200 OK"
payload ="/login.php"

def judge(web):
    r = HttpGet(web+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if r[1].find(find)!= -1:
        return 1;
    else:
        return 2;



def main():
    if(judge(url+"/admin_aspcms/_system/AspCms_SiteSetting.asp") == 1):
        res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
        if res[0].find("服务器状态")!= -1:
            print(Result+url+"/login.php 存在admin|admin|存在宝塔弱口令");

    

main()
