#coding:utf-8
import re
import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
html_response = requests.get("http://www.ygdy8.net/html/gndy/dyzz/20170129/53080.html", headers = headers)
html_response.encoding = 'GBK'
print html_response.text
html = html_response.text

vname = re.search('◎年　　代　(.*?)<br />', html).group(1).strip()
print vname