# -*- coding: utf-8 -*-
from django import forms
from concert.models import UserProfile,ConcertModel,TestModel
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username','password')
        
        
       
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website','picture',)
        

class ConcertForm(forms.ModelForm):
    class Meta:
        model = ConcertModel
        fields = '__all__'
        #field = ('concertId','concertName','bandId','location','date','tickets')
  
        
class TestForm(forms.ModelForm):
    concertId = forms.IntegerField(label="ConcertId")
    class Meta:
        model = TestModel
        fields = '__all__'
        
    
