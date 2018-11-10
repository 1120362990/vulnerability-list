# -*- coding: utf-8 -*-

import redis_vuln.redis_unauthorized


def exec(URL):
    redis_vuln.redis_unauthorized.attack(URL)



if __name__ == "__main__":
    exec()
