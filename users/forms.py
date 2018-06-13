#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 10:15
# @Author  : Hezq
# @Contact : Hezq168@gmail.com
# @File    : forms.py
# @Project : django_auth_example
# @Software: PyCharm

from django import forms


# 登录form
class LoginForm(forms.Form):
    user = forms.CharField()
    pwd = forms.CharField()


# 修改密码form
class ModifyPwdForm(forms.Form):
    pwd = forms.CharField(required=True, min_length=5, error_messages={'required': '密码不能为空!',
                                                                       'min_length': '密码小于5位！'})


# 注册form
class RegisterForm(forms.Form):
    user = forms.CharField(required=True, error_messages={'required': '用户名不能为空',})
    email = forms.EmailField(required=True, error_messages={'required': '邮箱不能为空',})
    pwd = forms.CharField(required=True, min_length=5, error_messages={'required': '密码不能为空!',
                                                                       'min_length':'密码小于5位！'})