from django.shortcuts import render
from django.http import HttpRequest

# Dashboard home view 
def homeView(request: HttpRequest):

    return render(request, 'dashboard/dashboard.html')

# Porjects dashoard  
def projectsDashView(request: HttpRequest):

    return render(request, 'dashboard/projectsDash.html')

# Posts dashboard 
def postsDashView(request: HttpRequest):

    return render(request, 'dashboard/postsDash.html')

# Interests dahsboard 
def interestsDashView(request: HttpRequest):

    return render(request, 'dashboard/interestsDash.html')
