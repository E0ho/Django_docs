from django.urls import path
from django.views.generic import *
from . import views
from .models import *

app_name = 'book'

urlpatterns = [
    path('', ListView.as_view(model=Book), name='list'),
    path('detail/<pk>/', DetailView.as_view(model=Book), name='detail'),
    path('create/', DetailView.as_view(model=Book), name='create'),
    path('update/<pk>/', DetailView.as_view(model=Book), name='update'),
    path('delete/<pk>/', DetailView.as_view(model=Book), name='delete'),
]
