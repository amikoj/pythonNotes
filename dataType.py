#!/usr/bin/python
# -*- coding:utf-8 -*-
# fuction example statement.


#type convert functions

x=100;

#print int(x)          #将x转换为一个整数  
#print long(x)        # 将x转换为一个长整数  
#print float(x )               #将x转换到一个浮点数  
#print complex(1,2)  #创建一个复数  
#print str(x )                 #将对象 x 转换为字符串  
#print repr(x )                #将对象 x 转换为表达式字符串  
#print eval(str(x) )              #用来计算在字符串中的有效Python表达式,并返回一个对象  
#print tuple([a for a in str(x)] )             #  将序列 s 转换为一个元组  
#print list(a for a in str(x))                #将序列 s 转换为一个列表  
#print chr(x)                 #将一个整数转换为一个字符  
#print unichr(x )             # 将一个整数转换为Unicode字符  
#print ord(str(x)[0] )                 #将一个字符转换为它的整数值  
#print hex(x )                # 将一个整数转换为一个十六进制字符串  12
#print oct(x )                # 将一个整数转换为一个八进制字符串


#string operation

str = "this is about  stirng %s,and postion is %d" % ("test",123)
print str


#function format string
test ='''   this is test
pp'''
print test # repr()


#uncode 字符串

b= u'this is unicode string \u0021'
print b


## python 字符串内建函数

internal = "string of    internal function."

""" S.capitalize() -> string
Return a copy of the string S with only its first character
capitalized. """
print  internal.capitalize()   
""" S.center(width[, fillchar]) -> string
Return S centered in a string of length width. Padding is
done using the specified fill character (default is a space) """
print internal.center(200)
'''
Return the number of non-overlapping occurrences of substring sub instring S[start:end].  
Optional arguments start and end are interpreted as in slice notation.
'''
print internal.count("string") 
print internal.count("string",0,10) 
print internal.count("string",None,10) 
print internal.count("string",10) 

""" S.decode([encoding[,errors]]) -> object
Decodes S using the codec registered for encoding. encoding defaults
to the default encoding. errors may be given to set a different error
handling scheme. Default is 'strict' meaning that encoding errors raise
a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
as well as any other name registered with codecs.register_error that is
able to handle UnicodeDecodeErrors. """
print internal.decode("utf-8")
""" S.expandtabs([tabsize]) -> string

Return a copy of S where all tab characters are expanded using spaces.
If tabsize is not given, a tab size of 8 characters is assumed. """
print internal.expandtabs()


#List about

list1 = [x for x in  [1,3.5,6,'fdsf']]
print list1

print cmp(list1,(1,3.5,6,'fdsf'))
print cmp(list1,[1,3.5,6,'fdsf'])
print len(list1)
print max(list1)
print min(list1)
print list((1,3.5,6,'fdsf'))

print list1.reverse();

print range(5)

#tupple
list4=(23,)
print list4
