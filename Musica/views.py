
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def signin(request):
    return render(request, 'app/signin.html')
