# !/usr/bin/env python
# -*-encoding:utf-8 -*-

'''
underline use introduce.





'''

class UnderLine:
     tip="tips"
     _singleUnderLine="single"  #the single underline variable of class member.
     __doubleUnderLine="double" #double underline variable of class member.
     def __init__(self):
          'test about underline use'
          self.description="under line class is referer to variable create."
          self._single="self single"
          self.__double="self double"
          self.__doubleMethod()
          self._singleMethod()


     def _singleMethod(self):
          'single underline method'
          print "just get a mehod which is defined _* \n"

     def __doubleMethod(self):
          'double underline method'
          print 'just get a method which is definde with double underline.'








if __name__ == "__main__":
     underline=UnderLine()
     underline._singleMethod()
     UnderLine.tip
