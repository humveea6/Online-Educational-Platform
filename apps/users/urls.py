from django.conf.urls import url
from django.urls import path,re_path
from apps.users.views import UserInfoView,UploadImageView,ChangePwdView,MyCourseView,FavOrgView,\
    FavTeacherView,FavCourseView,MyMessageView

urlpatterns=[
    re_path("^info/$",UserInfoView.as_view(),name="info"),
    re_path("^image/upload/$",UploadImageView.as_view(),name="upload"),
    re_path("^update/pwd/$",ChangePwdView.as_view(),name="update_pwd"),
    re_path("^my_course/$",MyCourseView.as_view(),name="mycourse"),
    re_path("^fav_org/$",FavOrgView.as_view(),name="fav_org"),
    re_path("^fav_teacher/$",FavTeacherView.as_view(),name="fav_teacher"),
    re_path("^fav_course/$",FavCourseView.as_view(),name="fav_course"),
    re_path("^my_messages/$",MyMessageView.as_view(),name="my_message"),
]
