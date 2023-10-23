from django.db import models

# Create your models here.
class Familydb(models.Model):
    name = models.CharField(max_length=50)
    nai = models.IntegerField()
    tel = models.CharField(max_length=50)
    gen = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    
    