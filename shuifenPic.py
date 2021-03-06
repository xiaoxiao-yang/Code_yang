# 水粉画1-50
# url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%B0%B4%E7%B2%89%E7%94%BB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E6%B0%B4%E7%B2%89%E7%94%BB&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&pn='+str(page*30)+'&rn=30&gsm=3c&1543115086720='
# 水粉画风景
# url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%B0%B4%E7%B2%89%E7%94%BB%E9%A3%8E%E6%99%AF&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%B0%B4%E7%B2%89%E7%94%BB%E9%A3%8E%E6%99%AF&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&pn='+str(page*30)+'&rn=30&gsm=3c&1543115217888='
# 水粉画花1-20
# url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%B0%B4%E7%B2%89%E7%94%BB%E8%8A%B1&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%B0%B4%E7%B2%89%E7%94%BB%E8%8A%B1&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&pn='+str(page*30)+'&rn=30&gsm=3c&1543132262557='

import multiprocessing
import requests
import urllib.request
import os
from PIL import Image
import re
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
'''
关键链接地址：
    https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8\&word='+word)
字节编码:
    import urllib.request
    print(urllib.request.quote('水粉画人物'))
'''
filename = 'E:/picture/shuifenhua/imghuajia/'
if not os.path.exists(filename):  # 判断文件夹是否存在
    os.mkdir(filename)

def getpreimg(url):
    urls = urllib.request.urlopen(url).read()
    urls = str(urls)
    pat1 = '"objURL":"(.*?)"'  # 注意用objURL爬取
    images = re.compile(pat1, re.S).findall(urls)
    for index, img in enumerate(images):
        print(img, end='\n')
        imgname = filename + str(index) + '.jpg'
        try:
            urllib.request.urlretrieve(img, filename=imgname)
        except Exception as e:
            print(e)

def getnegimgs(page):
    # page是页数，从1开始
    keyword = '水粉画画家'
    keyword = urllib.request.quote(keyword)
    htmls = []
    try:
        # 水粉画人物1-35
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='+str(keyword)+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word='+str(keyword)+'&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&pn='+str(page*30)+'&rn=30&gsm=5a&1542440984842='
        res = requests.get(url, headers=headers)
        # img = re.findall(res, html, re.S)
        htmls.append(res.json().get('data'))
        # print(htmls[0])
    except Exception as e:
        print(e)
    # 上面获得了很多json包，现在一个一个把图片网址get后写入本地文件夹吧！
    global count
    count = page * 30
    for html in htmls:
        # print(html)
        for i in html:
            if i.get('objURL') != None:
                try:
                    imgname = filename + str(count) + '.jpg'
                    urllib.request.urlretrieve(i.get('thumbURL'), filename=imgname)
                    count = count + 1
                    print(str(count) + "----" + i.get('thumbURL'))
                except Exception as e:
                    print(e)
    saveImg()

def saveImg():
  for filenumber in os.walk(filename):
    # print(filenumber[2])
    for files in filenumber[2]:
      # print(files)
      singleimg = Image.open(filename + files)
      singleimg.close()
      if singleimg.size <= (290, 290):
          os.remove(filename + files)

if __name__ == '__main__':
    keyword = input('请先输入关键字：')
    keyword = urllib.request.quote(keyword)
    url = 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='+keyword
    getpreimg(url)
    p = multiprocessing.Pool(10)
    # for i in range(1, 2):
    p.map(getnegimgs, range(1, 2))
    p.close()
    p.join()
