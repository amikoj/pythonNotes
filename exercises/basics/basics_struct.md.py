#! /usr/bin/env python
# -*- encoding:utf-8 -*-

from  sys import path
import keyword


def main():
    list = ['testa', 'bbb', 123433, 40.6]
    a = ['test', 'a', 999]

    print list
    list[3] = 3
    a.append("bb") #追加一个变量
    a.pop()     #移除地一个变量
    a.count("a") #统计变量出现的次数
    list.extend(a) #追加列表
    print list[2:3]  # 分片操作
    index=list.index(a) #检索位置
    a.insert(2,12) #向‘2’位置添加一个参数12
    print list + a
    print list * 2

def ifFunction(param):
    if param=="Open":
        print "yes"
    elif param =="close":
        print "No"
    else:
        pass

    a=7
    while a>=0:
        if a==1:
            continue
        elif a==0:
            break
        else:
            a-=1
        print "a value:",a



    b="testbbb"
    for a in b:
        print a

    test=["A","B","C","D"]
    for a in range(10):
        print test[a]





if __name__ == '__main__':
    print(path)
    # age = input("How old are you ?")
    # print "your are %s years old." % age

    # raw_str=raw_input("get raw_input:")
    # print raw_str
    print keyword.kwlist