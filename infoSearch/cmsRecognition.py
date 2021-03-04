#coding=gbk
#!/usr/bin/python

import requests
import zlib
import json

def whatweb(url):
    response = requests.get(url,verify=False)
    #上面的代码可以随意发挥,只要获取到response即可
    #下面的代码您无需改变，直接使用即可
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
        inputData=input('请输入你要识别的网站：		（请填写完整网址，如：http://www.baidu.com）\n\n')
        if not inputData:
            print(Error+'网站不可为空！\n')
        else:
            isUrl=0
    request = whatweb(inputData)
    print('')
    print(u"识别结果")
    print(request.json())