#coding=gbk
#!/usr/bin/python

import requests
import zlib
import json,sys

sys.path.append('..')
from common.font import *
from common.pubOptimization import *
#��ֹ��Ƶ���õ��¶������ɶ�ĳЩ�ֶν��д洢
Processing=str(Processing())
Information=str(Information())
Detected=str(Detected())
Result=str(Result())
Error=str(Error())

def whatweb(url):
    response = requests.get(url,verify=False)
    #����Ĵ���������ⷢ��,ֻҪ��ȡ��response����
    #����Ĵ���������ı䣬ֱ��ʹ�ü���
    whatweb_dict = {"url":response.url,"text":response.text,"headers":dict(response.headers)}
    whatweb_dict = json.dumps(whatweb_dict)
    whatweb_dict = whatweb_dict.encode()
    whatweb_dict = zlib.compress(whatweb_dict)
    data = {"info":whatweb_dict}
    return requests.post("http://whatweb.bugscaner.com/api.go",files=data)

if __name__ == '__main__':
    print('')
    print('')
    isUrl=1
    while isUrl:
        inputData=input('��������Ҫʶ�����վ��		������д������ַ���磺http://www.baidu.com��\n\n'+Input())
        if not inputData:
            print(Error+'��վ����Ϊ�գ�\n')
        else:
            isUrl=0
    request = whatweb(inputData)
    print('')
    print(Information+"ʶ������")
    print(Result+str(request.json()))