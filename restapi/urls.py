from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [

    re_path(r'^kulubeler/$', views.KulubeList.as_view()),
    path('kulubeler/<pk>/',views.KulubeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)