## python 判断语句

### 条件判断语句
格式：
```
if 判断条件:
   代码片段
elif 判断条件:
   代码片段
else:
   代码片段
```

**注意,python并不支持switch语句.**
```
a =10
b=5

if a>0 and b >0 and a >b:
    print "a is over b."
else:
    print "a is below b."
```


## python 循环判断语句

- while循环
  while 判断条件：
    执行语句……

- for循环

   
   for iterating_var in sequence:
       statements(s)

   for index, item in enumerate(sequence):
      process(index, item)
  
 ** TypeError: cannot concatenate 'str' and 'int' objects** 
   python组合字符串时不要用"+"连接字符串

   for循环的两种方式:
```
  for tt in alist:
    print "get value is",tt

  for index,value in enumerate(alist):
    print "get index is:%d and value is: %s" %(index,str(value))


```
 
## break
  和Java一样，退出循环。

## continue
  和java一样，结束当前代码块，进行下次循环操作.



## pass语句
   pass不做任何事情，一般是为了保证语法格式的完整性。
  

  ```
       
  if  True : 
    pass
    print "pass code pass."

  ```

 虽然pass并未做任何事情，但还是需要遵守整体的代码格式要求，保证代码格式的一致.





