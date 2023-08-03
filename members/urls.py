from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register', views.register, name='register'),
    # path('user_login', views.user_login, name='login'),
    path('home', views.home, name='home'),
    path('logoutaction', views.logoutaction, name='logout'),
]