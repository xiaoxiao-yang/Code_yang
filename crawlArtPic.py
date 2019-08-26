# 发现艺术品网站的艺术图片爬取
# http://www.studentart.com.cn/attachment/201810/23/47240470090fc66098680c16a32d383d.jpg
# http://www.studentart.com.cn/attachment/201810/23/57591_15402607322yM5_t5.jpg

import urllib.request
import re
import multiprocessing
import os

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

def pic(page):
    url = 'http://www.studentart.com.cn/arts/artwork?&ptype=10&order=1&p='+str((page-1)*120)
    urls = urllib.request.urlopen(url).read()
    urls = str(urls)
    # print(urls)
    # pat = '<a target="_blank" href="(.*?)"'
    pat = '<img class="imglazyload".*? original="(.*?)"'
    piclist = re.compile(pat).findall(urls)
    # print(urls)
    path = 'E:\\picture\\shuicaihua\\img\\'
    if not os.path.exists(path):
        os.makedirs(path)
    global count
    count = (page-1) * 120
    for picitem in piclist:
        # i += 1
        # print(i)python
        img = str(picitem).rsplit("_", maxsplit=1)
        filepath = path + str(count) + '.jpg'
        count += 1
        try:
            urllib.request.urlretrieve(img[0]+'.jpg', filename=filepath)
            print('the {} finished'.format(count))
        except Exception as e:
            print(e)
    print('finished!')
if __name__ == '__main__':
    p = multiprocessing.Pool(10)
    # for i in range(2):
        # url = 'http://www.studentart.com.cn/arts/artwork?&ptype=3&order=1&p='+i
    p.map(pic, range(2, 5))