from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):

    # 추가로 가능한 기능
    list_display = ('title', 'body')        # 시각화
    search_fields = ('title', 'body')       # 조회 기능


# 게시글
admin.site.register(Post, PostAdmin)

# 댓글 (게시글 참조)
admin.site.register(Comment)



# 유저 정보
admin.site.register(User)

# Profile (유저 참조)
admin.site.register(Profile)




# Profile (유저 참조)
admin.site.register(Tag)