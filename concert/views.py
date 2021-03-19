from django.shortcuts import render
from concert.forms import UserForm,UserProfileForm,ConcertForm #TestForm
from concert.models import ConcertModel,Ticket,UserProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages 
from datetime import datetime
import random
#from django.http import HttpResponse

from datetime import datetime

def getTimeToInt():    
    a = datetime.now()
    a = int(a.strftime('%Y%m%d%H%M%S'))
    return a


def dev(request,cmd):
    if request.method == 'POST':
        if cmd == 'addConcert':
            Id = getTimeToInt()
            name = "Glasgow party" + str(random.randint(1,10000))
            
            ConcertModel.objects.get_or_create(date=datetime.now(),concertId=Id,concertName=name);                        
        if cmd == 'addTicket':
            if request.user.is_authenticated:
                ticketId = random.randint(1,10000)
                concert = ConcertModel.objects.last()
                Id = 0
                if concert:
                    Id = concert.concertId
                Ticket.objects.get_or_create(ticketId=ticketId,user=request.user,concertId=Id)
            else:
                print("You need to be authenticated")
                
            
        
    return render(request,'concert/dev.html')

        
# Create your views here.
def index(request):
    concertList = ConcertModel.objects.order_by('-date')    
    context_dict = {}
    context_dict['concertList'] = concertList
    
    return render(request,'concert/index.html',context=context_dict)

def about(request):
    #context_dict = {}
    return render(request,'concert/about.html')#,context=context_dict)

def booking(request):
    #context_dict = {}
    return render(request,'concert/booking.html')#,context=context_dict)

def concert(request,Id):
    cont = {}
    if request.method == 'POST':
        foundConcert = concert.objects.get(concertId=Id)
        cont['concert'] = foundConcert        
    return render(request,'concert/concert.html',context=cont)

def myaccount(request):    
    #tickets = Ticket.objects.order_by('-ticketId')#Ticket.objects.filter(userId='abc')    
    tickets = Ticket.objects.filter(user=request.user)
    return render(request,'concert/myaccount.html',context={'tickets':tickets})

def register(request):
    registered = False
    
    custom_error_msg = []
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():               
            if request.POST.get("pw_confirm") != request.POST.get("password"):
                custom_error_msg.append("Please, check the password confirmation")                
            else:                
                user = user_form.save()
                user.set_password(user.password)
                user.save()                
                profile = profile_form.save(commit=False)
                profile.user = user
                
                lastPF = UserProfile.objects.last();
                if lastPF:
                    profile.uniqueId = lastPF.uniqueId + 1;
                else:
                    profile.uniqueId = 0
                
                profile.save()
                registered = True
                
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request,
          'concert/register.html',
          context= {'user_form':user_form,
                    'profile_form': profile_form,
                    'registered':registered,
                    'custom_error_msg':custom_error_msg})
        

def signin(request):
    error_msg = []
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')        
        
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('concert:index'))
            else:
                error_msg.append("Your account is disabled.")
        else:
            error_msg.append("Invalid signing in details")    
            
    return render(request,'concert/signin.html',context={"error_msg":error_msg})

def signout(request):
    logout(request)    
    return redirect(reverse('concert:index'))
        
        
        
        
        
        
        
        
        
        
        
        