"""Comershal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.adds_sort_date_new, name='adds_sort_date_new'),
    url(r'adds_sort_price_smoll/$', views.adds_sort_price_smoll, name='adds_sort_price_smoll'),
    url(r'adds_sort_price_big/$', views.adds_sort_price_big, name='adds_sort_price_big'),
    url(r'^(?P<adds_id>[0-9]+)', views.Advert, name='Advert'),
    url(r'dobavit/$', views.dobavit, name='dobavit'),
    url(r'addcoment/(?P<adds_id>[0-9]+)', views.addcoment, name='addcoment'),
    url(r'adds_sort_date_last/$', views.adds_sort_date_last, name='adds_sort_date_last'),
    url(r'adds_sort_date_new/$', views.adds_sort_date_new, name='adds_sort_date_new'),
    # url(r'adds/dobavit/add_picture/$', views.add_picture, name='add_picture'),
    url(r'page/([0-9]+)/$', views.adds_sort_date_new, name='adds_sort_date_new'),
    ]