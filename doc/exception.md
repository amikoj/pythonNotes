## Python 异常处理


### python 标准异常
BaseException 所有异常的基类
SystemExit    解释器请求退出
KeyboardInterrupt 用户中断执行(通常是输入^C)
Exception 常规错误的基类
StopIteration	迭代器没有更多的值
GeneratorExit	生成器(generator)发生异常来通知退出
StandardError	所有的内建标准异常的基类
ArithmeticError	所有数值计算错误的基类
FloatingPointError	浮点计算错误
OverflowError	数值运算超出最大限制
ZeroDivisionError	除(或取模)零 (所有数据类型)
AssertionError	断言语句失败
AttributeError	对象没有这个属性
EOFError	没有内建输入,到达EOF 标记
EnvironmentError	操作系统错误的基类
IOError	输入/输出操作失败
OSError	操作系统错误
WindowsError	系统调用失败
ImportError	导入模块/对象失败
LookupError	无效数据查询的基类
IndexError	序列中没有此索引(index)
KeyError	映射中没有这个键
MemoryError	内存溢出错误(对于Python 解释器不是致命的)
NameError	未声明/初始化对象 (没有属性)
UnboundLocalError	访问未初始化的本地变量
ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError	一般的运行时错误
NotImplementedError	尚未实现的方法
SyntaxError	Python 语法错误
IndentationError	缩进错误
TabError	Tab 和空格混用
SystemError	一般的解释器系统错误
TypeError	对类型无效的操作
ValueError	传入无效的参数
UnicodeError	Unicode 相关的错误
UnicodeDecodeError	Unicode 解码时的错误
UnicodeEncodeError	Unicode 编码时错误
UnicodeTranslateError	Unicode 转换时错误
Warning	警告的基类
DeprecationWarning	关于被弃用的特征的警告
FutureWarning	关于构造将来语义会有改变的警告
OverflowWarning	旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning	关于特性将会被废弃的警告
RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
SyntaxWarning	可疑的语法的警告
UserWarning	用户代码生成的警告



### 异常处理
捕捉异常可以用try/except语句，代码格式为  try: statement;except Exception,msg:statement;else:statement;如下示例:

```

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



#结果
value error: invalid literal for int() with base 10: ''
try statement is over
this is exception catch 
file write success.


```


### 异常触发

触发异常的语法格式: raise Exception,args,traceback
Exception:异常类型
args:异常内容
traceback:异常跟踪路径
示例如下:

```
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

```


### 自定义异常
自定义异常一般通过继承Exception类实现，传入错误提示,如下:

```
# define customer exception
class CustomerException(Exception):
   def __init__(self,*args):
      self.args=args

```

如上,python中类的创建格式：

```
 class name(fatherClass):         #若不需要继承的话直接使用 class name:即可。
    def __init__(self)
        print "这是构造函数，必须.后面可以添加其他参数."


a=name()
````





## 其他异常
1)assert 
  代码格式:asset False,'error msg.';print "msg"; assert 后面的语句是True继续执行print，false的话中断程序，同时输出assert语句逗号后的error提示信息。
2with ... as
  代码格式如下:
```
  with open('test.txt','w+') as file1:
   file1.read()
   print "read success."
  print "continue"


```
文件的流对象的操作，调用默认的异常处理器处理，但文件也会正常关闭.
















