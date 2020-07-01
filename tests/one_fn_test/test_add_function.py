#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: test_add_function
# DATE: 20-7-1 12:30
--------------------------------------------
"""

import sys

import pytest

from tests.test_app import coverage_context

sys.path.append('../src')

from one_function import add_function


class TestAdd(object):
    def setup_class(self):
        """测试开始时候执行, 用来做准备工作，一般用来初始化资源。"""
        print("into setup_class")

    def teardown_class(self):
        """测试结束时执行， 用来做收尾工作， 一般用来关闭资源"""
        # logger.info("pytest over")
        print("into teardown_class")

    def test_add(self):
        result = add_function(4, 6)
        print('result is {}'.format(result))
        assert result == 10


if __name__ == '__main__':
    with coverage_context(['../src', './'], debug=False, wait_running=1):
        # pytest.main(["-s","test_add_function.py"])
        pytest.main(["--cov=./src", "--cov-report=html"])
