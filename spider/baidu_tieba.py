#!/usr/local/python
#coding=utf-8
#出现这个错误  UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-9: ordinal not in range(128)
#在开头加上 import sys.....
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import string, urllib2
def baidu_tieba(url, begin_page, end_page):
    for i in range(begin_page, end_page+1):
        sName = string.zfill(i, 5) + '.html'#自动填充成六位的文件名
        print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......'
        f = open(sName, 'w+')
        m = urllib2.urlopen(url+str(i)).read()
        f.write(m)
        f.close()


bdurl = str(raw_input(u'请输入贴吧地址，去掉pn=后面的数字：\n'))
begin_page = int(raw_input(u'请输入开始的页数：\n'))
end_page = int(raw_input(u'请输入结束的页数：\n'))


baidu_tieba(bdurl, begin_page, end_page)

