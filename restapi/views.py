from django.shortcuts import render

# Create your views here.
from harita.models import Kulube
from restapi.serializers import KulubeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status





class KulubeList(APIView):
   
   def get(self, request, format=None):
      kulubeler = Kulube.objects.all()
      serializer = KulubeSerializer(kulubeler,many=True)
      return Response(serializer.data)
class KulubeDetail(APIView):

   def get_object(self,pk):
      try:
         return Kulube.objects.get(id=pk)
      except Kulube.DoesNotExist:
         raise Http404

   def get(self, request, pk, format=None):
      kulube = self.get_object(pk)
      serializer = KulubeSerializer(kulube)
      return Response(serializer.data)

   