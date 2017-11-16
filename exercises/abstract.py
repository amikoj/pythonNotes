# !/usr/bin/env python
# -*- encoding:utf-8 -*-

import  sys

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


