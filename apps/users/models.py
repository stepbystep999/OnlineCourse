# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(choices=(('male','男'),('female','女')),default='female', max_length=6)
    address = models.CharField(max_length=100, default='', verbose_name='地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码')
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)    #upload_to文件的书写格式详见官方文档，image在后台是以字符串形式存储的，所以需要设置最大长度

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
    def __unicode__(self):    #在print UserProfile的实例时，不定义该函数则无法打印此处的字符串
        return self.username    #继承的AbstractUser.username
