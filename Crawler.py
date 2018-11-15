#!/usr/bin/python3.6  
# -*- coding: utf-8 -*-
# Author:XXY

# openbaidu.py
#!usr/bin/python

from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1542282242141_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1542282242141%5E00_1263X922&word=%E6%B2%B9%E7%94%BB")
browser.find_element_by_id("su").click()
time.sleep(5)
browser.quit()