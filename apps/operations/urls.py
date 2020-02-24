from django.urls import path,re_path

from apps.operations.views import AddFavView

urlpatterns = [
    re_path("^fav/$",AddFavView.as_view(),name="fav")
]