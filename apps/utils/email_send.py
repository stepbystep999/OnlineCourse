# -*- coding:utf-8 -*-

__author__ = 'stepbystep999'
__date__ = '2017/11/2 1:27'

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from OnlineCourse.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    mail_title = ""
    mail_body = ""

    if send_type == "register":
        mail_title = "教育在线网注册激活链接"
        mail_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(mail_title, mail_body, EMAIL_FROM, [email]) #注意此处为的email为list类型
        if send_status: #发送成功
            pass

    elif send_type == "forget":
        mail_title = "教育在线网密码重置链接"
        mail_body = "请点击下面的链接重置你的密码: http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(mail_title, mail_body, EMAIL_FROM, [email]) #注意此处为的email为list类型
        if send_status: #发送成功
            pass