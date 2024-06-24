from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import *
# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {'posts':posts}

    return render(request, 'blog/list.html', context)


# URL 변수 활용
def detail(request, id):
    return HttpResponse(id)