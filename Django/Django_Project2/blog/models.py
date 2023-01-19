from django.db import models
#   Create   your   models   here.

class Post(models.Model):
    name = models.CharField(max_length=30)   #   데이터베이스의 필드(컬럼)
    information   = models.TextField(blank=True)
    image=models.ImageField(upload_to='blog/images/%Y/%m/%d/',blank=True)
    email=models.EmailField(blank=True)
    birth=models.CharField(max_length=6)
    hobby = models.TextField(blank=True)
    need = models.TextField(blank=True)
    url1=models.URLField()
    url2=models.URLField()
    # - 사진, 이름, 한줄소개, 취미, MBTI,
    #  현재 노력하고 있는 것
    
#   author는 추후 작성
def __str__(self):
    return f'[{self.pk}]{self.name}'
def get_abs_url(self):
    return f'/blog/{self.pk}'