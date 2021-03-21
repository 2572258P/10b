# -*- coding: utf-8 -*-
from django import forms
from concert.models import UserProfile,ConcertModel,TestModel,Band
from django.contrib.auth.models import User
from datetime import datetime,date as dt
import datetime

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name')
        
class UserProfileForm(forms.ModelForm):
    pw_confirm = forms.CharField(widget=forms.PasswordInput())    
    weAreBand = forms.BooleanField(initial=False,required=False)
    termsOfService = forms.BooleanField()
    
    class Meta:
        model = UserProfile
        fields = ('pw_confirm','weAreBand','termsOfService')

class BandForm(forms.ModelForm):
    bandName = forms.CharField(required=False)
    class Meta:
        model = Band
        fields = ('bandName',)

class DateInput(forms.DateInput):
    input_type = 'date'

class ConcertForm(forms.ModelForm):
    concertName = forms.CharField()
    location = forms.CharField()
    date = forms.DateField(initial=datetime.date.today,widget=DateInput)
    class Meta:
        model = ConcertModel
        fields = ('concertName','location','date','img')


        
class TestForm(forms.ModelForm):
    concertId = forms.IntegerField(label="ConcertId")
    class Meta:
        model = TestModel
        fields = '__all__'
        
    
