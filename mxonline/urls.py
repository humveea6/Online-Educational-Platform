"""mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin


from apps.users.views import LoginView,LogoutView,RegisterView,ActiveUserView,\
    ForgetPwdView,SendFailView,SendSuccessView,ResetView,ModifyPwd
from apps.operations.views import IndexView



from mxonline import settings

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('',IndexView.as_view(),name="index"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(),name="logout"),
    url(r'^captcha/', include('captcha.urls')),
    path("register/",RegisterView.as_view(),name="register"),
    re_path("active/(?P<active_code>.*)/$",ActiveUserView.as_view(),name="useractive"),
    path("forget/",ForgetPwdView.as_view(),name="forgetpwd"),
    path("send_fail/",SendFailView.as_view()),
    path("send_success",SendSuccessView.as_view()),
    re_path("reset/(?P<active_code>.*)/$",ResetView.as_view(),name="resetpwd"),
    path("modify_pwd/",ModifyPwd.as_view(),name="modifypwd"),

    #上传文件访问URL
    re_path('media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT}),
    # re_path('static/(?P<path>.*)$',serve,{"document_root":settings.STATIC_ROOT}),

    #机构相关页面
    # path("org_list/",OrgView.as_view(),name="orglist"),
    path("org/",include(('apps.organizations.urls',"organizations"),namespace="org")),

    #用户相关操作页面
    path("operation/",include(('apps.operations.urls',"operations"),namespace="op")),

    #课程信息相关页面
    path("course/",include(('apps.courses.urls',"courses"),namespace="course")),

    #个人中心相关页面
    path("users/",include(('apps.users.urls',"users"),namespace="users")),

    #富文本编辑器
    url(r'^ueditor/',include('DjangoUeditor.urls' )),

]