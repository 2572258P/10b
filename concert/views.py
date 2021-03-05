from django.shortcuts import render
#from django.http import HttpResponse

        
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
    #context_dict = {}
    return render(request,'concert/register.html')#,context=context_dict)

def signin(request):
    #context_dict = {}
    return render(request,'concert/signin.html')#,context=context_dict)

