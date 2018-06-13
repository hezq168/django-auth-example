from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as lg, logout as lo
from django.http import HttpResponse

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from users.forms import LoginForm
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


def logout(request):
    lo(request)
    return redirect('/')


def edit_pass(request):
    return render(request, 'users/edit_pass.html')

