#_*_ coding:utf-8 _*_

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]*)/$', views.index, name='index'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^login/$', views.loginto, name='login'),
    url(r'^logout/$', views.logouto, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
