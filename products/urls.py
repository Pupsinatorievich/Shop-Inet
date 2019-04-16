# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:43:33 2019

@author: Pups
"""

from django.urls import path
from products import views

urlpatterns = [ 
       path('product/<product_id>/', views.product, name='product'), 

               ]

