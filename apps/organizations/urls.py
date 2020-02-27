from django.conf.urls import url
from apps.organizations.views import OrgView,AddAskView,OrgHomeView,OrgTeacherView,OrgCourseView,\
    OrgDescView,TeacherListView,TeacherDetailView
from django.urls import path,re_path

urlpatterns=[
    re_path('list/$',OrgView.as_view(),name="list"),
    re_path('add_ask/$',AddAskView.as_view(),name="add_ask"),
    re_path('^(?P<org_id>\d+)/$',OrgHomeView.as_view(),name="home"),
    re_path('^(?P<org_id>\d+)/teacher/$',OrgTeacherView.as_view(),name="teacher"),
    re_path('^(?P<org_id>\d+)/course/$',OrgCourseView.as_view(),name="course"),
    re_path('^(?P<org_id>\d+)/desc/$',OrgDescView.as_view(),name="desc"),

    re_path("^all_teachers/$",TeacherListView.as_view(),name="allteacher"),
    re_path("^teacher_detail/(?P<teacher_id>\d+)/$",TeacherDetailView.as_view(),name="teacherdetail"),
]
