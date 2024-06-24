from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:id>', views.detail)       # URL 변수
]
