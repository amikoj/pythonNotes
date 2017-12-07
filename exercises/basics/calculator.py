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
        result = args[0]
        try:
            for operand in args[1:]:
                if operator in "+":
                    result += operand
                elif operator in '-':
                    result -= operand
                elif operator in '*':
                    result *= operand
                elif operator in '/':
                    result /=operand
        except Exception as e:
            print str(e)
            pass
        return result
    else:
        print "args must not be empty."
        raise Exception("args must not be empty.")


if __name__ == "__main":
    """
      By  external call.
    """
    print "main step."
    # args of used.
    args = sys.argv
    monocular(args)
