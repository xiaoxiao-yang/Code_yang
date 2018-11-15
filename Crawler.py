#!/usr/bin/python3.6  
# -*- coding: utf-8 -*-
# Author:XXY

# openbaidu.py
#!usr/bin/python

from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}



def getnegimgs(url,page):
    # page是页数，从1开始
    htmls = []
    try:
        # url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%A1%A8%E6%83%85%E5%8C%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E8%A1%A8%E6%83%85%E5%8C%85&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&pn="+str(page*30)+"&rn=30&gsm=5a&1520829304174="
    # 要加上header啊！而且不要加错，从浏览器里复制出来就好，加错或不加可能会返回403错误的

        res = requests.get(url, headers=headers)
        htmls.append(res.json().get('data'))
        print(htmls)
    except Exception as e:
        print(e)
page = 0
def URL(page):
    Main_URL = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E6%B2%B9%E7%94%BB&pn="+str(page)+"&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0"
    return Main_URL

browser = webdriver.Firefox()

for i in range(10):
    url = URL(page)
    browser.get(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    print("第",i,"页,\n",soup)
    time.sleep(2)
    page = page + 20


# for i in range(2):
#     browser.find_element_by_class_name('n').click()
#     # getnegimgs()
#
#
#     # bsObj = BeautifulSoup()
#     # print(bsObj.h1)
#     time.sleep(2)

browser.quit()