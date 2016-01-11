from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Advertising, Comments
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from .forms import Add_addsForm, Commentform
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.middleware.csrf import CsrfViewMiddleware
import datetime
from django.contrib import auth
from django.core.paginator import Paginator #разбивает по страницы при выводе

# Create your views here.

def Index(request, page_number=1):

    Advertising_list=Advertising.objects.all()

    current_page=Paginator(Advertising_list, 2)

    context={'Advertising_list': current_page.page(page_number),
             'Header': "Список объявлений",
             'username': auth.get_user(request).username}

    return render(request, 'index.html', context)


def adds_sort_price_big(request, page_number=1):

    Advertising_list=Advertising.objects.order_by('-Advertising_price')

    current_page=Paginator(Advertising_list, 2)

    context={'Advertising_list': current_page.page(page_number),
             'Header': "Список объявлений",
             'username': auth.get_user(request).username}

    return render(request, 'index.html', context)


def adds_sort_price_smoll(request, page_number=1):
    Advertising_list=Advertising.objects.all().order_by('Advertising_price')

    current_page=Paginator(Advertising_list, 2)

    context={'Advertising_list': current_page.page(page_number),
             'Header': "Список объявлений",
             'username': auth.get_user(request).username}

    return render(request, 'index.html', context)


def Advert(request, adds_id):
    args={}
    args['Advert']=get_object_or_404(Advertising, pk=adds_id)
    args['Comments']=Comments.objects.filter(comments_advertising_id=adds_id)
    args['form_comm']=Commentform
    args['username']=auth.get_user(request).username
    return render(request, 'Advert.html', args)


def dobavit(request):
    add_form=Add_addsForm
    args={}
    args.update(csrf(request))
    args['form']=add_form
    args['username']=auth.get_user(request).username
    if request.POST:
        new_adds=Add_addsForm(request.POST, request.FILES)

        if new_adds.is_valid() :

            new_adds.save()
            return HttpResponseRedirect('/')
        else:
            args['error_msg']="True"
    return render(request, 'dobavit.html', args)


def adds_sort_date_last(request, page_number=1):
    Advertising_list=Advertising.objects.all().order_by('Advertising_date')

    current_page=Paginator(Advertising_list, 2)

    context={'Advertising_list': current_page.page(page_number),
             'Header': "Список объявлений",
             'username': auth.get_user(request).username}

    return render(request, 'index.html', context)

def adds_sort_date_new(request, page_number=1):
    Advertising_list=Advertising.objects.all().order_by('-Advertising_date')

    current_page=Paginator(Advertising_list, 2)

    context={'Advertising_list': current_page.page(page_number),
             'Header': "Список объявлений",
             'username': auth.get_user(request).username}

    return render(request, 'index.html', context)

def addcoment(request, adds_id):
    if request.POST:
        form=Commentform(request.POST)
        if form.is_valid():
            coment=form.save(commit=False)
            coment.comments_advertising=Advertising.objects.get(id=adds_id)
            form.save()
    return redirect('/%s' % adds_id)
