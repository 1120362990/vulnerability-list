# -*- coding: utf-8 -*-
import os
import durpal.CVE_2014_3704
import durpal.CVE_2018_7600

def exec(URL):
    durpal.CVE_2014_3704.attack(URL)
    durpal.CVE_2018_7600.attack(URL)




if __name__ == "__main__":
    exec()
