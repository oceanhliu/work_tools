#!/usr/local/python
#coding=utf-8

import os
import time
from Tkinter import *#python GUI 图形化package

class capp:
    """
    对输入的路径和文件后缀以及编辑的天数进行搜索，并在输入路径下生成一个csv结果
    文件。"""

    def __init__(self, master):
        """file search tool"""
        frame1 = Frame(master)#Tkinter 
        frame1.pack()

        self.quest = Label(frame1, bitmap='questhead')
        self.quest.pack(side=LEFT)
        #self.button=Button(frame, text='Quit', fg='red', command=frame.quit)
        #self.button.pack(side=LEFT)
        self.dirlable = Label(frame1, text=unicode('输入搜索路径:', 'gbk'), font=('songti', 9))
        self.dirlable.pack(side=LEFT)
        self.entry = Entry(frame1, font=('songti', 9), width=65)
        self.entry.pack(side=LEFT)

        frame = Frame(master)
        frame.pack()
        self.Iblext = Label(frame, text=unicode('文件名后缀：', 'gbk'), font=('songti', 9))
        self.Iblext.pack(side=LEFT)

        self.ext = Entry(frame, width=15)
        self.ext.pack(side=LEFT)
        self.extstr = String Var()
        self.extstr.set(U'*.xls')
        self.ext['textvariable'] = self.extstr
        self.contents = StringVar()
        self.contents.set(U'')
        self.entry['textvariable'] = self.contents
        self.daylable = Label(frame, text=unicode('修改时间（几天前）：', 'gbk'), font=('songti', 9))
        self.daylable.pack(side=LEFT)
        self.days = Entry(frame, width =15)
        self.days.pack(side=LEFT)
        self.daystr = StringVar()
        self.daystr.set('1')
        self.days['textvariable'] = self.daystr
        self.hello = Button(frame, text = unicode('查找', 'gbk'), font=('songti', 12, 'bold'), fg='red', bg='white', height = 2, width = 8, command = self.sayhi)
        self.hello.pack(side=LEFT)

        frame3 = Frame(master)
        frame3.pack()
        self.msg = Lable(frame3, text=unicode('', 'gbk'))
        self.msg.pack(side=LEFT)

        def sayhi(self):
            print 'begin ......'
            self.msg.config(text='...')

            try:
                mydir = self.contents.get()
                mydays = self.daystr.get()
                myext = self.extstr.get()
                file1 = open(os.path.join(mydir, 'result.csv'), 'a+')
                searchInfo = '\nsearch' + myext + 'in' + mydays + 'days.seachtime:' + time.strftime('%Y-%m-%d%H:%M:%S', time.localtime(time.time())) + '\n'
                file1.write(searchInfo)
                file1.write('Filename, Modifytime, Size(bytes), Directory\n')
                file1.listFile(mydir, file1, mydays, myext)
                file1.close()
                self.msg.config(text=unicode('搜索成功！', 'gbk'), font=('songti', 9))
            except IOError, (errno, strerror):
                print 'IOError %s:%s' (errno, strerror)
            except:
                print "Unexpectederror:", sys.exc_info()[0]
                self.msg.config(text='error'+str(sys.exc_info()[0]))
                file1.close()
                raise

    def listFile(self, dirname, file1, days.ext):
        """search files....."""
        if len(ext) > 0:
            ext = os.path.splitext(ext)[1]
        if len(dirname) > 0:
            os.chdir(dirname)
            dirname = os.getcwd()
            print '[' + dirname + ']:'
            names = os.listdir(dirname)

        dirs = []

        for filename in names:
            fullname = os.path.join(dirname, filename)
            if os.path.isdir(fullname):
                dirs.append(fullname)
                continue

            if len(ext) > 0:
                if os.path.splitext(filename)[1] != ext:
                    status = 'ignore' + filename + 'forextension'
                    print status
                    self.msg.config(text=unicode(status, 'gbk'), font=('songti', 9))
                    continue

            t = os.path.getmtime(fullname)
            tnow = time.time()
            if len(days) > 0:
                if ((tnow - t) > 86400 * int(days)):
                    status = 'ignore' + filename + 'fordate'
                    print status
                    self.msg.config(text=unicode(status, 'gbk'), font=('songti', 9))
                    continue

            mt = time.localtime(t)
            size = os.path.getsize(fullname)

            fileinfo = filename + ',' + time.strftime('%Y-%m-%d%H:%M:%S', mt) + ',' + str(size) + ',' + dirname +'\n'
            print fileinfo
            file1.write(fileinfo)

        for dirname in dirs:
            self.listFile(dirname, file1, days.ext)

    
    if __name__ == '__main__':
        root = Tk()#GUI 
        root.title(unicode("搜索工具", 'gbk'))
        app = capp(root)
        root.mainloop()#主窗口的成员函数，让root工作起来
