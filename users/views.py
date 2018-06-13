from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as lg, logout as lo
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import make_password

from users.forms import LoginForm, ModifyPwdForm, RegisterForm
from users.models import User


class CustomBackend(ModelBackend):
    """重写authenticate模块"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:  #可以捕获除与程序退出sys.exit()相关之外的所有异常
            return None


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_data = login_form.cleaned_data
            user = authenticate(username=login_data['user'], password=login_data['pwd'])
            if user:
                lg(request, user)
                return redirect('/')
            else:
                return HttpResponse('登录失败')
        else:
            return render(request, 'users/login.html',{"error":login_form.errors})
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'users/login.html', {'login_form':login_form})


@login_required
def logout(request):
    lo(request)
    return redirect('/')


@login_required
def edit_pass(request):
    if request.method == 'POST':
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd = request.POST.get('pwd', '')
            email = request.POST.get('email', '')
            user = User.objects.get(email=email)
            if user:
                user.password = make_password(pwd)
                user.save()
                return render(request, 'users/login.html')
            else:
                pass
        else:
            email = request.POST.get('email', '')
            return render(request, 'users/edit_pass.html', {'email': email, 'modify_form': modify_form,
                                                            'msg': '密码不符合要求！'})
    return render(request, 'users/edit_pass.html')


def register(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            user_name = request.POST.get('user', '')
            email = request.POST.get('email', '')
            pass_word = request.POST.get('pwd', '')
            if User.objects.filter(Q(username=user_name) | Q(email=email)):
                return render(request, 'users/register.html', {'reg_form': reg_form, 'msg':'用户名或邮箱已经存在！'})
            user_profile = User()
            user_profile.username = user_name
            user_profile.email = email
            # 密码利用make_password加密
            user_profile.password = make_password(pass_word)
            # 保存用户数据
            user_profile.save()
            return redirect('/users/login/')
        else:
            return render(request, 'users/register.html', {'reg_form': reg_form})
    return render(request, 'users/register.html')
