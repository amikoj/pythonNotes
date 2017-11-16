#!/usr/bin/python   
# -*- encoding;utf-8 -*-

class User:
    'is a basic user info class'
    tag = "user"
    
    def __init__(self,*params):
        print "create %s" % self.__class__.__name__
        self.params=params

    def showName(self):
        print "this user name is:",self.params[0]
        return self.params[0]
    def __del__(self):
        #析构方法, 删除一个对象
        print "destory %s" % self.__class__.__name__
    
    
user= User("hfai",23,"monkey")
print user.showName(),"and params is:",User.tag

print "user dicts is:",User.__dict__
print "user doc is:",User.__doc__
print "user module:",User.__module__
print "user name is:",User.__name__
print "user bases is:",User.__bases__

#del user


#class about extends father
class SubClass(User):
    
    def __init__(self):
        
        print "this is origion function."
    def showName(self):
        print "this is children methods."
        return
    

a =SubClass()
a.showName()
a.showName()
    