from django.urls import path, include, re_path
from .views import home ,time, detail, index, about

AppName = 'fotball'
urlpatterns = [
    path('',home, name = "home"),
    path('time',time, name = "time"),
    path('article/<slug:slug>',detail, name = "detail"),
    path('index',index ,name = 'index'),
    path('article/index',index ,name = 'index-2'),
    path('about',about ,name = 'about'),
    
]