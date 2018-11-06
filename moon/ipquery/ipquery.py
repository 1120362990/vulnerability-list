# -*- coding: utf-8 -*-
from urllib.parse import urlparse
import socket
import requests

def attack(URL):
    url = URL
    URL = urlparse(URL).netloc
    if URL == '':
        URL = url
        #print('IP查询目标：' + URL)
    else:
        pass
    try:
        ip = URL
        payload = {'query': ip, 'resource_id': '6006'}
        r = requests.get("https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php", params=payload)

        print(r.json().get('data')[0].get('location'))
    except:
        try:
            ip = socket.gethostbyname(URL)
            print('IP查询目标：' + ip)
            payload = {'query': ip, 'resource_id': '6006'}
            r = requests.get("https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php", params=payload)
            print(r.json().get('data')[0].get('location'))
        except:
            print('获取IP地址错误：'+URL)


if __name__ == "__main__":
    attack()

