#!/usr/bin/python
# -*- coding:utf-8


import time
import sys
import os


sys.path.append('..')
from common.font import *
from common.pubOptimization import *
#防止高频调用导致堵塞，可对某些字段进行存储
Processing=str(Processing())
Information=str(Information())
Detected=str(Detected())
Result=str(Result())
Error=str(Error())


print(Processing+'----------------------------Loading--------------------------------')

try:
    import requests
except:
    print(Processing+'检测出您未安装requests模块，将替您安装此模块，请稍候……')
    os.system('pip install requests')
    import requests

try:
    import base64
except:
    print(Processing+'检测出您未安装base64模块，将替您安装此模块，请稍候……')
    os.system('pip install base64')
    import base64

try:
    import re
except:
    print(Processing+'检测出您未安装re模块，将替您安装此模块，请稍候……')
    os.system('pip install re')
    import re

try:
    import urllib.parse
except:
    print(Processing+'检测出您未安装urllib.parse模块，将替您安装此模块，请稍候……')
    os.system('pip install urllib.parse')
    import urllib.parse

try:
    from scrapy.selector import Selector
except:
    print(Processing+'检测出您未安装scrapy.selector模块，将替您安装此模块，请稍候……')
    os.system('pip install scrapy.selector')
    from scrapy.selector import Selector

try:
    from scrapy.http import HtmlResponse
except:
    print(Processing+'检测出您未安装scrapy.http模块，将替您安装此模块，请稍候……')
    os.system('pip install scrapy.http')
    from scrapy.http import HtmlResponse

try:
    import xlsxwriter,xlrd
except:
    print(Processing+'检测出您未安装xlsxwriter,xlrd模块，将替您安装此模块，请稍候……')
    os.system('pip install xlsxwriter')
    os.system('pip install xlrd')
    import xlsxwriter,xlrd

cookie=''

#单线程同步爬取每翻一页等待2秒防止被Ban

#忽略安全警告
requests.packages.urllib3.disable_warnings()

#获得总页数：
def get_page(key):
    key_base64 = base64.b64encode(key.encode('utf-8')).decode()
    key_base64 = urllib.parse.quote(key_base64)
    url = f'https://fofa.so/result?page=1&qbase64={key_base64}'
    r = requests.get(url=url, headers=headers, verify=False)
    html = r.text
    response = HtmlResponse(html, body=html, encoding='utf-8')
    selector = Selector(response=response)
    for i in [7, 6, 5, 4, 3, 2, 1]:
        path_xpath = f'normalize-space(/html/body/div[1]/div[6]/div[1]/div[2]/div[11]/div[2]/a[{i}])'
        page = selector.xpath(path_xpath).extract()
        page = " ".join(page)
        if page:
            break
    if not page:
        page = 1
    return page
	
#获取查询url链接
def get_url(key, count):
    key_base64 = base64.b64encode(key.encode('utf-8')).decode()
    key_base64 = urllib.parse.quote(key_base64)
    scanurl = f'https://fofa.so/result?page={count}&qbase64={key_base64}'
    return scanurl
	
#通过Xpath定位
def get_data(xpath):
    result = selector.xpath(xpath).extract()
    data = " ".join(result)
    return data


