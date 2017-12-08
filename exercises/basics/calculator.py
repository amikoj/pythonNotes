#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# encoding: utf-8
# module calculator
"""
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.



"""

import sys

def addition(*args):
    """
    Addition Operation.
    :param args:  All the operands.
    :return: the result of operation.
    """
    if len(args) > 0:
        result = args[0]
        try:
            for operand in args[1:]:
                result += operand
        except Exception as e:
            print str(e)
            pass
        return result
    else:
        print "args must not be empty."
        raise Exception("args must not be empty.")


def subtraction(*args):
    """
    Subtraction Operation.
    :param args: All the operands.
    :return: the result of operation.
    """
    if len(args) > 0:
        result = args[0]
        try:
            for operand in args[1:]:
                result -= operand
        except Exception as e:
            print str(e)
            pass
        return result
    else:
        print "args must not be empty."
        raise Exception("args must not be empty.")


def monocular(operator, *args):
    """
     Simple Operation
    :param operator:  Operator for monocular operations
    :param args: All the operands.
    :return:the result of operation.
    """
    if len(args) > 0:
        result = float(args[0])
        try:
            for operand in args[1:]:
                if operator in "+":
                    result += float(operand)
                elif operator in '-':
                    result -= float(operand)
                elif operator in '*':
                    result *= float(operand)
                elif operator in '/':
                    result /= float(operand)
        except Exception as e:
            print str(e)
            pass
        return result
    else:
        print "args must not be empty."
        raise Exception("args must not be empty.")


if __name__ == "__main__":
    """
      By  external call.
    """
    # print "main step."
    # args of used.
    if len(sys.argv) >= 4:
        print sys.a
        args = sys.argv[1:]
        result = monocular(args[0], *(args[1:]))
        print "get result:", result

