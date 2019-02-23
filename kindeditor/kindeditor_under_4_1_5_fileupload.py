# -*- coding: utf-8 -*-
import sys
import requests
import time

'''
Usage:
    moon.py -u  kindeditor http://127.0.0.1:8080/kidneditor
    影响：kindeditor<=4.1.5   文件上传漏洞   可上传txt和html，用作钓鱼或者跳转博彩网站
    检测方式：这里采用版本判断和查看上传文件的方式确认漏洞是否存在
             首先查询编辑器版本，如果在4.1.5版本之下，且存在相应的上传文件，则认为漏洞存在
'''

def attack(URL):
    print('[+]开始检测-kindeditor<=4.1.5文件上传漏洞。[+]')
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers={"User-Agent":user_agent}

    #获取版本
    try:
        url1 = URL+'/kindeditor-min.js'
        verify_response = requests.get(url1, headers=headers)
        # print(verify_response.status_code)
        print('开始检查kindeditor版本，kindeditor<=4.1.5存在文件上传漏洞:')
        if verify_response.status_code ==200:
            print('此kindeditor的版本为：',verify_response.content[:40])
            print('-----------------------------------------------------')
        else:
            print('未发现获取版本的文件:',verify_response.status_code)
            print('-----------------------------------------------------')
    except:
        print('获取版本失败。')

    #检测上传页面是否存在
    urls = (
        '/asp/upload_json.asp',
        '/asp.net/upload_json.ashx',
        '/jsp/upload_json.jsp',
        '/php/upload_json.php'
    )
    for url in urls:
        url = URL + url
        try:
            verify_response = requests.get(url, headers=headers)

            if verify_response.status_code == 200:
                try:
                    print('存在此页面：'+url+'    '+str(verify_response.status_code))
                except:
                    pass
            else :
                print('未发现此页面：'+url+'    '+str(verify_response.status_code))
                continue
        except :
            print("Someerror!")
    print('[+]检测结束-kindeditor<=4.1.5文件上传漏洞。[+]')
    print('\n')

if __name__ == "__main__":
    attack('')


