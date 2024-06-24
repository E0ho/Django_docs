from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import *


# 메인 페이지 처리 함수 (게시판 목록)
def index(request):
    posts = Post.objects.all()

    context = {'posts':posts}

    return render(request, 'blog/list.html', context)



# 상세 페이지 처리 함수
def detail(request, id):
    post = get_object_or_404(Post, id = id)
    comments = post.comments.all()

    context = {
        'post' : post,
        'comments' : comments
        }
    
    return render(request, 'blog/detail.html', context)



# 프로필 처리 함수
def profile(request):

    # 임시 테스트용
    user = User.objects.first()     # 사용자
    profile = user.profile          # 사용자 매칭 프로필
    print(profile.phone_number)
    context = {
        'user' : user,
        'profile':profile
        }

    return render(request, 'blog/profile.html', context)