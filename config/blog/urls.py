from unicodedata import name
from django.urls import path, include
from .views import home ,time, detail, contact ,index, about, post

AppName = 'fotball'
urlpatterns = [
    path('',home, name = "home"),
    path('time',time, name = "time"),
    path('article/<slug:slug>',detail, name = "detail"),
    path('index',home ,name = 'index'),
    path('about',about ,name = 'about'),
    path('post' ,post ,name = 'post'),
    path('contact', contact, name = 'contact'),
    path('api-auth/', include('rest_framework.urls')),
]