#!/usr/bin/env python
# coding=utf-8
import re
import urllib
import urllib2
from bs4 import BeautifulSoup

print ("--------------------------------\n"
       "LINK:http://routerpasswords.com/\n"
       "说明：密码收集爬虫\n"
       "作者：雷锋 后续继续改进文字类型\n"
       "--------------------------------")

url ='http://routerpasswords.com'
req = urllib2.urlopen(url).read()  #读取获取的网页内容
reg = re.compile(r'<option value=\"(.*?)\"') #正则过滤关键字
htm = re.findall(reg,req)              # 设备名字变量列表

for i in htm:
    data = urllib.urlencode({
      'findpass':1,
      'router':i,
      'findpassword':'Find+Password'
    }) # POST包数据
    content = urllib2.urlopen(urllib2.Request(url, data)).read()  # URL_POST请求并读取内容
    soup = BeautifulSoup(content,"html.parser")  # 创建BS对象
    strs = soup.find_all("table")       # 获取表格内的数据
    file_object = open('Userpass.html', 'a+')
    file_object.write(str(strs))        # 写入 关闭
    file_object.close()