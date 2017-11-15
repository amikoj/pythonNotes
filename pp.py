#!/usr/bin/python
# -*- encoding:utf-8 -*-
#this file is add views for blog(csdn)
import time
import urllib


#climp web 
def climp(var1):
     if (var1 == None) and len(var1) == 0:
          return;
     else:
          try:
               page = urllib.urlopen(var1)
               html = page.read()
          except:
               print "climp error."
          else:
               print 'climp success'
               return html
          

with open('urls.txt','r+' ) as file1:
     for line in file1:
          print climp(line)
          
print "operation at date:",time.strftime(format('%Y%m%d    %H:%M:%S'))