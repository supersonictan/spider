#coding:utf-8
import re
'''
案例地址：http://www.ygdy8.net/html/gndy/dyzz/index.html
'''
#打开文件
f = open('ddyt_list.html')
html = f.read()
f.close()

#获取页面里每个节目在dytt内部url地址。
each_vdetail_url = re.findall('<a href="(.*?)" class="ulink">', html)
for url in each_vdetail_url:
    print url

#获取节目名称
page_vnames = re.findall('<a href=".*?" class="ulink">.*《(.*?)》.*</a>', html)
for name in page_vnames:
    print name