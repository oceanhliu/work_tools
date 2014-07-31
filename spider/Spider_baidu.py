#!/usr/local/python
#-*-coding: utf-8-*-

import string
import urllib2
import re
import sys

reload(sys)
sys.setdefaultencoding('gbk')

#------处理页面上的各种标签-----------
class HTML_Tool:
    #用非贪婪模式匹配\t  \n 或空格或者超链接或者图片
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")
    #用非贪婪式匹配任意<>标签
    EndCharToNoneRex = re.compile("<.*?>")
    #用非贪婪模式匹配任意<p>标签
    BgnPartRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")

    #将一些html的符号实体转变为原始符号
    replaceTab = [("<", "<"), (">", ">"), ("&", "&"), ("&", "\""), (" ", " ")]

    def Replace_Char(self, x):
        x = self.BgnCharToNoneRex.sub("", x)
        x = self.BgnPartRex.sub("\n ", x)
        x = self.CharToNewLineRex.sub("\n", x)
        x = self.CharToNextTabRex.sub("\t", x)
        x = self.EndCharToNoneRex.sub("", x)

        for t in self.replaceTab:
            x = x.replace(t[0], t[1])
        return x

class Baidu_Spider:
    #声明相关的属性
    def __init__(self, url):
        self.myUrl = url
        #self.myUrl = url + '?see_lz=1'
        self.datas = []
        self.myTool = HTML_Tool()
        print u'已经启动百度贴吧爬虫......'

    #初始化加载页面并将其转码储存
    def baidu_tieba(self):
        #读取页面的原始信息并将其从gbk转码
        myPage = urllib2.urlopen(self.myUrl).read().decode('gbk')
        #计算楼主发布内容一共多少页
        endPage = self.page_counter(myPage)
        print 'debug_logger: total page==== %d' % endPage
        #获取该帖的标题
        title = self.find_title(myPage)
        print u'文章名称：' + title
        #获取最终的数据
        self.save_data(self.myUrl, 'baidutieba_'+title, endPage)


    #用来计算一共有多少页
    def page_counter(self, myPage):
        #匹配“共有<span class="red">12</span>页”来获取一共多少页
        #<span class="red">11</span>页
        myMatch = re.search(r'class="red">(\d+?)</span>', myPage, re.S)
        
        if myMatch:
            endPage = int(myMatch.group(1))
            print u'爬虫报告：发现楼主共有%d页的原创内容' % endPage
        else:
            endPage = 0
            print u'爬虫报告：无法计算楼主发布内容有多少页'
        return endPage

    #用来寻找该帖的标题
    def find_title(self, myPage):
        #匹配<h1 class="core_title_txt" title="">xxxx</h1>找出标题
        myMatch = re.search(r'<h1.*?>(.*?)</h1>', myPage, re.S)
        title = u'暂无标题'
        if myMatch:
            title = myMatch.group(1)
        else:
            print u'爬虫报告：无法加载文章标题！'
        #文件名不能包含以下字符：\/:*?"<>|
        title = title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','') 
        return title

    #用来存储楼主发布的内容
    def save_data(self, url, title, endPage):
        #加载页面数据到数组
        self.get_data(url, endPage)
        #打开本地文件
        f = open(title + '.txt', 'w+')
        f.writelines(self.datas)
        f.close()
        print u'爬虫报告文件已下载到本地并打包成txt文件'
        print u'请按任意键推出...'
        raw_input();

    #获取页面源码并将其存储到数组中
    def get_data(self, url, endPage):
        url = url + '?pn='
        for i in range(1, endPage+1):
            print u'爬虫报告：爬虫%d号正在加载...' % i
            myPage = urllib2.urlopen(url + str(i)).read()
            #将myPage中的html代码处理并存储到datas里面
            self.deal_data(myPage.decode('gbk'))

    #将内容从页面代码中抠出来
    def deal_data(self, myPage):
        myItems = re.findall('id="post_content.*?>(.*?)</div>', myPage, re.S)
        for item in myItems:
            data = self.myTool.Replace_Char(item.replace("\n", "").encode('utf-8'))
            self.datas.append(data + '\n')




#---------------------程序入口----------------------
print u"""#------------------------------------
# program: Baidu_Spider
# version: 1.0
# coder: oceanhliu
# date: 2014-07-19
# ---------------------------------------------
"""
#bdurl = 'http://tieba.baidu.com/p/2296712428?pn=1' 

print u'请输入贴吧的地址最后的数字串：'
bdurl = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))

#call 
mySpider = Baidu_Spider(bdurl)
mySpider.baidu_tieba()
