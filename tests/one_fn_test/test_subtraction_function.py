#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: test_subtraction_function
# DATE: 20-7-1 15:58
--------------------------------------------
"""
import sys

sys.path.append('../src')

from two_function import subtraction_function


class TestSubtraction(object):
    def setup_class(self):
        """测试开始时候执行, 用来做准备工作，一般用来初始化资源。"""
        print("into TestSubtraction setup_class")

    def teardown_class(self):
        """测试结束时执行， 用来做收尾工作， 一般用来关闭资源"""
        # logger.info("pytest over")
        print("into TestSubtraction teardown_class")

    def test_add(self):
        result = subtraction_function(6, 4)
        print('result is {}'.format(result))
        assert result == 2
