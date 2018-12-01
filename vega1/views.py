from django.shortcuts import render
import requests
import MySQLdb
from datetime import datetime
import logging
from .models import server
# Create your views here.


def index(request):
    return render(request, 'vega1/index.html')


def table(request):

    url = 'https://api.wmspanel.com/v1/data_slices?client_id={}&api_key={}&show_servers=true'
    client_id = '1bc3f987-8508-4960-867f-883d4e22fdfd'
    api_key = '364c04c53b8e0cedecbc8fa703cd0472'

    r = requests.get(url.format(client_id, api_key)).json()

    server_id = {
        'id': r['data_slices'][0]['server_ids'][0],
    }

    context = {'server_id': server_id}

    return render(request, 'vega1/table.html', context)
