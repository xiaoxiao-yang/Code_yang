import urllib.request
import re
import os
headers = {
    'User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

def crawil(url):
    urls = urllib.request.urlopen(url).read().decode('utf-8')
    urls = str(urls)
    # pat1 = '<ul class="imglist clearfix pageNum0".*?>(.*?)</ul>'
    # ht = re.compile(pat1).findall(urls)
    print(urls)

crawil("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D3%CD%BB%AD&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000")