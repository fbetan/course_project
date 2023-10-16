from django.urls import path
from .views import index, collect, collect_industry

app_name = 'data_collector'

urlpatterns = [
    path("", index, name="index"),
    path("collect/", collect, name="collect"),
    path("collect_industry/", collect_industry, name="collect_industry")
]