# -*- coding: utf-8 -*-
from django import forms
from concert.models import UserProfile,ConcertModel,TestModel
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','email')
        
        
       
class UserProfileForm(forms.ModelForm):
    pw_confirm = forms.CharField(widget=forms.PasswordInput())    
    termsOfService = forms.BooleanField()
    class Meta:
        model = UserProfile
        fields = ('pw_confirm','termsOfService')
        

class ConcertForm(forms.ModelForm):
    class Meta:
        model = ConcertModel
        fields = '__all__'
  
        
class TestForm(forms.ModelForm):
    concertId = forms.IntegerField(label="ConcertId")
    class Meta:
        model = TestModel
        fields = '__all__'
        
    
