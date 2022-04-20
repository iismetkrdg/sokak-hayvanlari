import django
from . import views

from django.urls import path

urlpatterns = [
    path('',views.WelcomeView.as_view(),name="home"),
    path('yuva',views.yuvabildir,name="yuvabildir"),
    path('harita',views.HaritaView.as_view(),name="harita"),
    path('yuva_details/<int:id>',views.yuva_details,name="yuva_details"),
    path('bul',views.BulView.as_view(),name="bul"),
    path('profil',views.profil,name="profil"),
    path('iletisim',views.IletisimView.as_view(),name="iletisim"),
]
