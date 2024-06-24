from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),                 # 메인 페이지 (목록)
    path('<int:id>/', views.detail, name='detail'),       # 상세 페이지
    path('profile/', views.profile, name='profile')      # 프로필 페이지
]
