# vulnerability-list

常见漏洞快速检测，目前包含以下漏洞的检测。  
测试环境为win10，python3。  
使用前需安装相关库：py -3 -m pip install -r requirements.txt  
有问题可提issues，最好附上报错截图。  

已发现的BUG：  

1. 有些漏洞的判断依据为网页返回信息，但部分网站设置了统一的错误页面，如统一的404页面，因此造成误报。后续针对此类问题通用的解决方式是显示返回页面的大小。

## Tomcat

- CVE_2017_12615 / CVE_2017_12617  
- tomcat_weakpassword  
- example_vulnerability(检测tomcat的examples等目录是否存在)  
- CNVD-C-2019-48814/CVE-2020-1938 #Apache Tomcat文件包含 参考：<https://github.com/YDHCUI/CNVD-2020-10487-Tomcat-Ajp-lfi/blob/master/CNVD-2020-10487-Tomcat-Ajp-lfi.py>  

> moon.py -u tomcat <http://xx.xx.xx.xx:xxxx>
  
## Fckeditor

- 获取版本及常见上传页面检测  
- fck<=2.4版本上传直接上传asa文件getshell  

> moon.py -u fck <http://xx.xx.xx.xx/fckxx>  

## Weblogic

- CVE_2017_10271 # 利用方法参考：<https://vulhub.org>  
- weblogic_ssrf_cve-2014-4210  
- weblogic_weakpassword  
- CVE-2018-2628   # Author:xxlegend  
- CNVD-C-2019-48814  
- CVE-2019-2725 # 参考：<https://github.com/lufeirider/CVE-2019-2725>

> moon.py -u weblogic <http://xx.xx.xx.xx:xxxx>  

## IP归属查询

- 能简单查一下IP的归属地  

> moon.py -u ip <http://www.xxx.com>  

## IIS

- 短文件名泄露 #来自 lijiejie/IIS_shortname_Scanner  

> moon.py -u iis <http://xx.xx.xx.xx>  

## Docker

- docker_daemon_api未授权访问  

> moon.py -u docker <http://xx.xx.xx.xx:xxxx>  

## Redis

- redis未授权访问  

> moon.py -u redis <http://xx.xx.xx.xx:xxxx> or moon.py -u redis xx.xx.xx.xx:xxxx  

## Zabbix

- zabbix_sql_CVE_2016_10134      #有参考独自等待的脚本  

> moon.py -u zabbix <http://xx.xx.xx.xx:xxxx>  

## Navigate

- navigate_Unauthenticated_Remote_Code_Execution  #利用方法参考  <https://www.exploit-db.com/exploits/45561/>  

> moon.py -u navigate <http://xx.xx.xx.xx:xxxx>  

## Gatepass

- Gate Pass Management System 2.1 - 'login' SQL Injection  # 参考  <https://www.exploit-db.com/exploits/45766/>  

> moon.py -u gatepass <http://xx.xx.xx.xx:xxxx>  

## Jboss

- admin-console  
- Checking Struts2  
- Checking Servlet Deserialization  
- Checking Application Deserialization  
- Checking Jenkins  
- Checking web-console  
- Checking jmx-console  
- JMXInvokerServlet  
- 此模块调用的是 # jexboss 使用此模块时，建议在微软新推出的terminal中使用<https://github.com/microsoft/terminal>，或者直接下载jexboss进行测试  

> moon.py -u jboss <http://xx.xx.xx.xx:xxxx>  

## Kindeditor

- kindeditor<=4.1.5文件上传漏洞

> moon.py -u kindeditor <http://xx.xx.xx.xx:xxxx/kidneditor-4.1.5>  

## Drupal

- Drupal < 7.32 “Drupalgeddon” SQL注入漏洞（CVE-2014-3704）  
- Drupal Drupalgeddon 2远程代码执行漏洞（CVE-2018-7600） # <https://github.com/a2u/CVE-2018-7600/blob/master/exploit.py>  

> moon.py -u drupal <http://xxx.xxx.xxx.xxx:xxxx>

## Thinkphp

- thinkphp_before5_0_23_rce  
- thinkphp5_inj_info  
- thinkphp5_x_rce  

> moon.py -u thinkphp <http://xxx.xxx.xxx.xxx:xxxx>

## Memcache

- 未授权访问

> moon.py -u memcache <http://xxx.xxx.xxx.xxx:xxxx>

## Js

- js代码中敏感信息收集 # 主要参考 <https://threezh1.github.io>  By Threezh1  

> moon.py -u js <http://xxx.xxx.xxx.xxx:xxxx>  

## search_exploits

- 在 exploitalert 中搜索某中间件存在的历史漏洞  

> moon.py -u exploits xxxxxx  

![search_exploits](https://raw.githubusercontent.com/1120362990/Paper/master/images/vulnerability-list-images/search_exploits.png)

## ActiveMQ

- activemq管理后台弱口令检测  
- CVE-2016-3088 activemq文件上传测试，这里只测试文件上传这个步骤，后续的MOVE操作请自行测试  

> moon.py -u activemq <http://xxx.xxx.xxx.xxx:xxxx>  

请勿用于违法行为，后果自负。  
