#!/usr/bin/python
# -*- encoding:utf-8 -*

##build-in function

#static function,two methods to create staticmethod,and use className.methodName(...)
class Test:
    def __init__(self):
        print "this is create function."
        
    def test():
        print "this  is a normal function."
        return
    test=staticmethod(test)
    
    @staticmethod
    def f():
        print "the second methods to changed static method."
    
    
Test.test()
Test.f()


#all,judge if or not exists param is 0 or None in List,tuple.if exists return False ,else return True.
print all((1,2,3,4))
print all([1,0,9,4])


#enumerate(), iterator for index, value of iterable

list1=["","test",1,453,"peek","hacker",0]
dicts={1:"dicts tst.","key":"value"}
for i,element in enumerate(list1):
    print "index is:%d,and element is:%s" % (i,element)
    
#any() 函数用于判断给定的可迭代参数 iterable 是否全部为空对象，如果都为空、0、false，则返回 False，如果不都为空、0、false，则返回 True。

print any([''])


#eval(expression,globals,locals) use excute string statement.
#expression -- 表达式。
#globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
#locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
print eval('2 * list1')


#execfile() use execute a file. execfile(filename,globals,locals)
#filename -- 文件名。
#globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
#locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
print execfile('test.sh')

#next() 返回迭代器的下一个项目。next(iterator)
iter1=iter(list1)
while True:
    try:
        x=next(iter1)
        print x
    except StopIteration:
        break
    
#exec 执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。exec object

'''
需要说明的是在 Python2 中exec不是函数，而是一个内置语句(statement)，但是Python 2中有一个 execfile() 函数。
可以理解为 Python 3 把 exec 这个 statement 和 execfile() 函数的功能够整合到一个新的 exec() 函数中去了。
'''
exec 'print "Hello World"'



x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
    
func()