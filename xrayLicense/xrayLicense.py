
import requests
import sys
import warnings

warnings.filterwarnings("ignore")

if len(sys.argv) != 2:
    print("example:python xrayLicense.py url.txt")
    exit()

proxies = {
    "https":"127.0.0.1:1111",
    "http":"127.0.0.1:1111"
    }

with open(sys.argv[1], encoding = 'utf-8') as f:
    for i in f.readlines():
        i = i.strip()
        print(i)
        if "http" not in i:
            i1 = "http://" + i
            i2 = "https://" + i
            try:
                print("正在发送" + i1 + "\n")
                res1 = requests.get(i1, proxies = proxies, timeout = 10, verify = False)
                if res1:
                    print("发送成功\n")
                else:
                    print("发送失败\n")
                print("正在发送" + i2 + "\n")
                res2 = requests.get(i2, proxies = proxies, timeout = 10, verify = False)
                if res2:
                    print("发送成功\n")
                else:
                    print("发送失败\n")
            except:
                print("发送失败\n")
                continue
        else:
            try:
                print("正在发送" + i + "\n")
                res1 = requests.get(i, proxies = proxies, timeout = 10, verify = False)
                if res1:
                    print("发送成功\n")
                else:
                    print("发送失败\n")
            except:
                print("发送失败")
                continue