from django.urls import path
from django.views.generic import *
from . import views
from .models import *

app_name = 'book'

urlpatterns = [
    path('', ListView.as_view(model=Book), name='list'),
    path('detail/<pk>/', DetailView.as_view(model=Book), name='detail'),
    path('create/', CreateView.as_view(model=Book, fields='__all__'), name='create'),
    path('update/<pk>/', UpdateView.as_view(model=Book, fields='__all__'), name='update'),

]
