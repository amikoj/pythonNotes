#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

#print '参数个数为:', len(sys.argv), '个参数。'
#print '参数列表:', str(sys.argv)
print  ' parmas:',sys.argv
print  'params numbers:',len(sys.argv)
print  'params details:',str(sys.argv)


#params 
a=b=c="this is test."
b="forcus changed."

a,b,c,d=1,34,"test",9
del a,b,d
#print a,b,c,
str = "this is test string."
print "str length is:",len(str)
print "string sub String is:",str[:5]
print "string sub String is:",str[-1:5]
print "string sub String is:",str[:-5]
print "string sub String is:",str[-1:]
print "string sub String is:",str[-5:]
print "string sub String is:",str[-1:-5]
print "string sub string qiepian:",str[::2]



#连接字符串
a = "test"
print a+'12'


#List
list =['testa','bbb',123433,40.6]
a=['test','a',999]

print list      
list[3]=3
print list[2:3]
print list+a
print list * 2


#tupple
tuple = ('tupple top',123,23.45,'tupple end')
t2 = (123.4,45,'tt',109)
print tuple
print t2
print  tuple[:4]
print tuple * 2
print tuple+t2


#dictionary
dict = {'key1':'value1','key2':23,2:"gg"}

print dict
print dict[2]
print dict.keys()
print dict.values()
dict2=dict.copy()
print dict2

print type(dict2)

print isinstance(2,int)

#k=list(t2)
#print k
