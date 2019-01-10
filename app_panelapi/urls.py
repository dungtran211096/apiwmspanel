from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index),
     url(r'^table.html/$', views.table, name='table'),
     url(r'^streams.html/$', views.streams, name='streams'),
     url(r'^re_publish.html/$', views.rtmp, name='re_publish'),
     url(r'^server/restart/$', views.server_ids, name='server_ids')
]
