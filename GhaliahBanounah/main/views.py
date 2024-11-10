from django.shortcuts import render
from django.http import HttpRequest

def homeView(request: HttpRequest):
    
    return render(request, 'main/home.html')