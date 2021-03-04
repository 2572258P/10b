# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:47:44 2021

@author: JungshicPark
"""

from django.urls import path
from concert import views

app_name = 'concert' 
#when URLs are referenced by others such as 'rango:url_name' the left side of colon 'rango' is from app_name

urlpatterns = [
        path('',views.index,name = 'index'),
        path('about/',views.about,name = 'about'),
        path('signUp/',views.index,name = 'signup'),
        path('order/',views.index,name = 'order'),
        path('order_result/',views.index,name = 'order_result'),
        path('contact/',views.index,name = 'contact'),
        ]
