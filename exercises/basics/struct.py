#!/usr/bin/env python
# -*-encoding:utf-8 -*-

# multi=lambda x,y:x*y #lambda关键字定义,以':'分割，左边为参数列表，右边为返回结果的表达式
# print multi(2,3)


def function(var1,var2="test"):
    "only print parameter."
    print var1,var2



# help(function)
# function("need","help")
# function(var2="var2",var1="var1")
# function("var1")



class TestClass:
    DESCRIPTION = "class introduction"  # 类变量，可直接通过类名调用
    __test = "test"  # 属于私有，不可在类外部直接调用以“__”开头
    _single = "single"  # 属于私有,不可使用from module import *导入使用

    def __init__(self,name):
        '测试类'
        self.name=name #通过self可以创建类的实例变量
        print TestClass.__test
        print TestClass._single




    def getName(self): #类的成员方法
        return self.name

    def __getName(self): #private
        return TestClass._single

    @staticmethod
    def getsingele():   #类的静态方法
        return TestClass.__test



# print TestClass.DESCRIPTION
# print TestClass.getsingele()
# test=TestClass("hfcai")
#
# print test.name
# print test.getName()
# print TestClass.getName(test)











class A:       #旧式类
    def __init__(self):
        print "classic type."


class B(object):  #新式类
    def __init__(self):
        print "new style type. one"



__metaclass__ =type
class C:               #新式类
    def __init__(self):
        print "new style type. two"






a=A()
b=B()
c=C()

print "class A __class__:%s,type:%s \n"% (a.__class__,type(a))

print "class B __class__:%s,type:%s \n"% (b.__class__,type(b))

print "class C __class__:%s,type:%s \n"% (c.__class__,type(c))













