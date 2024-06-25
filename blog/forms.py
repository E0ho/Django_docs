from django import forms


# 장고 Form 객체
class PostForm(forms.Form):
  title = forms.CharField(label="제목") 
  body = forms.CharField(label="내용", widget=forms.Textarea)