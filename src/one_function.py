#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: one_function
# DATE: 20-7-1 12:26
--------------------------------------------
"""

def add_function(a,b):
    print("a is {},b is {}".format(a,b))
    if not isinstance(a,int):
        return Exception('parameter a must int')
    if not isinstance(b,int):
        raise Exception('parameter b must int')
    c = a+ b
    return c
