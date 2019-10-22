# -*- coding: utf-8 -*-
import requests

'''
Usage:
    moon.py -u  weblogic http://127.0.0.1:8080
    用来查看weblogic常见的4个页面
'''

def attack(URL):
    urls = (
        '/console/login/LoginForm.jsp',
        '/wls-wsat/CoordinatorPortType',
        '/_async/AsyncResponseService',
        '/ws_utc/config.do'
    )

    print('[+]开始检测-Weblogic-common_page。[+]')
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers={"User-Agent":user_agent}
    for url in urls:
        url = URL + url
        try:
            verify_response = requests.get(url, headers=headers)

            if verify_response.status_code == 200:
                try:
                    print('[*]页面返回状态码：'+str(verify_response.status_code)+'  '+'页面返回大小为：'+str(len(verify_response.text))+'  '+url) # 因为部分网站设置了统一的404页面，造成误报，因此添加返回长度来进行辅助判断
                except Exception:
                    pass
            else:
                print('未发现页面：'+url)
                continue
        except Exception:
            print("[-]访问页面出错!")
    print('[+]检测结束-Weblogic-common_page。[+]')
    print('\n')

if __name__ == "__main__":
    attack()
