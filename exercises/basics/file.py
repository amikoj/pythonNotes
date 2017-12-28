#!/usr/bin/env python
#-*-encoding:utf-8-*-
import  sys,fileinput,codecs


testFile = file('file.py')
# 文件读操作
# print testFile.read()
# 文件单行读操作.
print testFile.readline()
# 文件单行制定字符读操作.
print testFile.readline(3)
# 文件读所有行,并返回一个list.
# print testFile.readlines()
print "file name:",testFile.name
# 文件迭代
print testFile.next()
print next(testFile)

# 返回一个整型的文件描述符,可供底层操作系统调用.
print testFile.fileno()

try:
    testFile.write("test")
except Exception as e:
    print e

# 关闭文件
testFile.close()



# with  open(name="file.py",mode='wb+',buffering=1024,) as testFile:
#     testFile.write("print \"append mode------------------------------ \"")
#     testFile.flush()
#     print testFile.read()

#
# with  open(name="file.py",mode='a',buffering=1,encoding='utf-8') as testFile:
#     testFile.write("print \"append mode------------------------------ \"")
#     testFile.flush()
#     testFile.seek(0)
#     print testFile.read()


testFile = fileinput.input('file.py')

for line in testFile:
    print line
# print testFile.filename()

for line in fileinput.input('file.py'):
    print line
    testFile.close()
    break


with codecs.open('file.py','rb',encoding='utf-8') as testFile:
    print testFile.read()


# print help(open)
# print file.__doc__
# print "append mode------------------------------ "