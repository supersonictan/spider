#-*-coding:utf8-*-
from lxml import etree
import re
import requests
import sys
reload(sys)


# 解析detail页面





#获取网页的html数据
def get_html(url):
    html = requests.get(url)
    return html





demo = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_2.html'


selector = etree.HTML(html1)
content = selector.xpath('//div[starts-with(@id,"test")]/text()')
for each in content:
    print each