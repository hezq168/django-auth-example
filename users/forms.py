#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 10:15
# @Author  : Hezq
# @Contact : Hezq168@gmail.com
# @File    : forms.py
# @Project : django_auth_example
# @Software: PyCharm

from django import forms


class LoginForm(forms.Form):
    user = forms.CharField()
    pwd = forms.CharField()