from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("You are watching Index Page")

def about(request):
    #context_dict = {}
    return render(request,'concert/about.html')#,context=context_dict)

def order(request):
    return HttpResponse("This is the order page")