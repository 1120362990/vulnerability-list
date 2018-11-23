# -*- coding: utf-8 -*-
import redis
import re

'''
Usage:
    moon.py -u  redis http://127.0.0.1:6379
    redis未授权访问漏洞
'''

def attack(URL):
    print('[+]开始检测-Redis未授权访问漏洞。[+]')
    #print(re.findall('//(.*?):',URL)[0])#获取IP
    #print(re.findall(':(\w*?)$',URL)[0])#获取端口
    try:
        r = redis.StrictRedis(host=re.findall('//(.*?):',URL)[0], port=re.findall(':(\w*?)$',URL)[0], db=0)
        print('获取连接成功。客户列表为：'+str(r.client_list()))
    except IndexError:
        try:
            r = redis.StrictRedis(host=re.findall('(.*?):', URL)[0], port=re.findall(':(\w*?)$', URL)[0], db=0)
            print('获取连接成功。客户列表为：' + str(r.client_list()))
        except redis.exceptions.ResponseError:
            print('[-]访问受限：NOAUTH Authentication required')
    except redis.exceptions.ConnectionError:
        print('获取连接失败。')

    print('[+]检测结束-Redis未授权访问漏洞。[+]')
if __name__ == "__main__":
    attack()


