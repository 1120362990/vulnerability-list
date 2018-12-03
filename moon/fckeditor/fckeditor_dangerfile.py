# -*- coding: utf-8 -*-
import sys
import requests
import time

'''
Usage:
    moon.py -u  fck http://127.0.0.1:8080
    
'''

def attack(URL):
    urls = (
        '/FCKeditor/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/FCKeditor/editor/filemanager/browser/default/browser.html?type=Image&connector=connectors/asp/connector.asp',
        '/FCKeditor/editor/filemanager/browser/default/browser.html?Type=Image&Connector=http://www.site.com%2Ffckeditor%2Feditor%2Ffilemanager%2Fconnectors%2Fphp%2Fconnector.php',
        '/FCKeditor/editor/filemanager/browser/default/browser.html?Type=Image&Connector=connectors/jsp/connector.jsp',
        '/FCKeditor/editor/filemanager/browser/default/connectors/test.html',
        '/FCKeditor/editor/filemanager/upload/test.html',
        '/FCKeditor/editor/filemanager/connectors/test.html',
        '/FCKeditor/editor/filemanager/connectors/uploadtest.html',
        '/FCKeditor/editor/filemanager/browser/default/browser.html?Type=Image&Connector=connectors/jsp/connector',
        '/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/browser/default/connectors/jsp/connector.jsp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/browser/default/connectors/php/connector.php?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/browser/default/browser.html?type=Image&connector=connectors/asp/connector.asp',
        '/editor/filemanager/browser/default/browser.html?type=Image&connector=connectors/jsp/connector.jsp',
        '/editor/filemanager/browser/default/browser.html?type=Image&connector=connectors/php/connector.php',
        '/editor/filemanager/browser/default/browser.html?Type=Image&Connector=http://www.site.com%2Ffckeditor%2Feditor%2Ffilemanager%2Fconnectors%2Fphp%2Fconnector.php',
        '/editor/filemanager/browser/default/browser.html?Type=Image&Connector=http://www.site.com%2Ffckeditor%2Feditor%2Ffilemanager%2Fconnectors%2Fjsp%2Fconnector.jsp',
        '/editor/filemanager/browser/default/browser.html?Type=Image&Connector=http://www.site.com%2Ffckeditor%2Feditor%2Ffilemanager%2Fconnectors%2Fasp%2Fconnector.asp',
        '/editor/filemanager/browser/default/browser.html?Type=Image&Connector=connectors/jsp/connector.jsp',
        '/editor/filemanager/browser/default/browser.html?Type=Image&Connector=connectors/asp/connector.asp',
        '/editor/filemanager/browser/default/browser.html?Type=Image&Connector=connectors/php/connector.php',
        '/editor/filemanager/browser/default/connectors/test.html',
        '/editor/filemanager/upload/test.html',
        '/editor/filemanager/connectors/test.html',
        '/editor/filemanager/connectors/uploadtest.html',
        '/editor/filemanager/browser/default/browser.html?Type=Image&Connector=connectors/jsp/connector'
    )

    print('[+]开始检测-Fckeditor敏感目录。[+]')
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers={"User-Agent":user_agent}
    for url in urls:
        url = URL + url
        try:
            verify_response = requests.get(url, headers=headers)

            if verify_response.status_code == 200:
                print('存在此页面：'+url)
            else :
                continue
        except :
            print("Someerror!")
    print('[+]检测结束-Fckeditor敏感目录。[+]')
    print('\n')

if __name__ == "__main__":
    attack()


