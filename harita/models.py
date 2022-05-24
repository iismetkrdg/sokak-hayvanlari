
import random
from django.db import models


class Kulube(models.Model):
   il = models.CharField(max_length=50)
   ilce = models.CharField(max_length=100)
   mahalle = models.CharField(max_length=100)
   sokak = models.CharField(max_length=100)
   kapi = models.CharField(max_length=50)
   aciklama = models.CharField(max_length=500,blank=True)
   is_active = models.BooleanField(default=True)
   sontarih = models.DateTimeField(auto_now=True)
   created_at = models.DateTimeField(auto_now_add=True)
   sayac = models.IntegerField(default=1)
   img = models.CharField(max_length=100,default=f'{str(random.randint(1,8))}.jpeg')
   latitude = models.CharField(max_length=20)
   longitude = models.CharField(max_length=20)
   dogcat = models.CharField(max_length=20,default='Kedi')

   class Meta:
      ordering = ['sontarih']
class Person(models.Model):
   username=models.CharField(max_length=25)
   beslemesayisi=models.IntegerField(default=0)
   bildirmesayisi=models.IntegerField(default=0)
   mamakilo=models.IntegerField(default=0)
   auth_token=models.CharField(max_length=100)

   def __str__(self):
      return self.username
   class Meta:
       ordering = ['-beslemesayisi']