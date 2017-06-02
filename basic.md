## python基本使用规范和语法基础


## python文件格式

python 文件后缀为*.py
python 基本头信息,编码名称不限制大小写.

```
# !/usr/bin/python
# -*- coding: UTF-8 -*-

```
#!/usr/bin/python这句话可以让已经有运行权限的py文件直接通过 ./*.py直接运行(linux、unix)


运行方法:
```
#python *.py

```

## 语法规范

+ python中的标识符由字母、数字、下划线组成，但不能以数字开头
+ python对大小写敏感
+ python对格式敏感
+ 以下划线开头的标识符如:_foo表示不能直接访问的类属性，需要通过类提供的接口进行访问,不可由 from xxx import *导入
+ 双下划线开头的标识符如:__foo代表类的私有成员；以双下划线开头和结尾的如:__foo__代表python中的特殊方法标识，如 __init__() 代表类的构造函数。
+ python可以一行显示多条语句(通过;隔开)，也可以一行显示一条语句而不使用;结束。
+ python 保留字符，这些保留字不能用作常数或变数，或任何其他标识符名称。所有 Python 的关键字只包含小写字母。
and	        exec    	not
assert  	finally 	or
break	        for	        pass
class   	from	        print
continue	global	        raise
def	        if	        return
del	        import      	try
elif	        in       	while
else        	is	        with
except  	lambda	        yield
  

+ 代码块
python通过缩进进行模块编写，缩进的空白数量是可变的。但是所有的代码块必须包含相同的缩进空白数量

+ python可以通过使用 '\'反斜杠将一行语句分为多行连接起来(是执行语句不是字符串)，若语句中包含[],{},()则无须使用反斜杠连接，其本身有连接作用。

+ python字符串表示方法:python可以使用单引号('),双引号("),三引号('''或者""")来表示，其中三引号可以由多行组成，编写多行文本的快捷语法，常用语文档字符串，在文件的特定地点，被当做注释。

```
a = '''这是三引号
使得```
   
```
+ python注释:单行注释(#)、多行注释使用三个单引号(''')或三个双引号(""")。
+ python的代码块之间使用空行隔开(代码格式和维护要求)

## python I/O

1) 输入
   python 输入可以使用input("")或者raw_input("")接受输入，input只能接受基本类型的输入，字符串不支持输入，字符串输入可以使用raw_input实现。
2) 输出
    - print 基本输出，默认输出可以换行，如果不需要换行怎需要在变量末尾加上逗号
    
## python代码组
缩进相同的一组语句构成一个代码块，称之为代码组。如if、elif、else、while、def、class等复合语句，首行以关键字开始，以冒号(:)结束，行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。代码格式如下:

```
def name(var_name):
   a=var_name
   print a


```

## 命令行参数
运行py程序时传入的一些参数，我们可以通过sys来获取。其中，sys.argv为参数列表，len(sys.argv)为参数个数，其中第一个参数为脚本文件名(即sys.argv[0])




