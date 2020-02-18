# -*- coding: utf-8 -*-
import zabbix_vuln.zabbix_sql_CVE_2016_10134
import zabbix_vuln.Authentication_Bypass


def exec(URL):
    zabbix_vuln.zabbix_sql_CVE_2016_10134.attack(URL)
    zabbix_vuln.Authentication_Bypass.attack(URL)


if __name__ == "__main__":
    exec()
