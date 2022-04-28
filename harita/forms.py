
from django import forms


from .models import Kulube

class YuvaBildirForms(forms.ModelForm):
   class Meta:
      model=Kulube
      fields=['il','ilce','mahalle','sokak','kapı','acıklama']

   il = forms.CharField(label='İl',max_length=50)
   ilce = forms.CharField(label='İlçe',max_length=100)
   mahalle = forms.CharField(label='Mahalle',max_length=100)
   sokak = forms.CharField(label='Sokak', max_length=100)
   kapı = forms.CharField(label='Kapı No', max_length=50)
   acıklama = forms.CharField(label='Açıklama', max_length=500)

class BesleForms(forms.Form):
   mama = forms.CharField(label='kackilo',max_length=50)
   id = forms.CharField(label='id',max_length=100)
   

   