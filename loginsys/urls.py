from django.conf.urls import url, patterns, include
from .import views

urlpatterns = patterns('',
      url(r'^login/', views.login, name='login'),
      url(r'^logout/', views.logout, name='logout'),
      url(r'^register/', views.register, name='register'),
    )


