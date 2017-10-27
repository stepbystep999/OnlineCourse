# -*- coding:utf-8 -*-

__author__ = 'stepbystep999'
__date__ = '2017/10/27 15:56'

import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import  views

class BaseSetting(object):
    enable_themes = True    # 默认主题功能为False
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "教育在线后台管理系统"
    site_footer = "教育在线网"
    menu_style = "accordion"
#
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)