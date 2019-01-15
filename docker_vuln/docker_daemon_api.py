# -*- coding: utf-8 -*-
import docker


'''
Usage:
    moon.py -u docker_vuln http://127.0.0.1:2375
    此漏洞默认存在2375端口上-nmap扫描结果- 2375/tcp open  docker
    贴一个漏洞介绍，可能拿shell：https://blog.csdn.net/qq_33020901/article/details/78685447
'''


def attack(URL):
    print('[+]开始检测-Docker-docker_daemon_api未授权访问。[+]')
    try:
        client = docker.DockerClient(base_url=URL)

        print('获取到的容器列表：'+str(client.containers.list()))
        print('[+]存在漏洞，连接成功!!!')
    except:
        print('[-]连接失败，漏洞不存在。')
    print('[+]检测完成-Docker-docker_daemon_api未授权访问。[+]')
    print('\n')




if __name__ == "__main__":
    attack()

