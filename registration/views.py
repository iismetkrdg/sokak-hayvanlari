from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from harita.models import Person
import uuid

def login_request(request):
   if request.user.is_authenticated:
      return redirect("home")
   if request.method=="POST":
      username= request.POST["username"]
      password=request.POST["password"]
      if not User.objects.filter(username=username):
         messages.add_message(request,messages.ERROR,"Kullanıcı adı bulunamadı.")
         return redirect("login")
      elif not User.objects.get(username=username).is_active:
         return render(request,"registration/login.html",{"error":"Öncelikle mail adresinizi doğrulamanız gerekmektedir."})
      user=authenticate(request,username=username,password=password)
      if user is not None:
         login(request,user)
         return redirect("home")
      else:
         messages.add_message(request,messages.INFO,"Yanlış parola veya şifre girdiniz.")
         return redirect("login")
      
   return render(request,"registration/login.html")


def register_request(request):
   if request.user.is_authenticated:
      return redirect("home")
   if request.method =="POST":
      username = request.POST["username"]
      firstname = request.POST["firstname"]
      lastname = request.POST["lastname"]
      email = request.POST["email"]
      password = request.POST["password"]
      repassword = request.POST["password"]
      
      if password==repassword:
         if User.objects.filter(username=username).exists():
            return render(request,"registration/register.html",{
               "error":"Bu kullanıcı adı kullanılıyor.",
               "username":username,
               "firstname":firstname,
               "lastname":lastname,
               "email":email
               })
         else:
            if User.objects.filter(email=email).exists():
               return render(request,"registration/register.html",{
                  "error":"Bu e-mail zaten kullanılıyor.",
                  "username":username,
                  "firstname":firstname,
                  "lastname":lastname,
                  "email":email
                  })
            else:
               try:
                  user=User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                  user.is_active=False
                  user.save()
                  auth_token=str(uuid.uuid4())
                  usern = Person(username=username,auth_token=auth_token)
                  usern.save()
                  send_mail_after_regis(email,auth_token)
                  return redirect("tokensend")
               except Exception as e:
                  return redirect("error")
      else:
         return render(request,"registration/register.html",{
            "error":"Parolalar eşleşmiyor.",
            "username":username,
            "firstname":firstname,
            "lastname":lastname,
            "email":email
            })
   return render(request,"registration/register.html")

def logout_request(request):
   logout(request)
   return redirect("home")
from django.core.mail import EmailMessage,send_mail
from django.template.loader import render_to_string
def send_mail_after_regis(semail,token):
   template=render_to_string('email_template.html',{"token":token})
   send_mail("Hesabını Doğrula",template,'Sokaktakiler Ekibi<sokaktakilerekibi@gmail.com>',[semail])
def verify(request,auth_token):
   try:
      profile_obj=Person.objects.filter(auth_token=auth_token).first()
      name=profile_obj.username
      user=User.objects.filter(username=name).first()
      if profile_obj:
         user.is_active=True
         user.save()
         
      else:
         return redirect("error")
      return redirect("success")
   except Exception as e:
      return redirect("error")
def error_page(request):
   return render(request,"registration/error.html")

def token_send(request):
   return render(request,"registration/token_send.html")

def success(request):
   return render(request,"registration/success.html")

 