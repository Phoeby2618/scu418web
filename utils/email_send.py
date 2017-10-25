# _*_ encoding:utf-8 _*_
from django.core.mail import send_mail

from random import Random

from forum.models import EmailVerifyRecord
from scu418web.settings import EMAIL_FROM




def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) -1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def send_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.email = email
    email_record.code = code
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == 'register':
        email_title = "智能信息处理实验室激活链接"
        email_body = "请点击下面的链接激活您的账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

        if send_status == 1:
            pass

    elif send_type == 'forget':
        email_title = "智能信息处理实验室找回密码链接"
        email_body = "请点击下面的链接重置您的密码：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

        if send_status == 1:
            pass



