import multiprocessing
import requests
import urllib.request
import pprint
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

def getnegimgs(page):
    # page是页数，从1开始
    htmls = []
    try:
        # url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%A1%A8%E6%83%85%E5%8C%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E8%A1%A8%E6%83%85%E5%8C%85&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&pn="+str(page*30)+"&rn=30&gsm=5a&1520829304174="
        url = "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%B2%B9%E7%94%BB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E6%B2%B9%E7%94%BB&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&pn="+str(page*30)
    # 要加上header啊！而且不要加错，从浏览器里复制出来就好，加错或不加可能会返回403错误的
        res = requests.get(url, headers=headers)
        htmls.append(res.json().get('data'))
        print(htmls)
    except Exception as e:
        print(e)
# 上面获得了很多json包，现在一个一个把图片网址get后写入本地文件夹吧！
#     global count
#     count = (page-1)*30
#     for html in htmls:
#         for i in html:
#             if i.get('thumbURL') != None:
#                 try:
#                     imgname = 'F:/negimage/' + str(count) + '.jpg'
#                     urllib.request.urlretrieve(i.get('thumbURL'), filename=imgname)
#                     count = count + 1
#                     # ir = requests.get(i.get('thumbURL'), headers=headers)
#                     # # if ir.status_code == 200:
#                     # #     open('F:/negimage1/' + '%d.jpg'%count, 'wb').write(ir.content)
#                     # #     print(str(count) + "----" + i.get('thumbURL'))
#                     # #     count = count + 1
#                     # open('F:/negimage/' + '%d.jpg' % count, 'wb').write(ir.content)
#                     print(str(count) + "----" + i.get('thumbURL'))
#                     # count = count + 1
#                 except Exception as e:
#                     print(e)
if __name__ == '__main__':

    p = multiprocessing.Pool(10)
    #for i in range(1, 34):
    p.map(getnegimgs, range(1, 2))
    p.close()
    p.join()
