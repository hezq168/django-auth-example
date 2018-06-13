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
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
