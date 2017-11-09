# !/usr/bin/env python
# -*-encoding:utf-8 -*-

import sys,urllib,urllib2




'''
urllib和urllib2的使用
'''

def accessByUrllib():
    print "access html by urllib"
    url="http://www.enjoytoday.cn/posts/362"
    page=urllib.urlopen(url)
    #print "page html:%s" % page.read()  #返回html文件内容
    print "\npage info:%s " % page.info()#返回基本信息(头信息)
    print "\npage code:%s"% page.getcode() #http请求响应码,若非http则返回None
    print "\npage url:%s"%page.geturl()  #请求url,,真实访问url(重定问情况下和url不相同)
    print "\npage headers: %s"%page.headers #返回头信息

    #将html写入本地,两种方法
    url_file=open("./test.html",'wb+')
    url_file.write(page.read())
    url_file.close()

    #使用urllib模块直接写入
    urllib.urlretrieve(url,"./test2.html")




def requestMethod(method="GET"):
    '''
    默认的urllib是以GET方式进行请求,可以通过使用urlencode()方法对其实现post请求,传入数据为类字典类型,key:vaule格式,但
    默认参数类型为标准的application/x-www-form-urlencoded表单格式,不可更改
    :param method: 指定请求方式:GET,POST
    :return:
    '''
    url="http://www.enjoytoday.cn/posts/362"
    if method:
        if method=="GET":
            page=urllib.urlopen(url)
            print "get request return:%s"%page.read()
        elif method=="POST":
            reload(sys)
            sys.setdefaultencoding('utf-8')   #解决 'ascii' codec can't encode characters问题,注意需要在调用setdefaultencoding()之前先reload(sys)不然会抛出没有该方法.
            dic={"name":u'飞云不在线',"sex":"man"}
            params=urllib.urlencode(dic)
            page=urllib.urlopen("%s?%s"%(url,params))
            print "post request return:%s" %page.read()
        else:
            raise Exception("pass param format error.")
    else:
        raise Exception("param must not be Empty.")




def accessproxy():
    '''
    urllib代理设置
    :return:
    '''
    url = "http://www.enjoytoday.cn/posts/362"
    poxy="http://www.baidu.com"
    urllib.urlopen(url,proxies=poxy)




def transferUrl():
    '''
    url 和本地路径转化
    :return:
    '''
    path = "D://python/test/tt.txt"
    url=urllib.pathname2url(pathname=path)
    print "path transfer to url:%s" % url
    print "url transfer to path:%s" %urllib.url2pathname(url)


def encodeStr():
    '''
    字符串的编码和解码
    :return:
    '''
    s="飞云不在线%%_345&"

    quote_s=urllib.quote(s)
    quote_plus_s=urllib.quote_plus(s)
    unquote_s=urllib.unquote(quote_s)
    unquote_plus_s=urllib.unquote_plus(quote_plus_s)

    #encode
    print "quote encode:%s"%quote_s
    print "quote plus encode:%s"%quote_plus_s
    #decode
    print "quote decode:%s" % unquote_s
    print "quote plus decode:%s" % unquote_plus_s



if __name__=="__main__":
    #accessByUrllib()
    # requestMethod("POST")
    # transferUrl()
    encodeStr()
