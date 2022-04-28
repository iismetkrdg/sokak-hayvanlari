from django.contrib.auth.models import User
from django.shortcuts import redirect, render
import folium
from .models import Kulube, Person
import datetime
from django.contrib import messages
from .forms import YuvaBildirForms
from django.views.generic import (CreateView, DetailView, ListView, TemplateView, UpdateView,FormView)
from django.views import View
   



class WelcomeView(ListView):
   model = Kulube
   template_name = "harita/index.html"
   context_object_name = 'kulubeler'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['besleme'] = list(Person.objects.all())[:3]
      context['yuvabildirme'] = list(Person.objects.all().order_by('bildirmesayısı'))[:3]
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
         text = f"<a target='_blank' href='/yuva_details/{i.id}> Detay </a>"
         print(text)
         folium.Marker([i.latitude,i.longitude],popup=text,tooltip="Detay için tıklayın.").add_to(m)
      m = m._repr_html_()
      context['m'] = m
      return context
class YuvaDetailsView(View):
   
   def get(self,request,*args,**kwargs):
      yuva = Kulube.objects.get(id=kwargs['pk'])
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
      person_object.beslemesayısı += 1
      person_object.save()
      messages.add_message(request,messages.INFO,'Her şey için teşekkürler.')
      return redirect('home')

class YuvaBildirView(CreateView):
   template_name = 'harita/yuvabildir.html'
   form_class = YuvaBildirForms
   success_url = "/"
   def get_context_data(self, **kwargs):
      print(super().get_context_data(**kwargs))
   def form_valid(self,form):
      return super().form_valid(form)

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




