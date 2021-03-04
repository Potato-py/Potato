python-evtx插件存在bug，0时间戳处理异常，需要修改文件C:\Users\lenovo\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\Evtx\BinaryParser.py的处理函数parse_filetime：

def parse_filetime(qword):
    # see http://integriography.wordpress.com/2010/01/16/using-phython-to-parse-and-present-windows-64-bit-timestamps/
    if qword == 0:
        return datetime.min
    try:
        return datetime.utcfromtimestamp(float(qword) * 1e-7 - 11644473600)
    except (ValueError, OSError):
        return datetime.min