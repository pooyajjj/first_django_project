from django.urls import path, include, re_path
from .views import home ,time, detail

AppName = 'fotball'
urlpatterns = [
    path('',home, name = "home"),
    path('time',time, name = "time"),
    path('article/<slug:slug>',detail, name = "detail"),
]