#coding:utf-8
import re
import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

#headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
html = requests.get("http://www.ygdy8.net/html/gndy/dyzz/20170129/53080.html", headers = headers)

# s = html.text
# print isinstance(s, unicode)
# print type(s)
#vname = re.search('◎导　　演　(.*?)<br />', html.content.encode('gbk').decode('utf-8').encode('utf-8')).group(1).strip()

output = open('requests_html.html','w')
output.write(html.content.decode('gbk').encode('utf-8'))
output.close()


vname = re.search('◎导　　演　(.*?)<br />', html.content.decode('gbk').encode('utf-8')).group(1).strip()
print vname;

content = html.content
print type(html.content)
html.content.decode('gbk').encode('utf-8')
print type(html)











# html.encoding = 'GB2312'
# html.encoding = 'UTF-8'
# html.encoding('GB2312')
# print html
# file = open('requests_html')
# html_file = file.read()
# vname = re.search('◎导　　演　(.*?)<br />', html_file).group(1).strip()
# print vname;
#
# html.text.decode('GB2312').encode('utf-8')
# print html.headers['content-type']
# # print html.encoding
# # print html.apparent_encoding
# #print html.content.decode('gbk').encode('utf-8')
#
# #html.encoding = 'utf-8'
# output = open('requests_html.html','w')
# output.write(html.text.decode('gbk').encode('utf-8'))
# output.close()
# vname = re.search('◎导　　演　(.*?)<br />', html.text.decode('gbk').encode('utf-8')).group(1).strip()