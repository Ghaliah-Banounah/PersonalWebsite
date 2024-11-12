from django.shortcuts import render
from django.http import HttpRequest

# Home page 
def homeView(request: HttpRequest):

    return render(request, 'dashboard/home.html')