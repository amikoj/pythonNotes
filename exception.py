#!/usr/bin/python
# -*- encoding:utf-8 -*-


#exception handler
a=12;
string =""
try:
   string="this is exception catch "
   var=""
   int(var)
except TypeError,Argument:
   string ="get exception.",Argument
except ValueError, Argument:
   print "value error:",Argument
else:
   string = "no exception"
finally:
   print "try statement is over"
print string;


#try:
   #print aa
#finally:
   #print "test has not contain exception."
#print "this is test."

# file operation exception

try:
   file1=open('test.md','wb+')
   file1.write("this is test file.")
except IOError:
   print "file can not open or write"
else:
   print "file write success."
   file1.flush()
   file1.close()
   
   
#throw exception
def function(var):
   if isinstance(var,str):
      raise Exception("Invalid var!")
   elif isinstance(var,int):
      print "this params is:",var
   return


try:
   function("test")
except Exception,msg:
   print "get exception is:",msg
else:
   print "function no find exception."
finally:
   print "function run over."


def function2(var=None):
   if var==None:
      raise NameError("not find params.")
   else:
      print "this parmas is :",var
   return

try:
   function2()
except NameError,msg:
   print msg
else:
   pass
finally:
   print "this is a test about exception create."


# define customer exception
class CustomerException(Exception):
   def __init__(self,*args):
      self.args=args
      
#-----exception calculator-------      
class Muffledcalculator:
   def __init__(self):
      print "this is gouzao hanshu."
   muffled = False
   def calc(self,expr):
      try:
         raise CustomerException("customer excepton.")
      except CustomerException,msg:
         if self.muffled:
            print "get exception and msg is:",msg
         else:
            raise
      
try :
   Muffledcalculator().calc('test')
except CustomerException,msg:
   print "get CustomerException,and msg is:",msg
finally:
   print "customer exception is final."