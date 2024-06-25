from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),                  # 메인 페이지 (목록)
    path('<int:id>/', views.detail, name='detail'),       # 상세 페이지

    path('profile/', views.profile, name='profile'),      # 프로필 페이지

    path('tag/<int:id>/', views.tag_li, name='tag'),      # 태그에 해당하는 Post 목록

    path('create/', views.create_post, name='create'),      # 생성
    path('delete/<int:id>/', views.delete_post, name='delete'),      # 삭제
    path('update/<int:id>/', views.update_post, name='update'),      # 수정
]
