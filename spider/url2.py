# !/usr/bin/etc python
# -*-encoding:utf-8 -*-

import  sys,urllib2
'''
using urllib2
'''


def request(url="http://www.baidu.com"):
    a=urllib2.urlopen(urllib2.Request(url))
    print a.read()











if  __name__ == "__main__":
    request()