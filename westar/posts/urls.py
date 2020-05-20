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
    path('content', views.ContentCreateView.as_view()), #생성 POST
#    path('content/<int:pk>', views.ContentsView.as_view()), #조회, 수정 
    path('content/<str:username>', views.ContentView.as_view()),
#    path('content/<str:username>/follow'),#팔로우 유저 목록
#   path('content/<int:pk>/to_clear') 삭제 DEL
    path('content/comment', views.CommetView.as_view()), #생성 POST
#   path('content/<int:pk>/comment/<int:pk>') 수정 PUT
#   path('content/<int:pk>/comment/<int:pk>/to_clear') 삭제 DEL
    path('content/like', views.LikeView.as_view()) #수정 PUT 
]
