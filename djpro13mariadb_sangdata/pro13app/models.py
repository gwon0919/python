from django.db import models

# Create your models here.
# python manage.py inspectdb > aaa.py 아나콘다 prompt에서 경로 설정 후 aaa.py를 만들어 기존에 있는 정보가 적혀 있는 파일을 생성한 수 필요한 정보를 가져온다.
class Sangdata(models.Model):
    code = models.IntegerField(primary_key=True)
    sang = models.CharField(max_length=20, blank=True, null=True)
    su = models.IntegerField(blank=True, null=True)
    dan = models.IntegerField(blank=True, null=True)
        
    class Meta:
        managed = False
        db_table = 'sangdata'
