from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        abstract=True

# Create your models here.
GENDER_CHOICES=(
    ("male","男"),
    ("female","女")
)

class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name="昵称",default="")
    birthday=models.DateField(verbose_name="生日",null=True,blank=True)
    gender=models.CharField(verbose_name="性别",choices=GENDER_CHOICES,max_length=6)
    address=models.CharField(max_length=100,verbose_name="地址",default="")
    mobile=models.CharField(max_length=11,verbose_name="手机号码")
    image=models.ImageField(upload_to="head_image/%Y/%m",null=True,blank=True)


    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name

    def __str__(self):
        if self.nick_name:
            return  self.nick_name
        else:
            return self.username

    def unread_nums(self):
        return self.usermessage_set.filter(has_read=False).count()


class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name="邮箱验证码")
    email=models.EmailField(max_length=50,verbose_name="邮箱地址")
    send_type=models.CharField(verbose_name="验证码类型",choices=(("register","注册"),("forget","找回")),max_length=8)
    send_time=models.DateTimeField(verbose_name="发送时间",default=datetime.now)

    class Meta:
        verbose_name="邮箱验证码"
        verbose_name_plural=verbose_name


    def __str__(self):
        return "{}({})".format(self.code,self.email)