#!/usr/bin/python
# -*- encoding:utf-8 -*-
##functions introduce.

def function(var1=None,var2=None):
    print "this is a simpe function define style."
    return


function();



def functions(var1):
    if isinstance(var1,list):
        print "var1 is a list data."
        var1[1]="is update"
    elif isinstance(var1,tuple):
        print "var1 is a tuple data"
        var1+=(11,22,33)
    print "this var1 is changed to :",var1
    return

#mutable
list1=["this ","is "," list"]
functions(list1)
print list1

#immutable
tuple1=(1,2,3,4,5)
functions(tuple1)
print tuple1


#key word params
def function2(var1,var2):
    print "we can get var1=",var1," and var2 =",var2
    return


function2(var1="this is ",var2="test")
function2(var2="this is ",var1="test")


#default param
def function3(var1="defalut param"):
    print "get param is:",var1
    return

function3()
function3("test")


def function4(*agrs):
    print agrs
    return


function4("this is test")
function4("this","is","test")


# lambda
 
test = lambda var1,var2: var1+var2;

print test("10","12")


#变量作用域
a = "tt"
 
def function5():
    global a
    print "before a:",a
    a="after"
    print "after:",a
    return 

function5()
print "after:",a


age = 12;
print "my age is:%s"%age

