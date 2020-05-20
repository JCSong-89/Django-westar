"""westar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from . import views  

urlpatterns = [
    path('user', views.UserCreateView.as_view()), #POST 생성
#    path('user_feed', views.UserFeedView.as_view()), #유저 홈 
    #path('user/<int:pk>'/profile, views.UserFeedView.as_view()), #조회, 수정 GET, PUT :userFEED
    path('user/login', views.UserLoginView.as_view()), #POST LOGIN
    path('user/recommend', views.User_recommend.as_view())
#   path(user/<int:pk>/clear) DEL 삭제
]
