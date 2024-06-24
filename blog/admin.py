from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):

    # 추가로 가능한 기능
    list_display = ('title', 'body')        # 시각화
    search_fields = ('title', 'body')       # 조회 기능


admin.site.register(Post, PostAdmin)
