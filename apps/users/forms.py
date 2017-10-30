# -*- coding:utf-8 -*-

__author__ = 'stepbystep999'
__date__ = '2017/10/29 4:22'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)