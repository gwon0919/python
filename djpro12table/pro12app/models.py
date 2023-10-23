from django.db import models

# Create your models here.
class Maker(models.Model):
    mname = models.CharField(max_length = 20)
    mtel = models.CharField(max_length = 30)
    maddr = models.CharField(max_length = 50)
    def __str__(self):      # id 대신에 name으로 나타나게함
        return self.mname
    

class Product(models.Model):
    pname = models.CharField(max_length=20)
    pprice = models.IntegerField()
    pmaker_name = models.ForeignKey(Maker, on_delete=models.CASCADE)       # FK는 Maker의 PK(id)를 참조
    
    