## python常用的内置函数



### 类型转换函数


```
#type convert functions

x=100;

print int(x)          #将x转换为一个整数  
print long(x)        # 将x转换为一个长整数  
print float(x )               #将x转换到一个浮点数  
print complex(1,2)  #创建一个复数  
print str(x )                 #将对象 x 转换为字符串  
print repr(x )                #将对象 x 转换为表达式字符串  
print eval(str(x) )              #用来计算在字符串中的有效Python表达式,并返回一个对象  
print tuple([a for a in str(x)] )             #  将序列 s 转换为一个元组  
print list(a for a in str(x))                #将序列 s 转换为一个列表  
print chr(x)                 #将一个整数转换为一个字符  
print unichr(x )             # 将一个整数转换为Unicode字符  
print ord(str(x)[0] )                 #将一个字符转换为它的整数值  
print hex(x )                # 将一个整数转换为一个十六进制字符串  
print oct(x )                # 将一个整数转换为一个八进制字符串


#结果返回
100
100
100.0
(1+2j)
100
100
100
('1', '0', '0')
['1', '0', '0']
d
d
49
0x64
0144


```

### 伪随机数获取
1)random.choice( seq  ):从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
2)seed([x]):改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。



### python 数学常量
1)pi:数学常量 pi（圆周率，一般以π来表示）
2)e:数学常量 e，e即自然常数（自然常数）。


## Python转义字符 

\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\a	响铃
\b	退格(Backspace)
\e	转义
\000	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
\f	换页
\oyy	八进制数，yy代表的字符，例如：\o12代表换行
\xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
\other	其它的字符以普通格式输出

## python 字符串运算符

特别注意： r/R 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。

使用: print r"\n"或者 print R"\n"(注意需要连接在一起写)


字符串连接方式通过%s、%d、%f占位符进行占位。格式如下:

```
str = "this is about  stirng %s,and postion is %d" %("test",123)
```








