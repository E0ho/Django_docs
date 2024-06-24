from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=250) 
  body = models.TextField()


  # Model Instance 대표 출력 값
  def __str__(self):
    return self.title