from pyexpat import model
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.template import context
import folium
from .models import Kulube, Person
import geocoder
import random
import datetime
from django.contrib import messages

from django.views.generic import (CreateView, DetailView, ListView, TemplateView,
                                  UpdateView)

def beslemesayıları():
   bos={}
   a=Person.objects.all()
   for i in list(a):
      bos[i.username]=i.beslemesayısı
   userns=list(dict(sorted(bos.items(), key=lambda item: item[1])))
   userns=userns[::-1]
   newbos=[]
   n=1
   for s in userns[:3]:
      name=User.objects.get(username=s).get_full_name()

      sayı=Person.objects.filter(username=s)[0].beslemesayısı
      newbos.append({"name":name,"sayı":sayı,"n":n})
      n+=1
   return newbos
def yuvabildirsayıları():
   bosd={}
   a=Person.objects.all()
   for i in list(a):
      bosd[i.username]=i.bildirmesayısı
   userns=list(dict(sorted(bosd.items(), key=lambda item: item[1])))
   userns=userns[::-1]
   newbosd=[]
   n=1
   for s in userns[:3]:
      name=User.objects.get(username=s).get_full_name()
      sayı=Person.objects.filter(username=s)[0].bildirmesayısı
      newbosd.append({"name":name,"sayı":sayı,"n":n})
      n+=1
   return newbosd
def mamakilo():
   bosd={}
   a=Person.objects.all()
   for i in list(a):
      bosd[i.username]=i.mamakilo
   userns=list(dict(sorted(bosd.items(), key=lambda item: item[1])))
   userns=userns[::-1]
   newboss=[]
   n=1
   for s in userns[:3]:
      name=User.objects.get(username=s).get_full_name()
      sayı=round(Person.objects.filter(username=s)[0].mamakilo/1000,1)
      newboss.append({"name":name,"sayı":sayı,"n":n})
      n+=1
   return newboss

class WelcomeView(ListView):
   model = Kulube
   template_name = "harita/index.html"
   context_object_name = 'kulubeler'
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['besleme'] = beslemesayıları()
      context['yuvabildirme'] = yuvabildirsayıları()
      context['mamakg'] = mamakilo()
      return context
class HaritaView(ListView):
   model = Kulube
   template_name = "harita/harita.html"
   
   def get_context_data(self,**kwargs):
      context = super().get_context_data(**kwargs)
      ks=Kulube.objects.all()
      m=folium.Map(location=[41.02,29],zoom_start=12)
      for i in list(ks):
         text=f"<a target='_blank' href='/yuva_details/{i.id}> Detay </a>"
         print(text)
         folium.Marker([i.latitude,i.longitude],popup=text,tooltip="Detay için tıklayın.").add_to(m)
      m=m._repr_html_()
      context['m']=m
      return context

def yuva_details(request,id):
   try:
      if not request.user.is_authenticated:
         return redirect("home")
      if request.POST:
         a=Kulube.objects.get(id=id)
         sonuc=a.created_at
         fark=(datetime.datetime.now(datetime.timezone.utc)-sonuc).days
         a.save()
         a.sayac+=int(request.POST["kackilo"])
         a.save()
         b=request.user
         c=Person.objects.get(username=b)
         c.mamakilo += int(request.POST["kackilo"])
         c.beslemesayısı+=1
         c.save()
         messages.add_message(request,messages.INFO,"Herşey için teşekkürler.")
         return redirect("home")
      yuva=Kulube.objects.get(id=id)
      sonuc=yuva.created_at
      fark=(datetime.datetime.now(datetime.timezone.utc)-sonuc).days
      oran=int(round(fark/(yuva.sayac/1000)))
      mahalle=yuva.mahalle.capitalize()
      sokak=yuva.sokak.capitalize()
      ilce=yuva.ilçe.capitalize()
      il=yuva.il.capitalize()
      kapıno=yuva.kapı
      adres=f" Yuva {mahalle}, {sokak}, {il}/{ilce} Konumunda {kapıno} no'lu bina yakınlarındadır. "
      m=folium.Map(location=[yuva.latitude,yuva.longitude],zoom_start=18)
      folium.Marker([yuva.latitude,yuva.longitude]).add_to(m)
      m=m._repr_html_
      context={
         "adres":adres,
         "m":m,
         "oran":oran,
      }
      return render(request,"harita/yuva_details.html",context)
   except:
      messages.add_message(request,messages.INFO,"Bir sorun oluştu.")
      return redirect("home")

def yuvabildir(request):
   try:
      if not request.user.is_authenticated:
         return redirect("home")
      if request.method=="POST":
         il=request.POST["il"]
         ilce=request.POST["ilce"]
         mahalle=request.POST["mahalle"]
         sokak=request.POST["sokak"]
         kapı=request.POST["kapı"]
         acıklama=request.POST["acıklama"]
         kelime=sokak+","+ilce+","+il
         location=geocoder.osm(kelime)
         if not location.lat:
            messages.add_message(request,messages.INFO,"Adres bulunamadı.")
            return redirect("home")
         new=Kulube(
            il=il,
            ilçe=ilce,
            mahalle=mahalle,
            sokak=sokak,
            kapı=kapı,
            acıklama=acıklama,
            img=(str(random.randint(1,8))+".jpeg"),
            latitude=location.lat,
            longitude=location.lng)
         new.save()
         a=Person.objects.filter(username=request.user).first()
         a.bildirmesayısı += 1
         a.save()
         messages.add_message(request,messages.INFO,"Yuva kaydı alındı, teşekkürler.")
         return redirect("home")
      return render(request,"harita/yuvabildir.html")
   except:
      messages.add_message(request,messages.ERROR,"Bir sorun oluştu.")
      return redirect("home")


class BulView(ListView):
   model = Kulube
   template_name = 'harita/bul.html'
   context_object_name = 'kulubeler'

def profil(request):
   try:
      if not request.user.is_authenticated:
         return redirect("home")
      userr=request.user
      datauser2=User.objects.filter(username=userr)[0]
      datauser=Person.objects.filter(username=userr)[0]
      context={
         "profil":datauser,
         "profil2":datauser2
      }
      return render(request,"harita/profil.html",context)
   except:
      messages.add_message(request,messages.ERROR,"Bir sorun oluştu.")
      return redirect("home")

class IletisimView(TemplateView):
   template_name = 'harita/iletisim.html'




