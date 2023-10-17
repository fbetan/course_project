from django.urls import path

from .views import index, search, polinfo


app_name = 'politicians'
urlpatterns = [
    path("", index, name="index"),
    path("search/", search, name="search"),
    path("polinfo/", polinfo, name="polinfo")
]