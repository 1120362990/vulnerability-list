# vulnerability-list

常见漏洞快速检测，目前包含以下漏洞。
  
## Tomcat：  

- CVE_2017_12615 / CVE_2017_12617  
- tomcat_weakpassword  
- example_vulnerability(检测tomcat的examples等目录是否存在)  

> moon.py -u tomcat http://xx.xx.xx.xx:xxxx
  
## Fckeditor

- 获取版本及常见上传页面检测  
- fck<=2.4版本上传直接上传asa文件getshell  

> moon.py -u fck http://xx.xx.xx.xx/fckxx  

## Weblogic

- CVE_2017_10271 #利用方法参考：https://vulhub.org  
- weblogic_ssrf_cve-2014-4210  
- weblogic_weakpassword  
- CVE-2018-2628   #Author:xxlegend  

> moon.py -u weblogic http://xx.xx.xx.xx:xxxx  

## IP归属查询

- 能简单查一下IP的归属地  

> moon.py -u ip http://www.xxx.com  

## IIS

- 短文件名泄露 #来自 lijiejie/IIS_shortname_Scanner  

> moon.py -u iis http://xx.xx.xx.xx  

## Docker

- docker_daemon_api未授权访问  

> moon.py -u docker http://xx.xx.xx.xx:xxxx  

## Redis

- redis未授权访问  

> moon.py -u redis http://xx.xx.xx.xx:xxxx or moon.py -u redis xx.xx.xx.xx:xxxx  

## Zabbix

- zabbix_sql_CVE_2016_10134      #有参考独自等待的脚本  

> moon.py -u zabbix http://xx.xx.xx.xx:xxxx  

## Navigate

- navigate_Unauthenticated_Remote_Code_Execution  #利用方法参考  https://www.exploit-db.com/exploits/45561/  

> moon.py -u navigate http://xx.xx.xx.xx:xxxx  

## Gatepass

- Gate Pass Management System 2.1 - 'login' SQL Injection      #参考  https://www.exploit-db.com/exploits/45766/  

> moon.py -u gatepass http://xx.xx.xx.xx:xxxx  

## Jboss

- admin-console  
- Checking Struts2  
- Checking Servlet Deserialization  
- Checking Application Deserialization  
- Checking Jenkins  
- Checking web-console  
- Checking jmx-console  
- JMXInvokerServlet  
- 此模块调用的是 #jexboss  

> moon.py -u jboss http://xx.xx.xx.xx:xxxx  

## Kindeditor

- kindeditor<=4.1.5文件上传漏洞

> moon.py -u kindeditor http://xx.xx.xx.xx:xxxx/kidneditor-4.1.5  

## Drupal

- Drupal < 7.32 “Drupalgeddon” SQL注入漏洞（CVE-2014-3704）  
- Drupal Drupalgeddon 2远程代码执行漏洞（CVE-2018-7600） # https://github.com/a2u/CVE-2018-7600/blob/master/exploit.py  

> moon.py -u drupal http://xxx.xxx.xxx.xxx:xxxx