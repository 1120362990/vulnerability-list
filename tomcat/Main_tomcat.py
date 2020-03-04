# -*- coding: utf-8 -*-
import tomcat.CVE_2017_12615
import tomcat.example_vulnerability
import tomcat.CVE_2017_12617
import tomcat.tomcat_weakpasswd
import tomcat.CVE_2020_1938


def exec(URL):
    tomcat.example_vulnerability.attack(URL)
    tomcat.CVE_2017_12615.attack(URL)
    tomcat.CVE_2017_12617.attack(URL)
    tomcat.tomcat_weakpasswd.attack(URL)
    tomcat.CVE_2020_1938.attack(URL)




if __name__ == "__main__":
    exec()
