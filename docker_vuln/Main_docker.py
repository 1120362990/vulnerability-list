# -*- coding: utf-8 -*-
import docker_vuln.docker_daemon_api


def exec(URL):
    docker_vuln.docker_daemon_api.attack(URL)




if __name__ == "__main__":
    exec()
