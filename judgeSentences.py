#!/usr/bin/python
# -*- coding:utf-8 -*-
#basic Judge sentences.


a =10
b=5

if a>0 and b >0 and a >b:
    print "a is over b."
else:
    print "a is below b."
    
    
    
#循环判断    
alist = [34,56.32,455,"tets",'a']

for tt in alist:
    print "get value is",tt

for index,value in enumerate(alist):
    print "get index is:%d and value is: %s" %(index,str(value))
    
    
    
if  True : 
    pass
    print "pass code pass."