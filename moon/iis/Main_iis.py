# -*- coding: utf-8 -*-
import ipquery.ipquery
import os

def exec(URL):
    print('[+]开始检测-IIS短文件名漏洞。[+]')
    #切换工作路径
    os.chdir(os.path.realpath(__file__)[:38])
    os.system("py -2 iis_shortname_Scan.py "+URL) 
    print('[+]检测完成-IIS短文件名漏洞。[+]')





if __name__ == "__main__":
    exec()
