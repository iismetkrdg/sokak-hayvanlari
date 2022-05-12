from typing import List
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import redirect, render
import folium
from .models import Kulube, Person
import datetime
import geocoder
from django.contrib import messages
from .forms import YuvaBildirForms
from django.views.generic import (CreateView, DetailView, ListView, TemplateView, UpdateView,FormView)
from django.views import View
   



class WelcomeView(ListView):
   model = Kulube
   template_name = "harita/index.html"
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['besleme'] = list(Person.objects.all())[:3]
      context['yuvabildirme'] = list(Person.objects.all().order_by('bildirmesayisi'))[:3]
      context['mamakg'] = list(Person.objects.all().order_by('mamakilo'))[:3]
      return context

class HaritaView(ListView):
   model = Kulube
   template_name = "harita/harita.html"
   
   def get_context_data(self,**kwargs):
      context = super().get_context_data(**kwargs)
      ks = Kulube.objects.all()
      m = folium.Map(location=[41.02,29],zoom_start=12)
      for i in list(ks):
         folium.Marker([i.latitude,i.longitude]).add_to(m)
      m = m._repr_html_()
      context['m'] = m
      return context
class YuvaDetailsView(View):
   
   def get(self,request,*args,**kwargs):
      yuva = Kulube.objects.get(id=kwargs['pk'])
      if yuva.latitude is None:
         location = geocoder.osm(yuva.il+","+yuva.sokak)
         yuva.latitude = location.lat
         yuva.longitude = location.lng
         yuva.save()
      fark = (datetime.datetime.now(datetime.timezone.utc)-yuva.created_at).days
      oran = int(round(fark/(yuva.sayac/1000)))
      m = folium.Map(location=[yuva.latitude,yuva.longitude],zoom_start=18)
      folium.Marker([yuva.latitude,yuva.longitude]).add_to(m)
      m = m._repr_html_
      context = {'yuva':yuva,'oran':oran,'m':m}
      return render(request,'harita/yuva_details.html',context)
   def post(self,request,*args,**kwargs):
      yuva = Kulube.objects.get(id=kwargs['pk'])
      yuva.sayac += int(request.POST['kackilo'])
      yuva.save()
      person_object = Person.objects.get(username=request.user)
      person_object.mamakilo += int(request.POST['kackilo'])
      person_object.beslemesayisi += 1
      person_object.save()
      messages.add_message(request,messages.INFO,'Her şey için teşekkürler.')
      return redirect('home')


class YuvaBildirView(View):
   def get(self,request,*args, **kwargs):
      form = YuvaBildirForms
      return render(request,'harita/yuvabildir.html',{'form':form})
   def post(self,request, *args, **kwargs ):
      form = YuvaBildirForms(request.POST)
      if form.is_valid():
         location = geocoder.osm(form.cleaned_data.get('il')+","+form.cleaned_data.get('sokak'))
         if not location.lat:
            messages.add_message(request,messages.ERROR,'Girdiğiniz bilgilere ait konum bulunamadı.')
            return redirect('home')
         a = form.save()
         a.latitude = location.lat
         a.longitude = location.lng
         a.save()
         person = Person.objects.get(username=request.user)
         person.bildirmesayisi += 1
         person.save()
         
         messages.add_message(request,messages.INFO,'Her şey için teşekkürler...')
         return redirect('home')
      else:
         messages.add_message(request,messages.ERROR,'Bir hata oluştu.')
         return redirect('home')
class BulView(ListView):
   model = Kulube
   template_name = 'harita/bul.html'
   context_object_name = 'kulubeler'
class ProfilView(DetailView):
   model = User
   template_name = 'harita/profil.html'
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['person'] = Person.objects.get(id=User.objects.get(username=context['user']).id)
       return context

class IletisimView(TemplateView):
   template_name = 'harita/iletisim.html'



def custom400(request,exception):
   return render(request,'harita/not-found.html',status=400)
def custom404(request,exception):
   return render(request,'harita/not-found.html',status=404)