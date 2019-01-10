from django.shortcuts import render
import requests
import MySQLdb
from django.views.decorators.csrf import csrf_exempt

from .filters import Filter
from datetime import datetime
from django.db.models import Q


from .models import server_id, stream, re_publish

# Create your views here.


def index(request):
    return render(request, 'app_panelapi/index.html')


def table(request):
    server_name = server_id.objects.all()
    context = {'servers': server_name, }

    return render(request, 'app_panelapi/table.html', context)


# @csrf_exempt
def rtmp(request):
    rule = re_publish.objects.all()

    context = {'rule': rule}
    return render(request, 'app_panelapi/re_publish.html', context)


def streams(request):
    str = stream.objects.all()
    context = {'str': str, }

    return render(request, 'app_panelapi/streams.html', context)


@csrf_exempt
def server_ids(request):
    # rule = re_publish.objects.all ()

    server_ids = request.POST.get("server_ids", "")
    context = {'server_ids': server_ids}
    return render(request, 'app_panelapi/restart.html', context)





