#!/usr/bin/python
# -*- coding:utf-8

import requests
from bs4 import BeautifulSoup
import re

def ipConvertor(ip):
    url = 'http://whois.pconline.com.cn/ipJson.jsp?ip='+ip+'&json=true'
    data = {'ip': ip}
    r = requests.get(url)
    resoul = eval(r.text)#使用eval()可将字符串转换成字典
    pro=resoul['pro']
    city=resoul['city']
    region=resoul['region']
    addr=resoul['addr']
    regionNames=resoul['regionNames']
    err=resoul['err']
    resoulDict={'pro':pro,'city':city,'region':region,'addr':addr,'regionNames':regionNames,'err':err}
    return  resoulDict
ipConvertor("124.202.168.122")