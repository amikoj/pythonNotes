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




if __name__ == "__main__":
    # magic("tet")   #need attention, python function can not dup..,  it will override before function define of the same of function.
    a=A()
    print len(a)
    magic()








