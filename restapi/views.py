from django.shortcuts import render

# Create your views here.
from harita.models import Kulube
from restapi.serializers import KulubeSerializer
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

   