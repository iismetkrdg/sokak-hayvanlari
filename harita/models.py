
import random
from django.db import models


class Kulube(models.Model):
   il=models.CharField(max_length=50)
   ilce=models.CharField(max_length=100)
   mahalle=models.CharField(max_length=100)
   sokak=models.CharField(max_length=100)
   kapı=models.CharField(max_length=50)
   acıklama=models.CharField(max_length=500,blank=True)
   is_active=models.BooleanField(default=True)
   sontarih=models.DateTimeField(auto_now=True)
   created_at=models.DateTimeField(auto_now_add=True)
   sayac=models.IntegerField(null=True,default=1)
   img=models.CharField(max_length=100,null=True,default=f'{str(random.randint(1,8))}.jpeg')
   latitude=models.CharField(max_length=20,null=True)
   longitude=models.CharField(max_length=20,null=True)

   def __str__(self):
      return f"{self.il}{self.ilce}{self.sokak}"
   class Meta:
      ordering = ['sontarih']
class Person(models.Model):
   username=models.CharField(max_length=25)
   beslemesayısı=models.IntegerField(null=True,default=0)
   bildirmesayısı=models.IntegerField(null=True,default=0)
   mamakilo=models.IntegerField(null=True,default=0)
   auth_token=models.CharField(max_length=100,null=True)

   def __str__(self):
      return self.username
   class Meta:
       ordering = ['-beslemesayısı']