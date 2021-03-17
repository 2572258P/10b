from django.shortcuts import render
from concert.forms import UserForm,UserProfileForm,ConcertForm #TestForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages 

#from django.http import HttpResponse

def dev(request):    
    concertAdded = False
    if request.method == 'POST':
        cf = ConcertForm(request.POST)
        if cf.is_valid():        
            cf.save(commit=True)
            concertAdded = True
        else:
            messages.error(request, "Error")
            
    else:
        cf = ConcertForm()

    context = {"concertForm":cf,"concertAdded":concertAdded,"messages":messages,"form":cf}
    return render(request,'concert/dev.html',context)

        
# Create your views here.
def index(request):
    #context_dict = {}
    return render(request,'concert/index.html')#,context=context_dict)

def about(request):
    #context_dict = {}
    return render(request,'concert/about.html')#,context=context_dict)

def booking(request):
    #context_dict = {}
    return render(request,'concert/booking.html')#,context=context_dict)

def concert(request):
    #context_dict = {}
    return render(request,'concert/concert.html')#,context=context_dict)

def myaccount(request):
    #context_dict = {}
    return render(request,'concert/myaccount.html')#,context=context_dict)

def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
               profile.picture = request.FILES['picture']
                
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request,
          'concert/register.html',
          context= {'user_form':user_form,
                    'profile_form': profile_form,
                    'registered':registered})
        

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('concert:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid signing in details")
    else:
        return render(request,'concert/signin.html')

