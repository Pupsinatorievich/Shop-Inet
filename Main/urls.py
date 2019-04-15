# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:43:33 2019

@author: Pups
"""

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ path('land/', views.landing, name='landing'), 
               path('admin/', admin.site.urls),
               path('', views.home, name="home"),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


