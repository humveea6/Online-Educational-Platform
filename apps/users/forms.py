from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username=forms.CharField(required=True,min_length=2)
    password=forms.CharField(required=True,min_length=3)
    # captcha = CaptchaField()


class RegisterForm(forms.Form):
    username=forms.EmailField(required=True)
    password=forms.CharField(required=True,min_length=5)


class ForgetForm(forms.Form):
    email=forms.EmailField(required=True)
    # captcha=CaptchaField(error_messages={"invalid":"验证码错误"})


class ModifyPwdForm(forms.Form):
    pwd1=forms.CharField(required=True,min_length=6)
    pwd2=forms.CharField(required=True,min_length=6)

class CaptchaForm(forms.Form):
    captcha = CaptchaField()