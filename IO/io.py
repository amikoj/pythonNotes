#!/usr/bin/python
# -*- coding: UTF-8 -*- 

#str = input("请输入：");
#print "你输入的内容是: ", str


## file operation

file1= open('./test.txt','wb+')

# write() function.
content = "http://www.enjoytoday.cn\n"
file1.write(content)
file1.write("add any")
file1.close()

file1= open('./test.txt','r+')
getString= file1.read(10)
file1.seek(0)
print "get String is:",getString+file1.read(10)



##rename
import os
##print "current path is:",os.path.realpath(file1)
os.rename(file1.name,'./tt.txt')


# file delete
#os.remove('./tt.txt')
#mkdir()
os.mkdir('test')



print "file close operation:",file1.close()
print "文件名: ", file1.name
print "是否已关闭 : ", file1.closed
print "访问模式 : ", file1.mode
print "末尾是否强制加空格 : ", file1.softspace


file.seek