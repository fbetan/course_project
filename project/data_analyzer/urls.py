from django.urls import path 
from .views import index, analyze, analyze_industry

app_name = 'data_analyzer'

urlpatterns = [
    path("", index, name="index"),
    path("analyze/", analyze, name="analyze"),
    path("analyze_industry/", analyze_industry, name="analyze_industry")
]