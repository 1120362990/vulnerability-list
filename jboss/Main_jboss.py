# -*- coding: utf-8 -*-
import os
import jboss

def exec(URL):
    print('[+]开始检测-jboss。[+]')
    #切换工作路径
    os.chdir(os.path.realpath(__file__)[:35])
    os.system("py -2 jexboss.py -host "+URL) 
    print('[+]检测结束-jboss。[+]')


if __name__ == "__main__":
    exec()
