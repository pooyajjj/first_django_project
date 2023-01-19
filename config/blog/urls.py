from unicodedata import name
from django.urls import path, include
from . import views

app_name = 'fotball'
urlpatterns = [
    path('',views.Home.as_view(), name = "home"),
    path('time/',views.time, name = "time"),
    path('article/<slug:slug>',views.detail, name = "detail"),
    # path('index/',views.Home.as_view() ,name = 'index'),
    path('about/',views.about ,name = 'about'),
    path('post/' ,views.post ,name = 'post'),
    path('contact/', views.contact, name = 'contact'),
    path('api-auth/', include('rest_framework.urls')),
    path('get_all/', views.GetAllDate.as_view(), name = 'get_all'),
    path('get_fav/', views.GetFavData.as_view(), name = 'get_fav'),
]