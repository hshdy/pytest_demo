#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: test_app
# DATE: 20-7-1 12:54
--------------------------------------------
"""
import time
from contextlib import contextmanager

import coverage as coverage
import pytest


def start_hook():
    pass

def stop_hook():
    pass


@contextmanager
def coverage_context(source, debug=False, wait_running=6):
    cov = coverage.Coverage(source=source)
    if not debug:
        cov.start()
    start_hook()
    yield
    time.sleep(wait_running)
    stop_hook()
    time.sleep(2)
    if not debug:
        cov.stop()
        cov.html_report(directory="tests_html_report")



def run_pytest(cov_source, cov_debug=False, cov_wait = 6):
    with coverage_context(cov_source, debug=cov_debug, wait_running=cov_wait):
        # from tests.one_fn_test.test_add_function import TestAdd
        #
        # TestAdd().test_add()
        # for test one_fn_test
        pytest.main(['-s','./one_fn_test/'])


if __name__ == '__main__':
    run_pytest(['../src'],cov_wait=1)