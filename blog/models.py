from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=250) 
  body = models.TextField()


  # Model Instance 대표 출력 값
  def __str__(self):
    return self.title
  

# 1:N 관계 (하나의 Post -> 여러 Comment)
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # 외래 참조 키
    author = models.CharField(max_length=20)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)







# 1:1 관계 (하나의 User -> 하나의 Profile)
class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# 1:1 관계 (하나의 User -> 하나의 Profile)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)