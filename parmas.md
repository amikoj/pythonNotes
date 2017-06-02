## python变量
变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间。基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。


### 赋值
1) python中变量赋值不需要类型声明
2) 每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
3) 变量使用前必须赋值，变量赋值后才可被创建
4) 变量赋值格式: a = 12
5) python允许多个变量同时赋值，格式为: a = b = c =100或者a,b,c,d=1,34,"test",99


### 标准数据类型
python 定义了五个标准数据类型:
- Numbers(数字)
- String(字符串)
- List(列表)
- Tupple(元组)
- Dictionary(字典)

#### Numbers(数字)
数字数据类型为不可改变数据类型，当改变数字数据类型对象时会分配一个新的对象

1) 创建
   可以直接通过赋值方式创建一个数字数据类型对象，每赋值一个数字类型就会创建一个新的对象。格式为:var1=101
2) 删除
   通过del语句删除 del var1,var2,...,varN
3) 支持类型
    - int(有符号的整型)
    - long(长整型[也可代表八进制和十六进制]):长整型也可以使用小写"L"，但是还是建议您使用大写"L"，避免与数字"1"混淆。Python使用"L"来显示长整型。
    - float(浮点型)
    - complex(复数)
    

#### String(字符串)
字符串由数字、字母、下划线组成的一串字符。
1) 取值方式
  python中有两种方式对当前的字符串进行取值:
  - 从左到右取值默认从0开始，最大范围为字符长度减1
  - 从右到左取值默认从-1开始。
2) 截取字串格式: str[begin:over]下标可以为0表示从头开始或到尾部截止。注意begin指定的字符需要在over左侧，否则无法取到。
3）切片操作:str[begin:over:step],对str截取后的字符串以step步长进行切片分割。


### List(列表)
python 中使用最频繁的数据结构，可以完成大多数集合类结构的数据结构实现。支持字符、数字、字符串以及列表。通过[]进行标识，列表的截取方式和String的字串截取方式相同.[begin:over]
1)加号(+)是列表连接运算符，星号(*)是重复操作。如下案例:

```
#List
list =['testa','bbb',123433,40.6]
a=['test','a',999]

print list
list[3]=3
print list[2:3]
print list+a
print list * 2

```


### Tupple(元组)
元组类似与List，但是元组不可二次赋值，使用()标志，同样通过逗号分割,tupple的获取和List方法相同。如下为用法示例:

```

#tupple
tuple = ('tupple top',123,23.45,'tupple end')
t2 = (123.4,45,'tt',109)
print tuple
print t2
print  tuple[:4]

#tuple[3]=3  //该操作无效，元组不允许修改更新
print tuple * 2
print tuple+t2


```


### Dictionary(字典)
类似与List,List有序、Dictionary无序(类似与Java中的map,通过key-value方式存储)，格式通过{key:value,....}赋值。和json数据格式很相像.如下，给出一个简单的操作示例:


```
  #dictionary
dict = {'key1':'value1','key2':23,2:"gg"}

print dict
#print dict[0] //这种操作是不合法的
print dict[2]
print dict.keys()
print dict.values()
dict2=dict.copy()
print dict2


```


### 数据类型转化
通过函数实现数据类型的转换。对应函数如下:

int(x [,base])             将x转换为一个整数
long(x [,base] )           将x转换为一个长整数
float(x)                   将x转换到一个浮点数
complex(real [,imag])      创建一个复数
str(x)                     将对象 x 转换为字符串
repr(x)                    将对象 x 转换为表达式字符串
eval(str)                  用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)                   将序列 s 转换为一个元组
list(s)                    将序列 s 转换为一个列表
set(s)                     转换为可变集合
dict(d)                    创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)               转换为不可变集合
chr(x)                     将一个整数转换为一个字符
unichr(x)                  将一个整数转换为Unicode字符
ord(x)                     将一个字符转换为它的整数值
hex(x)                     将一个整数转换为一个十六进制字符串
oct(x)                     将一个整数转换为一个八进制字符串

### 参数数据类型判断获取

1)通过type(param)返回参数类型，显示如下格式:

```
<type 'dict'>
```

2)通过isinstance 来判断,如下:

```

print isinstance(2,int)

##结果如下：
True


```



### 注意
1)尽量不要使用内部函数名作为变量的名称，否则在使用该内部函数的时候回报:TypeError: 'list' object is not callable错误；
2)数据类型分为数字型和非数字型。数字型包括整型，长整型，浮点型，复数型；非数字型包括字符串，列表，元组和字典 ；
3)非数字型的相同点:都可以进行切片、连接(+)、重复(*)、取值([])等相关操作；
4)非数字型不同点:列表可以直接赋值并对其进行更新修改，元组赋值后不可更改，字典通过(key,vlaue)存储，通过key取值进行更新修改。