#主功能模块，通过正则获取目标信息：
def scan(target,key):
    filename= './信息收集-'+re.findall('"([^"]+)"', key)[0]+'.xlsx'#创建的表格地址+名字
    global count, page_count, selector
    host = ''
    count += 1
    leave_count = page_count - count - 1
    print(' ')
    print(Information+f'这是第{count}页的内容，还有{leave_count}页的内容：')
    print(' ')
    result = ''
    r = requests.get(url=target, headers=headers, verify=False)
    if headers['Cookie'] in str(r.cookies):
        result = True
    html = r.text
    if '出错了' in html:
        print(' ')
        print(Error+'出错了：-----------------------------------------------------------------------------')
        if '游客使用高级语法只能显示第一页' in html:
            print(Detected+'*********************cookie有误，需要使用登录后的cookie**************************')
        elif '普通用户只能翻5页' in html:
            print(Detected+'***********普通用户只能翻5页,充钱会使你更强，可更换有会员的cookie***************')
        else:
            print(html)
            print(Detected+'***********************某个地方出现了问题，请查看html代码***********************')
        print(Error+'-------------------------------------------------------------------------------------')
        print(' ')
        print(Result+'-------------------------已将以上数据打包至'+filename+'------------------------------------')
        print(' ')
        chooseExit=input(bold('是否继续搜索？y/n \n\n')+Input())
        if chooseExit in ('y','Y','Yes','YES','yes'):
            os.system('cls')
            print('')
            fofa_main()
        else:
            return "isBreak"
    response = HtmlResponse(html, body=html, encoding='utf-8')
    selector = Selector(response=response)
    if result:
        if not os.path.exists(filename):
            workbook = xlsxwriter.Workbook(filename) # 创建xls表
            worksheet = workbook.add_worksheet('sheet1')
        else:
            excelData = xlrd.open_workbook(filename) # 打开原xls表
            excelData.sheet_names()  # 获取xls文件中所有sheet的名称
            table = excelData.sheet_by_index(0) # 通过索引获取xls文件第0个sheet
            nrows = table.nrows  # 获取table工作表总行数
            ncols = table.ncols  # 获取table工作表总列数
            workbook = xlsxwriter.Workbook(filename)  #创建一个excel文件
            worksheet = workbook.add_worksheet()    #创建一个工作表对象
            worksheet.set_column(0,ncols,22)    #设定列的宽度为22像素
            for i in range(nrows):
                worksheet.set_row(i,22)                 #设定第i行单元格属性，高度为22像素，行索引从0开始
                for j in range(ncols):
                    cell_value = table.cell_value(i,j,) #获取第i行中第j列的值
                    if i == 0:
                        format = workbook.add_format({'border':1,'align':'center','bg_color':'cccccc','font_size':13,'bold':True})
                    format.set_align('vcenter')                 #设置单元格垂直对齐
                    worksheet.write(i,j,cell_value,format)      #把获取到的值写入文件对应的行列
        headFormat = workbook.add_format({'border':1,'align':'center','bg_color':'#94C0F1','font_size':13,'bold':True})
        headFormat.set_align('vcenter')
        headings = ['id','title','host','port','ssl_domain','status','language','server','isp'] 
        worksheet.write_row('A1',headings,headFormat)#插入表头部
        for i in range(1, 11):#i每页查出来的条目数
            for j in range(1, 3):
                host_xpath = f'normalize-space(/html/body/div[1]/div[6]/div[1]/div[2]/div[{i}]/div[1]/div[1]/a[{j}])'
                host_result = get_data(host_xpath)
                if host_result:
                    host = host_result
            port_xpath = f'normalize-space(/html/body/div[1]/div[6]/div[1]/div[2]/div[{i}]/div[2]/div[1]/a)'
            title_xpath = f'normalize-space(/html/body/div[1]/div[6]/div[1]/div[2]/div[{i}]/div[1]/div[2])'
            header_xpath = f'normalize-space(/html/body/div[1]/div[6]/div[1]/div[2]/div[{i}]/div[2]/div[2]/div/div[1])'
            certificate_xpath = f'normalize-space(/html/body/div[1]/div[6]/div[1]/div[2]/div[{i}]/div[2]/div[4])'
            server_xpath = f'normalize-space(/html/body/div[1]/div[6]/div[1]/div[2]/div[{i}]/div[1]/div[8]/a)'
            isp_xpath = f'normalize-space(/html/body/div[1]/div[6]/div[1]/div[2]/div[{i}]/div[1]/div[6]/a)'
            port = get_data(port_xpath)
            title = get_data(title_xpath)
            header = get_data(header_xpath)
            certificate = get_data(certificate_xpath)
            server = get_data(server_xpath)
            isp = get_data(isp_xpath)
            if port:
                port = int(port)
            ssl_domain = re.findall(r'(?<=CommonName: ).*(?=Subject Public)', certificate)
            ssl_domain = " ".join(ssl_domain).strip()
            language = re.findall(r'(?<=X-Powered-By: ).*(?=)', header)
            language = " ".join(language).strip()
            if 'PHPSESSID' in header and language == '':
                language = 'php'
            elif 'JSESSIONID' in header and language == '':
                language = 'jsp'
            try:
                ssl_domain = ssl_domain.split(' CommonName: ')[1]
            except:
                ssl_domain = ''
            if not ssl_domain and 'domain=' in header:
                ssl_domain = re.findall(r'(?<=domain=).*(?=;)', header)
                ssl_domain = " ".join(ssl_domain).strip()
                ssl_domain = ssl_domain.split(';')[0]
            try:
                status = int(header.split(' ')[1].strip())
                if status not in [200, 301, 302, 303, 304, 307, 400, 401, 403, 404, 405, 407,
                                  500, 501, 502, 503, 504, 508]:
                    status = ''
            except:
                status = ''
            if port == '' and status == '' and isp == '' and title == '':
                host = ''
            print(Detected+f'id:{i+(count-1)*10}--title:{title}--host:{host}--port:{port}--ssl_domain:{ssl_domain}--status:{status}--language:{language}--server:{server}--isp:{isp}')
            #print('-----------------------')
            rowContent=[i+(count-1)*10,title,host,port,ssl_domain,status,language,server,isp] 
            num=i+1+(count-1)*10
            numIndex='A'+str(num)
            #worksheet.write_row(numIndex, rowContent)
            #num=int(num)
            #worksheet.write(num,0,rowContent)
            format = workbook.add_format({'border':1,'align':'center','bg_color':'cccccc','font_size':13,'bold':True})
            format.set_align('vcenter') 
            worksheet.write_row(numIndex,rowContent,format)
            print(Detected+'        （--------------打印到表格第'+numIndex+'行--------------）')
            print(' ')
            # print(certificate)
            # print(header)
        workbook.close()
    else:
        os.system('cls')
        print(Error+'cookie无效，请重新获取cookie')
        fofa_main()

#主函数模块
def fofa_main():
    global count, page_count,cookie,headers
    count = 0
    print('')
    isCookie=1
    while isCookie:
        cookie= input(bold("请输入您的cookie：      例如：_fofapro_ars_session=d3dd0e36de2a5c491e0746fbc3b41022 \n\n")+Input())
        if not cookie:
            print(Error+'cookie不可为空！\n')
        else:
            isCookie=0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.40',
        'Cookie': cookie       # 请输入你登陆后的session
    }
    print('')
    isKey=1
    while isKey:
        key= input(bold('请输入查询语法：      例如：title="土豆" \n\n')+Input())
        if key.find('"')!=-1:
            isKey=0
        else:
            print(Error+'key语法错误！\n')
    print('')
    print(Processing+'-------------------------searching……-------------------------------')
    page_count = get_page(key)
    page_count = int(page_count) + 1
    for page in range(1, page_count):
        url = get_url(key, page)
        #print('访问url:'+url)
        scans=scan(url,key)
        if scans=="isBreak":
            break
        # time.sleep(2)
		
if __name__ == '__main__':
    fofa_main()