#!/usr/bin/env python
# -*-encoding:utf-8-*-


import sys,urllib
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import numpy as np

u'''
获取kotlin官方Blog中的发布数据信息,并通过图例展示.

'''

# 解释器
MY_MARKUP="lxml"
# 最近提交的
RECENT_POSTS_ID = "recent-posts-2"
# 所有文档按月份
ARCHIVES_ID = "archives-2"
# 按照标签分类
CATEGORIES_ID = "categories-2"

# filter of archives
ARCHIVES_FILTER_ID = 'entry-title'


def parseSpecies(tagInfo):
    u"""
    用于解析对应项中的url.
    :param tagInfo:  [element.Tag] Tag标签,包裹ul,a
    :return: 返回一个字典,key为分类,value为指向的url.
    """
    dict = {}
    tagList = tagInfo.find_all(name='li')
    for tag in tagList:
        url = tag.a['href']
        name = tag.a.get_text()
        if url and name:
            dict[name] = url
        # print name, url
    return dict


def getArticleInfo(url,filter):
    '''
    get articles' number from this url.
    :param url:  web url
    :return: count of articles.
    '''
    html=urllib.urlopen(url)
    soup = BeautifulSoup(html,MY_MARKUP)
    list=soup.find_all(class_=filter)
    alist = []
    for line in list:
        url = line.a['href']
        title =  line.a.get_text()
        alist.append({"url":url,"title":title})
    return  alist


def drawHistogram(list):
    '''
    draw histogram for list.
    :param list: contain name and count .
    :return:
    '''
    x=[]
    y=[]
    for line in list:
        x.append(line["title"])
        y.append(int(line["count"]))
    plt.bar(x=x,height=y,color='blue',width=0.5)
    plt.show()


main_html = urllib.urlopen("https://blog.jetbrains.com/kotlin")
soup = BeautifulSoup(main_html,MY_MARKUP)
recentPosts =  soup.find(id=RECENT_POSTS_ID)
archives =  soup.find(id=ARCHIVES_ID)
categories = soup.find(id=CATEGORIES_ID)

dic = parseSpecies(categories)
list = []
# print dic
for name,url in dic.items():
    list.append({"title":name[0:4],"count":len(getArticleInfo(url,ARCHIVES_FILTER_ID))})

drawHistogram(list)
