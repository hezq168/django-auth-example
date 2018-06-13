#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 11:02
# @Author  : Hezq
# @Contact : Hezq168@gmail.com
# @File    : urls.py
# @Project : django_auth_example
# @Software: PyCharm


from django.urls import path
from users import views

urlpatterns = [
    #  注册
    path('register/', views.register, name='register'),
    #  登录
    path('login/', views.login, name='login'),
    #  退出
    path('logout/', views.logout, name='logout'),
    #  修改密码
    path('edit_pass/', views.edit_pass, name='edit_pass'),
]
