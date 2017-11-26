# !/usr/bin/etc python
# -*-encoding:utf-8-*-

'魔法方法使用.'

#魔法方法

def magic():
    tuple=(12,"second data",76,987)
    #内建函数
    print len(tuple),"\n"
    #魔法方法
    print tuple.__len__()




if __name__ == "__main__":
    magic()
