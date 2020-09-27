#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 2:52 下午
# @Author  : Kaimin Zeng
# @File    : urls.py
from django.urls import path,re_path,register_converter
from . import views,converters

register_converter(converters.IntConverter,'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('',views.comment),
    ### 带变量的URL
    path('<int:year>', views.year),  # 只接收整数，其他类型返回404
    path('<int:year>/<str:name>', views.name),
    ### 正则匹配
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
    ### 自定义过滤器
    path('<yyyy:year>', views.year),
    path('books',views.books),




]

