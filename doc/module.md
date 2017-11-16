## Python 模块
Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。模块能定义函数，类和变量，模块里也能包含可执行的代码。




## 使用

1)import 导入
import modulelname
多个模块:import modulename1,name2,name3
调用module中的函数: module.function,示例如下:


```
#!/usr/bin/python
# -*- encoding:utf-8 -*-

import module1;
module1.function()

```


2)from moduleName import functionName1,name2,name3格式导入


  ```
   from module1 import function
   function()

  ```

3)from moduleName import * 格式导入
  把一个模块的所有内容全都导入到当前的命名空间


4)模块搜索路径
  - 运行py当前目录
  - shell变量中的PYTHONPATH下的每个路径
  - 默认python安装路径



5)reload()函数
  当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。因此，如果你想重新执行模块里顶层部分的代 码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法格式为:reload(module_name)



## Python 中的包
包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。也就是处理自定义模块的导入问题.格式为:from packageName.moduleName import functionName;
- python 调用的module 需要和导入的PackageName在同一级目录
- 每一个package下需要放一个__init__.py文件,可以为空不写任何代码


## 系统相关模块
1) import sys
   sys.argv 是一个 list,包含所有的命令行参数. 
   sys.stdout sys.stdin sys.stderr 分别表示标准输入输出,错误输出的文件对象.
   sys.stdin.readline() 从标准输入读一行 sys.stdout.write("a") 屏幕输出a 
   sys.exit(exit_code) 退出程序 
   sys.modules 是一个dictionary，表示系统中所有可用的module
   sys.platform 得到运行的操作系统环境 
   sys.path 是一个list,指明所有查找module，package的路径. 

2) import os
   os.environ 一个dictionary 包含环境变量的映射关系 
   os.environ["HOME"] 可以得到环境变量HOME的值 
   os.chdir(dir) 改变当前目录 os.chdir('d:\\outlook') 注意windows下用到转义
   os.getcwd() 得到当前目录 
   os.getegid() 得到有效组id os.getgid() 得到组id
   os.getuid() 得到用户id os.geteuid() 得到有效用户id
   os.setegid os.setegid() os.seteuid() os.setuid()
   os.getgruops() 得到用户组名称列表 
   os.getlogin() 得到用户登录名称 
   os.getenv 得到环境变量
   os.putenv 设置环境变量
   os.umask 设置umask
   os.system(cmd) 利用系统调用，运行cmd命令
  
3)内置模块(不需要import可以直接访问)
  help(obj) 在线帮助, obj可是任何类型 
  callable(obj) 查看一个obj是不是可以像函数一样调用
  repr(obj) 得到obj的表示字符串，可以利用这个字符串eval重建该对象的一个拷贝
  eval_r(str) 表示合法的python表达式，返回这个表达式
  dir(obj) 查看obj的name space中可见的name
  hasattr(obj,name) 查看一个obj的name space中是否有name
  getattr(obj,name) 得到一个obj的name space中的一个name 
  setattr(obj,name,value) 为一个obj的name 
  space中的一个name指向vale这个object 
  delattr(obj,name) 从obj的name space中删除一个name
  vars(obj) 返回一个object的name space。用dictionary表示
  locals() 返回一个局部name space,用dictionary表示 
  globals() 返回一个全局name space,用dictionary表示 
  type(obj) 查看一个obj的类型
  isinstance(obj,cls) 查看obj是不是cls的instance 
  issubclass(subcls,supcls) 查看subcls是不是supcls的子类
  ##################    类型转换  ##################

  chr(i) 把一个ASCII数值,变成字符
  ord(i) 把一个字符或者unicode字符,变成ASCII数值
  oct(x) 把整数x变成八进制表示的字符串
  hex(x) 把整数x变成十六进制表示的字符串
  str(obj) 得到obj的字符串描述
  list(seq) 把一个sequence转换成一个list
  tuple(seq) 把一个sequence转换成一个tuple
  dict(),dict(list) 转换成一个dictionary 
  int(x) 转换成一个integer
  long(x) 转换成一个long interger 
  float(x) 转换成一个浮点数 
  complex(x) 转换成复数
  max(...) 求最大值 
  min(...) 求最小值






