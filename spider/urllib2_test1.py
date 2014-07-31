#!/usr/local/python

#-*-coding: utf-8-*-
import urllib2

#create a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
#add username and pwd
top_level_url = "http://example.com/foo/"
#if know realm,we can use "None" daiti it
#password_mgr.add_password(None, top_level_url, username, password)
password_mgr.add_password(None, top_level_url,'why', '123')

#create a new handler
handler = urllib2.HTTPBasicAuthHandler(password_mgr)

#create "opener"
opener = urllib2.build_opener(handler)

a_url = 'http://www.baidu.com/'

#use opener get a url
opener.open(a_url)

#install opener
#now all call urllib2.urlopen will use our opener
urllib2.install_opener(opener)
