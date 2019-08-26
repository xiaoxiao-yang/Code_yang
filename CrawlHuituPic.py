#!/usr/bin/python3.6  
# -*- coding: utf-8 -*-
# Author:XXY
import multiprocessing
import requests
import urllib.request
import os
from PIL import Image
import re
# 汇图网水粉画

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

def getimgs(page):
    # page是页数，从1开始

    htmls = []
    try:
        # 水粉画人物1-35
        # url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='+str(keyword)+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word='+str(keyword)+'&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&pn='+str(page*30)+'&rn=30&gsm=5a&1542440984842='
        url = 'http://soso.huitu.com/Search/GetAllPicInfo?perPageSize=102&kw=%E9%9D%99%E7%89%A9%E6%B0%B4%E7%B2%89%E7%94%BB&page='+str(page)
        res = requests.get(url, headers=headers)
        # img = re.findall(res, html, re.S)
        htmls.append(res.json().get('r'))
        # print(htmls[0])
    except Exception as e:
        print(e)
    # 上面获得了很多json包，现在一个一个把图片网址get后写入本地文件夹吧！
    global count
    count = page * 90
    for html in htmls:
        # print(html)
        for i in html:
            if i.get('imgBigUrl') != None:
                try:
                    imgname = 'E:\\picture\\shuifenhua\\img\\' + str(count) + '.jpg'
                    urllib.request.urlretrieve(i.get('imgBigUrl'), filename=imgname)
                    count = count + 1
                    print(str(count) + "----" + i.get('imgBigUrl'))
                except Exception as e:
                    print(e)

if __name__ == '__main__':
    getimgs(4)