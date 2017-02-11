#-*-coding:utf8-*-
from lxml import etree
import re
import requests
import sys
reload(sys)

"""
解析detail页面。
页面样例：http://www.ygdy8.net/html/gndy/dyzz/20170129/53080.html
"""

def get_detail_data(url):
    html_str = get_htmlString(url)
    get_vInfo_dic(html_str)


#获取网页的html数据
def get_htmlString(url):
    html = requests.get(url)
    html_str = html.content.decode('gbk').encode('utf-8')
    output = open('resource/requests_html.html', 'w')
    output.write(html_str)
    output.close()
    return html_str

def get_vInfo_dic(html_str):
    dic = {}
    name = re.search('◎年　　代　(.*?)<br />', html_str).group(1).strip()
    country = re.search('◎国　　家　(.*?)<br />', html_str).group(1).strip()
    category = re.search('◎类　　别　(.*?)<br />', html_str).group(1).strip()
    language = re.search('◎语　　言　(.*?)<br />', html_str).group(1).strip()
    screan_lang = re.search('◎字　　幕　(.*?)<br />', html_str).group(1).strip()
    imdb = re.search('◎IMDb评分&nbsp; (.*?) users<br />', html_str).group(1).strip()
    size = re.search('◎视频尺寸　(.*?)<br />', html_str).group(1).strip()
    length = re.search('◎片　　长　(.*?)<br />', html_str).group(1).strip()
    director = re.search('◎导　　演　(.*?)<br />', html_str).group(1).strip()
    actors = re.search('◎主　　演　(.*?)<br /><br />', html_str).group(1).strip()
    intro = re.search('◎简　　介<br /><br />　　(.*?)<br /><br />', html_str).group(1).strip()
    ftp = 'ftp://' + re.search('<a href="ftp://(.*?)">', html_str).group(1).strip()
    title_image = re.search('border="0" src="(.*?)" alt="" /><br /><br />', html_str).group(1).strip()
    detail_image = re.findall('window.open\(\'(.*?)\'\);" border', html_str)[1]

    dic['name'] = name
    dic['country'] = country
    dic['category'] = category
    dic['language'] = language
    dic['screan_lang'] = screan_lang
    dic['imdb'] = imdb
    dic['size'] = size
    dic['length'] = length
    dic['director'] = director
    dic['actors'] = actors
    dic['intro'] = intro
    dic['ftp'] = ftp
    dic['title_image'] = title_image
    dic['detail_image'] = detail_image

    print dic