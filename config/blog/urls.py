from django.urls import path
from .views import home ,time, detail, index, about

AppName = 'fotball'
urlpatterns = [
    path('',home, name = "home"),
    path('time',time, name = "time"),
    path('article/<slug:slug>',detail, name = "detail"),
    path('index',index ,name = 'index'),
    path('about',about ,name = 'about'),
    
]