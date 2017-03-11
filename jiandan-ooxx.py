#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'fuqumao'

import sys
import time
import requests
import bs4

# 加入header模拟浏览器
headers = {'referer': 'http://jandan.net/',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}

reload(sys)
sys.setdefaultencoding('utf-8')
baseUrl = 'http://jandan.net/ooxx/page-{}#comments'
begin_page = 0
while begin_page < 300:
    begin_page += 1
    requestUrl = baseUrl.format(begin_page)
    res = requests.get(requestUrl, headers=headers)
    html = bs4.BeautifulSoup(res.text, 'lxml')
    print("开始爬第" + str(begin_page) + '页数据~')
    for index, each in enumerate(html.select('img')):
        # filename=time.strftime('%Y%m%d%H%I%S',time.localtime(time.time()))+str(random.randint(12, 1000))
        filename = str('第' + str(begin_page) + '页第' + str(index) + '张')
        try:
            if str(each.attrs['src'])[-4:] == '.jpg':
                if str(each.attrs['src'])[0:4] != 'http':
                    try:
                        jpg_content = requests.get('http:' + each.attrs['src'], stream=True).content
                        if jpg_content is not None:
                            if sys.getsizeof(jpg_content) >= 10240:
                                jpg = open('D:\\scrawer_pic\{}.jpg'.format(filename.encode('gbk')), 'wb')
                                jpg.write(jpg_content)
                                print('http:' + str(each.attrs['src']) + "下载成功,文件名为:" + filename)
                            else:
                                print('文件大小不符合，舍弃~')
                        else:
                            print('http:' + str(each.attrs['src']) + "下载不成功")
                        # 歇息0.5s
                        time.sleep(0.5)
                    except Exception, e:
                        print('http:' + str(each.attrs['src']) + "下载不成功1,异常信息为" + str(e.message))
                else:
                    try:
                        jpg_content = requests.get(each.attrs['src'], stream=True).content
                        if jpg_content is not None:
                            if sys.getsizeof(jpg_content) >= 10240:
                                jpg = open('D:\\scrawer_pic\{}.jpg'.format(filename.encode('gbk')), 'wb')
                                jpg.write(jpg_content)
                                print(str(each.attrs['src']) + "下载成功,文件名为:" + filename)
                            else:
                                print('文件大小不符合，舍弃~')

                        else:
                            print(str(each.attrs['src']) + "下载不成功")
                        time.sleep(0.5)
                    except Exception, e:
                        print(str(each.attrs['src']) + "下载不成功2,异常信息为" + str(e.message))
        except Exception, e:
            print("出现异常," + str(e.message))
    # 休息2s 防止被反爬虫屏蔽
    time.sleep(2)
