# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:43:33 2019

@author: Pups
"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ path(r'land/', views.landing, name='landing'), 
               path('admin/', admin.site.urls),
               path(r'', views.home, name="home"),
               ]

