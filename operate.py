#!/usr/bin/python
# -*- coding:utf-8 -*-

a=120
b=13
c1=a+b
c2=a-b
c3=a*b
c4=a/b
c5=a%b
c6=a//b
c7=a**b
print 'addition:',c1
print 'Subtraction：',c2
print 'multiplication：',c3
print 'division：',c4
print 'rest:',c5
print 'whole:',c6
print 'Exponentiation:',c7


alist=['test1','test2',23,45]

if 23 in alist:
    print "i get it."
    
    
aString = "simple string." 
blist=['tt','bb']
blist.append(aString)

aTurpe=('aa',"bb",aString)

print "blist:",blist
print  "aTrupe:",aTurpe

print "result:",(blist[2] is aTurpe[2])