from django.shortcuts import render

# Create your views here.
from harita.models import Kulube,Person
from restapi.serializers import KulubeSerializer , PersonSerializer
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination





class KulubeList(APIView):
   
   def get(self, request, format=None):
      kulubeler = Kulube.objects.all()
      paginator = PageNumberPagination()
      result = paginator.paginate_queryset(kulubeler,request)
      serializer = KulubeSerializer(result,many=True)
      data = {
         'next':paginator.get_next_link(),
         'results':serializer.data
      }
      return Response(data)
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
class KulubebyLocation(APIView):
   def get(self,request,lat,lon,format=None):
      gonder = []
      kulubeler = Kulube.objects.all()
      for i in list(kulubeler):
         fark = ((float(lat)-float(i.latitude))**2 + (float(lon)-float(i.longitude))**2)**(1/2)
         if fark < 0.006:
            gonder.append(i)


      serializer = KulubeSerializer(gonder,many=True)
      return Response(serializer.data)
class PersonView(APIView):
   def get(self,request,format=None):
      personsbildir = list(Person.objects.all().order_by('-bildirmesayisi'))[10]
      personsbesle = list(Person.objects.all().order_by('-beslemesayisi'))[10]
      personsmama = list(Person.objects.all().order_by('-mamakilo'))[10]
      serializer1 = PersonSerializer(personsbildir,many=True)
      serializer2 = PersonSerializer(personsbesle,many=True)
      serializer3 = PersonSerializer(personsmama,many=True)
      data = {
         'bildir' : serializer1.data,
         'besle' : serializer2.data,
         'mama' : serializer3.data,
      }
      return Response(data)