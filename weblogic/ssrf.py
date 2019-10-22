# -*- coding: utf-8 -*-

import requests

'''
Usage:
    moon.py -u  weblogic http://127.0.0.1:7001
    weblogic version: 10.0.2,10.3.6
    修复：uddiexplorer 删除该目录下的文件，或者做权限配置，禁止对外访问。
    如果可登陆，可在 Setup UDDI Explorer 处获得明确的内网IP
'''
def attack(URL):
    print('[+]开始检测-Weblogic-ssrf-CVE-2014-4210。[+]')

    url = f'{URL}/uddiexplorer/'
    headers = {"Content-Type":'text/xml',
               "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print("存在weblogic-ssrf漏洞页面："+url)
        else:
            print("[-]未发现漏洞页面。")
    except requests.exceptions.ConnectionError:
        print('[-]访问页面出错!')
    print('[+]检测结束-Weblogic-ssrf-CVE-2014-4210。[+]')
    print('\n')


if __name__ == "__main__":
    attack()
