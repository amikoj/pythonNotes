## python操作运算符

### 支持运算符


- 算术运算符
   基本运算符包括"+"、"-"、"*"、"/"、"%".除此之外还添加了幂运算符("**")和除法取整数部分运算符("//"),如下演示

```
#!/usr/bin/python
# -*- coding:utf-8 -*-
a=120
b=13
c1=a+b
c2=a-b
c3=a*b
c4=a/b
c5=a%b
c6=a//b
c7=a**b
print 'addition:',c1
print 'Subtraction：',c2
print 'multiplication：',c3
print 'division：',c4
print 'rest:',c5
print 'whole:',c6
print 'Exponentiation:',c7

#结果如下
addition: 133
Subtraction： 107
multiplication： 1560
division： 9
rest: 3
whole: 9
Exponentiation: 1069932053790720000000000000

```
  
- 比较（关系）运算符(所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。)
  1)===: 等于  - 比较对象是否相等 a==b
  2)!= : 不等于 - 比较两个对象是否不相等 a!=b
  3)<> : 不等于 -  比较两个对象是否不相等 a<>b
  4)>  :  大于 - 返回x是否大于y x>y
  5)<  : 小于 - 返回x是否小于y
  6)>= : 大于等于	- 返回x是否大于等于y
  7)<= : 小于等于 -	返回x是否小于等于y。

- 赋值运算符
  1)=
  2)+=
  3)-=
  4)*=
  5)/=
  6)%=
  7)**=
  8)//=
- 逻辑运算符
   1)&:与运算
   2)|:或运算
   3)^:异或运算
   4)~:非运算
   5)and:与运算
   6)or:或运算
   7)not:非运算
- 位运算符
   1)<<:左位移运算
   2)>>:右位移运算

- 成员运算符
  1)in 如果在指定的序列中找到值返回 True，否则返回 False
  2)not in  如果在指定的序列中没有找到值返回 True，否则返回 False	

   ```
    alist=['test1','test2',23,45]

    if 23 in alist:
        print "i get it."


   ```
- 身份运算符
  1)is 是判断两个标识符是不是引用自一个对象
  2)is not  是判断两个标识符是不是引用自不同对象
  ```
       
   aString = "simple string." 
   blist=['tt','bb']
   blist.append(aString)
   aTurpe=('aa',"bb",aString)
   print "blist:",blist
   print  "aTrupe:",aTurpe
   print "result:",(blist[2] is aTurpe[2])

  ```
- 运算符优先级 
