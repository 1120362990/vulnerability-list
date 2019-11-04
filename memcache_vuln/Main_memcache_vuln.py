# -*- coding: utf-8 -*-
import memcache_vuln.memcache_un


def exec(URL):
    # memcahce_un.attack(URL)
    memcache_vuln.memcache_un.attack(URL)


if __name__ == "__main__":
    exec()
