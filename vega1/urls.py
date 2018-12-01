from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index),
     url(r'^table.html/$', views.table),
   # url(r'^streams.html/$', views.streams),
]