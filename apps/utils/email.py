from apps.users.models import EmailVerifyRecord
from django.core.mail import send_mail
from mxonline.settings import EMAIL_FROM
import random

def send_email(email,send_type):
    email_record=EmailVerifyRecord()
    rand_str=gen_random_str(8)
    email_record.code=rand_str
    email_record.email=email
    email_record.send_type=send_type
    email_record.save()

    email_title=""
    email_body=""

    if send_type=="register":
        email_title="慕学在线注册激活链接"
        email_body="请点击下面的链接激活你的账户：http://127.0.0.1:8000/active/{}".format(rand_str)

        send_status=send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            return True
        else:
            return False

    elif send_type=="forget":
        email_title = "慕学在线密码重置链接"
        email_body = "请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{}".format(rand_str)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            return True
        else:
            return False






def gen_random_str(length=8):
    str=""
    rand_str="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYX0123456789"
    rand_len=len(rand_str)-1
    # random1=random.random()
    for i in range(length):
        str+=rand_str[random.randint(0,rand_len)]

    return str


