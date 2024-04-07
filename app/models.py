from django.db import models



# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    pic_url = models.CharField(max_length=255,blank=True)
    name = models.CharField(max_length=255,unique=True)
    author = models.CharField(max_length=255)
    votes = models.PositiveIntegerField(blank=True)
    rating = models.DecimalField(decimal_places=1,max_digits=2)
    
    def __str__(self):
        return self.name