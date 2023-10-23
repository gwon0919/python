from django.db import models

# Create your models here.
class Guest(models.Model):
    # myno = models.AutoField(auto_created=True,primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    regdate = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        #ordering = ('title',)        # 정렬방법 2 # 오름차순 정렬 / tuple type으로 기술
        #ordering = ('title','-id')
        ordering = ('-id',)
        