#!/usr/bin/env python
# -*-encoding:utf-8 -*-

'''
exception 使用介绍


'''

import exceptions






def exceptionDemo():
    '异常展示'
    #syntax error
    # str="just show syntax type error."
    #  print str,"\n"
    try:
        '捕获异常的代码执行片段'
        s = None
        a = 12
        print a * s
        print  "over"
    except IOError:         #except为异常发生触发运行片段关键词,可以指定内置异常类类型,采用匿名类型,不获取异常信息
        print "catch IOError."
    except TypeError as error: #捕获异常定义异常变量,新的API采用'as'来指定变量名称.
        print "catch TypeError.",error
    except (UnboundLocalError,BufferError):    #捕获异常定义捕获的异常类型可以使用元组的形式添加多个捕获的异常类型.
        pass          #pass无意义占位关键字
    except Exception,error:    #捕获异常Exception,将捕获所有的继承自Exception类型的异常,该种定义异常变量的方法属于老的api,新的api向下兼容.
        print "catch Exception and use \',\' define param.",error
    except:        #捕获所有的异常类型包括系统异常退出等.
        pass
    else:        #else为未发生异常执行的代码块，必须在except之后
        print "no catch any Exception."
    finally:    #finally不管有没有出现异常均会执行,可以和try单独使用,一般用于资源的关闭操作.
        print "alwanys run."








def buildInPythonException():
    '显示exceptions中的内容'
    print dir(exceptions),"\n"



def throwException():
    'python抛出异常的方法'
    #1
    # raise Exception
    # raise Exception("throw exception")
    raise DefException("def exception.")




def catchException():
    'python中捕获异常的方法'
    #method 1
    try:
        print  (10/0)
    except:
        print "catch the Exception."
        pass


def raiseException():
    '异常触发抛出'
    a = 12
    s = None
    try:
        print a * s
    except Exception as error:
        if a < 10:
            pass
        else:
            raise



class DefException(Exception):
    pass



class CustomerException(Exception):
    KEY_CODE="code"
    KEY_MESSAGE="message"
    def __init__(self,**args):
        self.code=args[CustomerException.KEY_CODE]
        self.message=args[CustomerException.KEY_MESSAGE]

    def __str__(self):
        print repr(" throw code:%s,message:%s" % (self.code,self.message))


if __name__ == "__main__":
    # buildInPythonException()
    # throwException()
    # catchException()
    # exceptionDemo()
    # error = IOError("the file is not exists.")
    # raise error
    # raiseException()
    # raise DefException("Def Exception")
    # raise CustomerException(code=21,message="this is customer Exception")
    with open(name="./struct.py",mode="rb+")  as file:
         print file.read()






