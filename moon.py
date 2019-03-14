# -*- coding: utf-8 -*-
import sys
import tomcat.Main_tomcat
import fckeditor.Main_fckeditor
import ipquery.Main_ipquery
import weblogic.Main_weblogic
import iis.Main_iis
import docker_vuln.Main_docker
import redis_vuln.Main_redis
import zabbix_vuln.Main_zabbix
import navigate_vuln.Main_navigate
import gatepass_vuln.Main_gatepass
import ipq.Main_ipq
import spring_vuln.Main_spring
import jboss.Main_jboss
import kindeditor.Main_kindeditor
import durpal.Main_durpal
import bf_dicts.Main_bf

if __name__ == "__main__":

    #使用说明
    if len(sys.argv) < 3 or sys.argv[1]=="-h":
        print('''
漏洞检测：
userage: python -u module http://xx.xx.xx.xx:xx
modul:  tomcat fck weblogic iis docker redis zabbix navigate gatepass
IP归属查询：
userage: python -u ip www.xxxxx.com/xx.xx.xx.xx
modul：ip ipq
        ''')

    #漏洞利用
    elif sys.argv[1] == '-u':
        # 处理url末尾可能存在的/
        if sys.argv[3][-1] != '/':
            pass
        else:
            sys.argv[3] = sys.argv[3][0:-1]
        print('[+]检测地址:'+sys.argv[3])

        if sys.argv[2] == 'tomcat':
            tomcat.Main_tomcat.exec(sys.argv[3])
        elif sys.argv[2] == 'fck':
            fckeditor.Main_fckeditor.exec(sys.argv[3])
        elif sys.argv[2] == 'ip':
            ipquery.Main_ipquery.exec(sys.argv[3])
        elif sys.argv[2] == 'weblogic':
            weblogic.Main_weblogic.exec(sys.argv[3])
        elif sys.argv[2] == 'iis':
            iis.Main_iis.exec(sys.argv[3])
        elif sys.argv[2] == 'docker':
            docker_vuln.Main_docker.exec(sys.argv[3])
        elif sys.argv[2] == 'redis':
            redis_vuln.Main_redis.exec(sys.argv[3])
        elif sys.argv[2] == 'zabbix':
            zabbix_vuln.Main_zabbix.exec(sys.argv[3])
        elif sys.argv[2] == 'navigate':
            navigate_vuln.Main_navigate.exec(sys.argv[3])
        elif sys.argv[2] == 'gatepass':
            gatepass_vuln.Main_gatepass.exec(sys.argv[3])
        elif sys.argv[2] == 'spring':
            spring_vuln.Main_spring.exec(sys.argv[3])
        elif sys.argv[2] == 'ipq':
            ipq.Main_ipq.exec(sys.argv[3])
        elif sys.argv[2] == 'jboss':
            jboss.Main_jboss.exec(sys.argv[3])
        elif sys.argv[2] == 'kindeditor':
            kindeditor.Main_kindeditor.exec(sys.argv[3])
        elif sys.argv[2] == 'drupal':
            durpal.Main_durpal.exec(sys.argv[3])


        else:
            print('''
漏洞检测：
userage: python -u module http://xx.xx.xx.xx:xx
modul:  tomcat fck weblogic iis docker redis zabbix navigate gatepass kindeditor
IP归属查询：
userage: python -u ip www.xxxxx.com/xx.xx.xx.xx
modul：ip ipq
                    ''')
    elif sys.argv[1] == '-p':
        print('[+]检测地址:'+sys.argv[2]+sys.argv[3]+sys.argv[4])
        bf_dicts.Main_bf.exec(sys.argv[2],sys.argv[3],sys.argv[4])

    else:
        print('''
漏洞检测：
userage: python -u module http://xx.xx.xx.xx:xx
modul:  tomcat fck weblogic iis docker redis zabbix navigate gatepass
IP归属查询：
userage: python -u ip www.xxxxx.com/xx.xx.xx.xx
modul：ip ipq
				''')
