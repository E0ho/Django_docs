from django import forms
from .models import *

# 장고 Form 객체
class PostForm(forms.Form):
  title = forms.CharField(label="제목") 
  body = forms.CharField(label="내용", widget=forms.Textarea)


# 장고 ModelForm 객체
class PostModelForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'body']

    labels = {
      'title' : '제목',
      'body' : '내용'
    }