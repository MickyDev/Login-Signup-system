"""prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from members import views
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('members.urls')),
    path('register/', include('members.urls')),
    path('user_login/', include('members.urls')),
    path('home/', include('members.urls')),
    path('admin/', admin.site.urls),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'resetpassword.html'),
         name="reset_password"),
    
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'resetpassworddone.html'),
         name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'resetpasswordconfirm.html'),
         name="password_reset_confirm"),
    
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'resetpasswordcomplete.html'),
         name="password_reset_complete"),
]