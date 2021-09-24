#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__title__  =
__Time__   = 2020-04-06 11:40
__Author__ = 小菠萝测试笔记
__Blog__   = https://www.cnblogs.com/poloyy/
"""
import pytest


def setup_module():
    print("=====整个.py模块开始前只执行一次:打开浏览器=====","\t")


def teardown_module():
    print("=====整个.py模块结束后只执行一次:关闭浏览器=====","\t")


def setup_function():
    print("===每个函数级别用例开始前都执行setup_function===","\t")


def teardown_function():
    print("===每个函数级别用例结束后都执行teardown_function====","\t")


def test_one():
    print("one")


def test_two():
    print("two")


class TestCase():
    def setup_class(self):
        print("====整个测试类开始前只执行一次setup_class====","\t")

    def teardown_class(self):
        print("====整个测试类结束后只执行一次teardown_class====","\t")

    def setup_method(self):
        print("==类里面每个用例执行前都会执行setup_method==","\t")

    def teardown_method(self):
        print("==类里面每个用例结束后都会执行teardown_method==","\t")

    def setup(self):
        print("=类里面每个用例执行前都会执行setup=","\t")

    def teardown(self):
        print("=类里面每个用例结束后都会执行teardown=","\t")

    def test_three(self):
        print("three")


    def test_four(self):
        print("four")


    def test_five(self):
        assert 3 == 5


# if __name__ == '__main__':
#     pytest.main(["-q", "-s", "-ra"])

