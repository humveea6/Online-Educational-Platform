from django.urls import path,re_path

from apps.operations.views import AddFavView,CommentView

urlpatterns = [
    re_path("^fav/$",AddFavView.as_view(),name="fav"),
    re_path("^comment/$",CommentView.as_view(),name="comment"),
]