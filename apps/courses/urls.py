from django.urls import path,re_path

from apps.courses.views import CourseListView,CourseDetailView,CourseLessonView,CourseCommentView,VideoView

urlpatterns = [
    re_path("list/$",CourseListView.as_view(),name="list"),
    re_path("^(?P<course_id>\d+)/$",CourseDetailView.as_view(),name="detail"),
    re_path("^(?P<course_id>\d+)/lesson/$",CourseLessonView.as_view(),name="lesson"),
    re_path("^(?P<course_id>\d+)/comments/$",CourseCommentView.as_view(),name="comment"),
    re_path("^(?P<course_id>\d+)/video/(?P<video_id>\d+)$",VideoView.as_view(),name="video"),
]