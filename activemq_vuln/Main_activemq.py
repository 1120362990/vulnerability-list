# -*- coding: utf-8 -*-
import activemq_vuln.ActiveMQ_uploadfile_cve_2016_3088
import activemq_vuln.Activemq_weakpasswd


def exec(URL):
    activemq_vuln.Activemq_weakpasswd.attack(URL)
    activemq_vuln.ActiveMQ_uploadfile_cve_2016_3088.attack(URL)


if __name__ == "__main__":
    exec()
