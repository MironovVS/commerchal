from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Advertising
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from .forms import Add_addsForm
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.middleware.csrf import CsrfViewMiddleware
import datetime

# Create your views here.

def Index(request):

    Advertising_list=Advertising.objects.all()

    context={'Advertising_list': Advertising_list,
             'Header': "Список объявлений",}

    return render(request, 'adds/index.html', context)


def adds_sort_price_big(request):

    Advertising_list=Advertising.objects.order_by('-Advertising_price')

    context={'Advertising_list': Advertising_list,
             'Header': "Список объявлений",}

    return render(request, 'adds/index.html', context)


def adds_sort_price_smoll(request):
    Advertising_list=Advertising.objects.all().order_by('Advertising_price')

    context={'Advertising_list': Advertising_list,
             'Header': "Список объявлений"}

    return render(request, 'adds/index.html', context)


def Advert(request, adds_id):
    p=get_object_or_404(Advertising, pk=adds_id)
    return render(request, 'adds/Advert.html', {'Advert': p})


def dobavit(request):
    add_form=Add_addsForm
    args={}
    args.update(csrf(request))
    args['form']=add_form
    if request.POST:
        new_adds=Add_addsForm(request.POST)
        if new_adds.is_valid():
            new_adds.save()
            return HttpResponseRedirect('/adds/')
        else:
            args['error_msg']="True"
    return render(request, 'adds/dobavit.html', args)


def adds_sort_date_last(request):
    Advertising_list=Advertising.objects.all().order_by('Advertising_date')

    context={'Advertising_list': Advertising_list,
             'Header': "Список объявлений"}

    return render(request, 'adds/index.html', context)

def adds_sort_date_new(request):
    Advertising_list=Advertising.objects.all().order_by('-Advertising_date')

    context={'Advertising_list': Advertising_list,
             'Header': "Список объявлений"}

    return render(request, 'adds/index.html', context)