# !/usr/bin/etc python
# -*-encoding:utf-8-*-

'魔法方法使用.'

#魔法方法



def magic(param):
    print  param

def magic():
    tuple=(12,"second data",76,987)
    #内建函数
    print len(tuple),"\n"
    #魔法方法
    print tuple.__len__()
    print  tuple.__str__()
    print tuple.__add__(("123",12)),tuple #add操作只能连接同类型数据,返回一个新的对象
    print tuple.__getitem__(1)



class A(object):
    def __init__(self):
        self.name="hfcai"
        self.sex="man"
        self.value=1234

    def __len__(self):
        return  10








class B(object):
     def __init__(self):
         '有关property函数的使用.'
         self.width = 10
         self.height=100



     def __call__(self, *args, **kwargs):
         print "[call,her,2]"


     def setSize(self,size):
         self.width,self.height=size

     def getSize(self):
         return self.width,self.height

     size=property(getSize)


     def staticMethod():
         print "this is a static  method."
     staticMethod = staticmethod(staticMethod)

     def classA(cls):
         print "this is class method"
     classA=classmethod(classA)


     @staticmethod  #装饰器
     def staticA():
         print "this is static A method."

     @classmethod
     def classA(cls):
         print "this is class A."


class Base(object):
    def __new__(cls, *args, **kwargs):
        print "__new__"
        return object.__new__(cls)


    def __init__(self):
        print "__init__"

    def __del__(self):
        print "__del__"

    @classmethod
    def A(cls):
        print "class method"


    @staticmethod
    def B():
        print "static method"


    def C(self):
        print "this is self"


    def __del__(self):
        print "__del__"

if __name__ == "__main__":
    # magic("tet")   #need attention, python function can not dup..,  it will override before function define of the same of function.
    # a=A()
    # print len(a)
    # magic()
    # b=B()
    # print b.size
    # print b.classA()
    # print B.classA()
    # print B.staticMethod()
    # print B.staticA()
    # a=iter(b,"2")
    # print  a.next()
    a = Base()
    try:
        print "Begin transfer-----------------------------call by instance."
        # call the class method
        a.A()
        # call static method
        a.B()
        # call the instance method
        a.C()

        print "Begin transfer------------------------------call by Class"
        # call the class  method
        Base.A()
        # call static method
        Base.B()
        # call instance method
        Base.C()
    except Exception as e:
        print e

    del a


