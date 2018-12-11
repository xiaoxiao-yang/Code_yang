#!/usr/bin/python3.6  
# -*- coding: utf-8 -*-
# Author:XXY

import urllib.request   # 导入urllib模块
import re     # 导入re模块
import os
from PIL import Image
htmlurl = 'http://www.win4000.com/wallpaper_detail_134824_3.html'
downloadpath = 'E:\\picture\\img\\'
def getHTML(htmlurl):
  req = urllib.request.urlopen(htmlurl)
  buf = req.read()
  return buf.decode('utf-8')
def downloadImg(buf):
  req = r'src="(.+?\.jpg)"' #正则表达式，匹配图片格式
  imgreq = re.compile(req) #编译正则表达式
  imglist = re.findall(imgreq, buf)
  # print(imglist)
  x = 0
  if not os.path.isdir(downloadpath):#若没有则创建
    os.makedirs(downloadpath)
  paths = downloadpath
  for imgurl in imglist:
    f = open(paths + str(x) +'.jpg',"wb")  #打开文件
    req = urllib.request.urlopen(imgurl)
    buf = req.read()       #读出文件
    f.write(buf)
    f.close()
    x = x + 1
  return imglist
def saveImg():
  for filenumber in os.walk(downloadpath):
    print(filenumber[2])
    for files in filenumber[2]:
      print(files)
      singleimg = Image.open(downloadpath + files)
      singleimg.close()
      #print(singleimg.size, singleimg.width, singleimg.height)
      if singleimg.size == (1920, 1080):
        print(singleimg)
      else:
        os.remove(downloadpath + files)
buf = getHTML(htmlurl)
downloadImg(buf)
saveImg()