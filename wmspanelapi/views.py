from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .filters import Filter, Filter1
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import server_id, stream, re_publish
from django.views.generic import TemplateView
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
import requests
import MySQLdb
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


# Create your views here.


def user_login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request,
                  'app_panelapi/login.html',
                  {'form': form})


@login_required
def index(request):
    vega = stream.objects.filter(input='notok', status='online')
    vega1 = re_publish.objects.filter(status='0').all()
    filter = Filter1(request.GET, queryset=vega)
    filter1 = Filter(request.GET, queryset=vega1)

    paginator = Paginator(filter1.qs, 10)
    page = request.GET.get('page', 1)
    try:
        paginators = paginator.page(page)
    except PageNotAnInteger:
        paginators = paginator.page(1)
    except EmptyPage:
        paginators = paginator.page(paginator.num_pages)

    context = {'filter': filter, 'filter1': filter1, 'vega': paginators}
    return render(request, 'wmspanelapi/index.html', context, {'section': 'index'})

