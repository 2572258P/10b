# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:47:44 2021

@author: JungshicPark
"""

from django.urls import path
from concert import views
from team10b import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'concert' 
#when URLs are referenced by others such as 'rango:url_name' the left side of colon 'rango' is from app_name

urlpatterns = [
        path('',views.index,name = 'index'),
        path('about/',views.about,name = 'about'),
        path('booking/<int:concertId>/',views.booking,name = 'booking'),
        path('concert/<int:concertId>/',views.concert,name = 'concert'),
        path('concertAdd/',views.concertAdd,name = 'concertAdd'),
        path('myaccount/',views.myaccount,name = 'myaccount'),
        path('deleteAccount/',views.deleteAccount,name = 'deleteAccount'),
        path('register/',views.register,name = 'register'),
        path('signin/',views.signin,name = 'signin'),
        path('signout/',views.signout,name = 'signout'),
        path('SearchResult/',views.search,name = 'searchResult')
        ]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
