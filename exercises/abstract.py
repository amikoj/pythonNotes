# !/usr/bin/env python
# -*- encoding:utf-8 -*-

import  sys,bisect

'''
抽象学习
'''


def usefibs(one,two,rang):
    '''
    模拟斐波那契数
    :return: 返回计算结果
    '''
    fibs=[one,two]
    print  rang
    for x in range(rang[0],rang[1],rang[2]):
        fibs.append(fibs[-2]+fibs[-1]) #添加一个前两个数相加的新数字
    return fibs

def parametric(param):
    '''
    形式参数修改列表(list)
    :param param:
    :return:
    '''
    param[0]=12



def functionJudge():
    '''
    用于函数判断,通过内联函数 :callable(),python 3.0不再使用.
    :return: 返回判断结果
    '''
    x=usefibs   #不带有参数，仅仅表示方法本身.
    return  callable(x)


def zipExec(title,description):
    return zip(title,description)



def collectionParams(title,*params):
    '''
    测试收集函数,类似于指针变量
    :param title:
    :param params:
    :return:
    '''
    print "title:",title
    print "\nparmas:",params



def collectionDict(**dict):
    '''
    测试收集参数,类似于指针的指针.
    :param dict:
    :return:
    '''
    print "dict %(name)s" % dict       # "%(key)s" % dict 指定指定key的字典的数值.


tip="global param"
no_same="no same param"

def squareParam():
    '''
    测试同名或者不同名的全局变量在方法区间内的使用,和在方法内定义全局变量
    :return:
    '''
    global method    #声明全局，但不可直接赋值
    method="method"
    tip="method parm"
    print "normal:",tip,no_same
    print  "global:",globals()['tip'],no_same #内建函数，返回全局变量的数值



if __name__=="__main__":
    #fbis
    print usefibs(2,4,(0,15,1))
    print "usefibs is can use" if functionJudge() else "usefibs() is not use."
    print "访问文档字符串:",usefibs.__doc__    #__doc__是函数属性
    #help(usefibs) #内建函数,获取基本函数信息
    list=[10,45,76]
    print list
    parametric(list)
    print  list
    dict={}
    dict['name']=['hfcai']
    dict.setdefault("name",[]).append(4)
    print dict
    a= dict.setdefault
    print a.__doc__
    print zipExec("hfcai","is a man people.")

    collectionDict(name="hfcai",value="name")

    b=1
    print vars(usefibs)  #内建函数
    squareParam()
    print method



