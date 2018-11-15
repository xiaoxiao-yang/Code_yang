import urllib.request
import re
import os
import time
import random
headers = {
    'User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
opener = urllib.request.build_opener()  # 创建opener对象
opener.addheaders = [headers]
urllib.request.install_opener(opener)  # 将opener安装为全局

def craw(url):
    urls = urllib.request.urlopen(url).read()
    urls = str(urls)
    # data = str(data)
    pat1 = '<a class="thumb" href="(.*?)">'  #图片链接的正则表达式
    items = re.compile(pat1).findall(urls)
    for index, item in enumerate(items):
        item = "https://www.felixr.com/" + item
        # print(item, end='\n')
        crawpic(item, index)

def crawpic(url, page):
    urls = urllib.request.urlopen(url).read()
    urls = str(urls)
    # pat1 = '<td class="page">(.*?)</td>'
    pat2 = '<a class="preview".*? href="(.*?)".*?>'   #提取图片的链接地址
    imgurls = re.compile(pat2).findall(urls)
    file = "E:/picture/women/"
    filename = os.path.exists(file)
    if not filename:
        os.makedirs(file)
    for img in imgurls:
        # imgname = "E:/picture/women/" + str(page+97) + '.jpg'
        imgname = file + str(page + 97) + '.jpg'

        # print(img, end='\n')
        try:
            urllib.request.urlretrieve(img, filename=imgname)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            # img +1
            if hasattr(e, "reason"):
                print(e.reason)
                # img +1
            # time.sleep(10)
        except Exception:
            print('sorry, you are wrong!')
            # time.sleep(1)
        else:
            print('第%d张图片下载完成' % (page + 1))
        rom = random.randint(1, 4)
        time.sleep(rom)
# print(time.clock())

if __name__ == '__main__':
    # keyword = input("input keyword:")
    url = "https://www.felixr.com/prints-and-posters/search/results/women/2/96"
    craw(url)
