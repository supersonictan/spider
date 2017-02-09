#coding:utf-8
import re
'''
案例地址：http://www.ygdy8.net/html/gndy/dyzz/20170129/53080.html
'''
#打开文件
f = open('resource/detail.html','r')
html = f.read()
f.close()

#获取页面里每个节目在dytt内部url地址。
vname = re.search('◎年　　代　(.*?)<br />', html).group(1).strip()
v_country = re.search('◎国　　家　(.*?)<br />', html).group(1).strip()
v_category = re.search('◎类　　别　(.*?)<br />', html).group(1).strip()
v_language = re.search('◎语　　言　(.*?)<br />', html).group(1).strip()
v_screan_lang = re.search('◎字　　幕　(.*?)<br />', html).group(1).strip()
v_imdb = re.search('◎IMDb评分&nbsp; (.*?) users<br />', html).group(1).strip()
v_size = re.search('◎视频尺寸　(.*?)<br />', html).group(1).strip()
v_length = re.search('◎片　　长　(.*?)<br />', html).group(1).strip()
v_director = re.search('◎导　　演　(.*?)<br />', html).group(1).strip()
v_actors = re.search('◎主　　演　(.*?)<br /><br />', html).group(1).strip()
v_intro = re.search('◎简　　介<br /><br />　　(.*?)<br /><br />', html).group(1).strip()
v_ftp = 'ftp://' + re.search('<a href="ftp://(.*?)">', html).group(1).strip()
v_main_image = re.search('border="0" src="(.*?)" alt="" /><br /><br />', html).group(1).strip()
v_detail_image = re.findall('window.open\(\'(.*?)\'\);" border', html)[1]


#下载图片到本地

print vname
print v_country
print v_category
print v_language
print v_screan_lang
print v_imdb
print v_size
print v_length
print v_director
print v_actors.split('<br />')
print v_actors
print v_intro
print v_ftp
print v_main_image
print v_detail_image