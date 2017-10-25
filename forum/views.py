# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

from .forms import LoginForm, RegisterForm, ForgetForm, ModifyForm
from .models import UserProfile
from utils.email_send import send_email
from .models import EmailVerifyRecord

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class ForumView(View):
    def get(self,request):
        return render(request, 'indexForum.html')

class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email):
                return render(request, 'register.html', {'msg': '用户已存在'})
            username = request.POST.get('username', '')
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')
            if password1 != password2:
                return render(request, 'register.html', {'msg': '密码不一致'})

            user_profile = UserProfile()
            user_profile.email = email
            user_profile.username = username
            user_profile.password = make_password(password1)
            user_profile.is_active = False
            user_profile.save()

            send_email(email, 'register')
            return render(request, 'send_sucess.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        login_form = LoginForm()
        return render(request, 'active_success.html')


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form':forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            user_profile = UserProfile.objects.filter(email=email)
            if user_profile:
                send_email(email, 'forget')
                return render(request, 'send_sucess.html')
            else:
                return render(request, 'forgetpwd.html', {'msg': '用户不存在', 'forget_form': forget_form})
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class ResetPwdView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'reset.html', {'email':email})
        else:
            return render(request, 'reset_fail.html')


class ModifyView(View):
    def post(self, request):
        modify_form = ModifyForm(request.POST)
        if modify_form.is_valid():
            email = request.POST.get('email', '')
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')
            if password1 != password2 :
                return render(request, 'reset.html', {'msg': '密码不一致'})
            else:
                user_profile = UserProfile.objects.get(email=email)
                user_profile.password = make_password(password1)
                user_profile.save()
                return render(request, 'modify_success.html')
        else:
            return render(request, 'reset.html', {'modify_form':modify_form})

