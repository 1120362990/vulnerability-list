# -*- coding: utf-8 -*-
import memcache


def attack(URL):
    list = URL.split('/')
    try:
        print('[+]开始检测-memcache未授权访问漏洞。[+]')
        mc = memcache.Client([list[-1]], debug=True)
        print('[!]memcache获取信息结果：[!]')
        ret = mc.get_stats()
        print(ret)
    except:
        print('[-]未发现-发现-memcache未授权访问漏洞。[-]')
        pass
    print('[+]检测结束-memcache未授权访问漏洞。[+]')


if __name__ == "__main__":
    attack()
