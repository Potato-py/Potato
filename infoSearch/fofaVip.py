import requests
import json
import base64
import re
import sys

sys.path.append('..')
from common.font import *
from common.pubOptimization import *
#防止高频调用导致堵塞，可对某些字段进行存储
Processing=str(Processing())
Information=str(Information())
Detected=str(Detected())
Result=str(Result())
Error=str(Error())

def main():
    print(Processing+'正在读取配置文件')
    with open(r'.\conf\fofaUser.json', 'r') as q:# 读取配置文档
        jsonData=json.load(q)
        email=jsonData["userVip"][0] #email
        key=jsonData["userVip"][1] #key
    isTar=1
    while isTar:
        targetsrting=input(bold('请输入查询语法：      例如：title="土豆" \n\n')+Input()) #搜索关键字
        if targetsrting.find('"')!=-1:
            isTar=0
        else:
            print(Error+'key语法错误！\n')
    target=base64.b64encode(targetsrting.encode('utf-8')).decode("utf-8")
    page="1" #翻页数
    try:
        size=str(int(input(bold('请输入查询条目数：      默认：10000 \n\n')+Input()))) #每页返回记录数
    except:
        size="10000"
    url="https://fofa.so/api/v1/search/all?email="+email+"&key="+key+"&qbase64="+target+"&size="+size
    resp = requests.get(url)
    data_model = json.loads(resp.text)

    data_url=[]
    filename= './信息收集url-'+re.findall('"([^"]+)"', targetsrting)[0]+'.txt'#创建的表格地址+名字
    save=open(filename,'w+')

    for i in data_model['results']: #取结果列表
        for j in i[0:1]: #取结果列表中的每个列表的url,需要IP则改为[1:2]
            data_url.append(j)

    for i in data_url:
        save.write(i+"\n")

    save.close()
    print("")
    print(Result+'-------------------------已将以上数据打包至'+filename+'------------------------------------')


if __name__ == '__main__':
    main()