


from rest_framework import serializers
from harita.models import Kulube , Person

class KulubeSerializer(serializers.ModelSerializer):
   class Meta:
      model = Kulube
      fields = ['id','il','ilce','mahalle','sokak','kapi','aciklama','img','dogcat','sontarih']

class PersonSerializer(serializers.ModelSerializer):
   class Meta:
      model = Person
      fields = ['username','beslemesayisi','bildirmesayisi','mamakilo']
      

