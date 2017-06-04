## Python 函数



### 函数定义
- 定义格式


def function(params...):
     statement;
     return expresssion;


示例:

```
#!/usr/bin/python
# -*- encoding:utf-8 -*-
##functions introduce.

def function(var1=None,var2=None):
    print "this is a simpe function define style."
    return


function();
```

### 参数传递
在 python 中，类型属于对象，变量是没有类型的.
1)可更改(mutable)与不可更改(immutable)对象
  - 不可更改类型:string、tuples、numbers(传递的是对象，指向的引用变化不会影响结果)
  - 可更改类型:list、dict(传递过去的是引用本身，引用修改，结果会发生改变)

  代码如下:


```
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



## 结果如下:
var1 is a list data.
this var1 is changed to : ['this ', 'is update', ' list']
['this ', 'is update', ' list']
var1 is a tuple data
this var1 is changed to : (1, 2, 3, 4, 5, 11, 22, 33)
(1, 2, 3, 4, 5)

```


2) 参数类别
- 必备参数
  无多余声明操作的参数声明,如def function(var1):statement;其中var1就为必备参数
- 关键字参数
  函数调用使用关键字参数来确定传入的参数值。使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为
  Python 解释器能够用参数名匹配参数值。示例如下:
  ```
    #key word params
    def function2(var1,var2):
        print "we can get var1=",var1," and var2 =",var2
        return


    function2(var1="this is ",var2="test")
    function2(var2="this is ",var1="test")

    #结果如下
    we can get var1= this is   and var2 = test
    we can get var1= test  and var2 = this is 

  ```



- 默认参数
   缺省默认参数，在函数定义时已经赋值了一个默认值，若参数未传入，则传入默认值。代码如下:

   ```
   #default param
   def function3(var1="defalut param"):
       print "get param is:",var1
       return

   function3()
   function3("test")

   ```
- 不定长参数
  可以传入多个参数，定义格式: def function(*args):statement;感觉和指针很像.传入的args是一个元组类型参数。使用示例如下:
```
def function4(*agrs):
    print agrs
    return


function4("this is test")
function4("this","is","test")

#结果显示
('this is test',)
('this', 'is', 'test')

```


### 匿名函数
python 使用 lambda 来创建匿名函数。
- lambda只是一个表达式，函数体比def简单很多。
- lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
- lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。- 
- 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。


1)语法
  lambda arg1,arg2,arg3:experssion


2)示例

```
# lambda
 
test = lambda var1,var2: var1+var2;

print test("10","12")

```





### 变量作用域
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。全局变量想要作用于方法中需要使用global声明,示例如下:


```
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

#结果
before a: tt
after: after
after: after

```







