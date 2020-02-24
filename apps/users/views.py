from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.utils.email import send_email
from django.contrib import messages

from apps.users.forms import LoginForm,RegisterForm,CaptchaForm,ForgetForm,ModifyPwdForm
from apps.users.models import UserProfile,EmailVerifyRecord


class ActiveUserView(View):
    def get(self,request,active_code):
        # print(active_code)
        check_exist=EmailVerifyRecord.objects.filter(code=active_code)
        if check_exist:
            for item in check_exist:
                email=item.email
                user=UserProfile.objects.get(email=email)
                user.is_active=True
                user.save()
        else:
            return render(request,"active_fail.html")

        messages.info(request,"激活成功！")
        return render(request,"login.html")


class RegisterView(View):
    def get(self,request,*args,**kwargs):
        # register_form=CaptchaForm()
        return render(request,"register.html")

    def post(self,request,*args,**kwargs):
        register_form=RegisterForm(request.POST)
        # print(request.POST.get("username",""),'\n')
        # print(request.POST.get("password",""),'\n')
        if register_form.is_valid():
            user_name=request.POST.get("username","")
            if UserProfile.objects.filter(email=user_name):
                msg="邮箱已被注册！"
                register_form._errors["msg"]=register_form.error_class([msg])
                return render(request,"register.html",{
                    "register_form":register_form
                })
            password=request.POST.get("password","")
            user_profile=UserProfile()
            user_profile.username=user_name
            user_profile.email=user_name
            user_profile.is_active=False
            user_profile.password=make_password(password)
            user_profile.save()

            if send_email(user_name,"register"):
                return render(request,"send_success.html")
            else:
                return render(request,"send_fail.html")

        else:
            messages.info(request,"邮箱地址非法！")
            print(2333)
            return render(request,"register.html",{
                "register_form":register_form
            })


class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class LoginView(View):
    def get(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))

        # login_form=CaptchaForm()
        return render(request,"login.html")

    def post(self,request, *args, **kwargs):
        login_form=LoginForm(request.POST)

        if login_form.is_valid():

            # user_name= request.POST.get("username","")
            # password= request.POST.get("password","")
            # if not user_name:
            #     return render(request, "login.html", {"msg": "请输入用户名"})
            #
            # if not password:
            #     return render(request, "login.html", {"msg": "请输入密码"})

            user_name=login_form.cleaned_data["username"]
            password=login_form.cleaned_data["password"]
            user= authenticate(username=user_name,password=password)
            # user = authenticate(username="1597878913@qq.com", password="c20140045")
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    msg="用户未激活！"
                    login_form._errors["msg"]=login_form.error_class([msg])
                    return render(request, "login.html", {"msg": "用户未激活！请前往邮箱激活", "login_form": login_form})

            else:
                print(233)
                return render(request,"login.html",{"msg":"用户名或密码错误","login_form":login_form})

        else:
            return render(request,"login.html",{"login_form":login_form})


class ForgetPwdView(View):
    def get(self,request):
        # forget_form=ForgetForm()
        return render(request,"forgetpwd.html")

    def post(self,request):
        forget_form=ForgetForm(request.POST)
        if forget_form.is_valid():
            email=request.POST.get("email","")
            if send_email(email,"forget"):
                return render(request,"send_success.html")
            else:
                return render(request,"send_fail.html")
        else:
            msg = "邮箱地址不合法！"
            forget_form._errors["msg"] = forget_form.error_class([msg])
            return render(request, "forgetpwd.html", {
                "forget_form": forget_form
            })


class SendFailView(View):
    def get(self,request):
        return render(request,"send_fail.html")

class SendSuccessView(View):
    def get(self,request):
        return render(request,"send_success.html")


class ResetView(View):
    def get(self,request,active_code):
        # print(active_code)
        check_exist=EmailVerifyRecord.objects.filter(code=active_code)
        if check_exist:
            for item in check_exist:
                email=item.email
                return render(request,"password_reset.html",{"email":email})
        else:
            messages.info(request,"重置链接失效！")
            return render(request,"active_fail.html")


class ModifyPwd(View):
    def post(self,request):
        modifypwd_form=ModifyPwdForm(request.POST)
        print(333333)
        if modifypwd_form.is_valid():

            pwd1=request.POST.get("pwd1","")
            pwd2=request.POST.get("pwd2","")
            email=request.POST.get("email","")
            if pwd1!=pwd2:
                messages.error(request,"密码不一致！")
                return render(request, "password_reset.html", {
                    "email": email,
                    "msg":"密码不一致！"
                })
            else:
                user=UserProfile.objects.get(email=email)
                user.password=make_password(pwd1)
                user.save()

                EmailVerifyRecord.objects.filter(email=email).delete()
                messages.info(request,"密码修改成功！")
                return render(request,"login.html")

        else:
            email = request.POST.get("email", "")
            messages.error(request,"密码长度过短！")
            return render(request, "password_reset.html", {
                "email": email,
                "msg": "密码长度过短！"
            })


