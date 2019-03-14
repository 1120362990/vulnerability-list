# -*- coding: utf-8 -*-
import docker
import os

'''
hydra
'''


def attack(service,ip,port):
    if service  == 'ftp':
        os.chdir('bf_dicts')
        os.system(f'hydra -L FTP-user.txt -P FTP-passwd.txt -V -s {port} {ip} {service}')
    else:
        print('Service for -'+service+'- not support!')
    
    print(service,ip,port)




if __name__ == "__main__":
    attack()
