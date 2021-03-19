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
        path('booking/',views.booking,name = 'booking'),
        path('concert/<int:Id>/',views.concert,name = 'concert'),        
        path('myaccount/',views.myaccount,name = 'myaccount'),
        path('register/',views.register,name = 'register'),
        path('signin/',views.signin,name = 'signin'),
        path('signout/',views.signout,name = 'signout'),
        path('dev/<slug:cmd>/',views.dev,name = 'dev')
        ]
