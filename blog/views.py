from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import *
from .forms import *

# 메인 페이지 처리 함수 (게시판 목록)
def index(request):

    # 전체
    posts = Post.objects.all()

    # 키워드 검색
    keyword = request.GET.get('keyword')
    if keyword:
        posts = Post.objects.filter(title__contains = keyword)

    context = {'posts':posts}

    return render(request, 'blog/list.html', context)



# 상세 페이지 처리 함수
def detail(request, id):
    post = get_object_or_404(Post, id = id)
    comments = post.comments.all()
    tags = post.tag.all()


    context = {
        'post' : post,
        'comments' : comments,
        'tags' : tags
        }
    
    return render(request, 'blog/detail.html', context)


def tag_li(request, id):

    # tag 조회
    tag = get_object_or_404(Tag, id=id)

    # tag에 해당하는 Post 목록
    posts = tag.post_set.all()

    context = {
        'tag': tag,
        'posts': posts
    }

    print(context)
    return render(request, 'blog/list.html', context)



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





# Django Form 객체
def input_PostForm(request):
    
    # URL 방문
    if request.method == "GET":
        forms = PostForm()
        
        context = {'forms':forms}

        return render(request, 'blog/forms.html', context)

    # 데이터 전송
    elif request.method == "POST":

        title = request.POST.get('title')
        body = request.POST.get('body')

        posts = Post.objects.all()
        posts.create(title = title, body = body)

        return redirect('/admin')