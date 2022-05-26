import django
from . import views

from django.urls import path

urlpatterns = [
    path('',views.WelcomeView.as_view(),name = "home"),
    path('yuvabildir',views.YuvaBildirView.as_view(),name = "yuvabildir"),
    path('harita',views.HaritaView.as_view(),name = "harita"),
    path('yuva_details/<pk>',views.YuvaDetailsView.as_view(),name = "yuva_details"),
    path('bul',views.BulView.as_view(),name = "bul"),
    path('profil/<pk>/',views.ProfilView.as_view(),name = "profil"),
    path('iletisim/',views.IletisimView.as_view(),name = "iletisim"),
    path('skorlar/',views.ScoreBoardView.as_view(),name = 'scoreboard')
]
