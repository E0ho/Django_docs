from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('ok')


# URL 변수 활용
def detail(request, id):
    return HttpResponse(id)