from django.db import models

# Create your models here.
class Article (models.Model):       # 논리적인 테이블을 클래스로 정의
    irum = models.CharField(max_length=10)
    juso = models.CharField(max_length=30)
    nai = models.IntegerField()
    