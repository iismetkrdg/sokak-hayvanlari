import django
from . import views

from django.urls import path

urlpatterns = [
    path('',views.WelcomeView.as_view(),name="home"),
    path('yuva',views.yuvabildir,name="yuvabildir"),
    path('harita',views.harita,name="harita"),
    path('yuva_details/<int:id>',views.yuva_details,name="yuva_details"),
    path('bul',views.bul,name="bul"),
    path('profil',views.profil,name="profil"),
    path('iletisim',views.iletisim,name="iletisim"),
]
