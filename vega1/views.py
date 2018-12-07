from django.shortcuts import render
import requests
import MySQLdb
from datetime import datetime
import logging
from .models import server_id, stream, re_publish
# Create your views here.


def index(request):
    return render(request, 'vega1/index.html')


def table(request):

    server_name = server_id.objects.all()
    streams = stream.objects.all()

    # servers = server_name.filter(server_id=server_id),
    context = {'servers': server_name, 'streams': streams}
    # data = stream.objects.last()

    return render(request, 'vega1/table.html', context)
