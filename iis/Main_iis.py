# -*- coding: utf-8 -*-
import iis.iis_shortname_Scan
import os

def exec(URL):
    # print('[+]开始检测-IIS短文件名漏洞。[+]')
    # #切换工作路径
    # os.chdir('iis')
    # os.system("py -2 iis_shortname_Scan.py "+URL) 
    # print('[+]检测完成-IIS短文件名漏洞。[+]')

    iis.iis_shortname_Scan.attack(URL)

if __name__ == "__main__":
    exec()
