#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 4:42 下午
# @Author  : Kaimin Zeng
# @File    : converters.py

class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value
