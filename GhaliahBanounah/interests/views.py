from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import InterestForm

# Add interest
def addInterestView(request: HttpRequest):

    interestData = InterestForm()

    response = render(request, 'interests/addInterest.html')
    
    if request.method == "POST":
        interestData = InterestForm(request.POST, request.FILES)
        if interestData.is_valid():
            interestData.save()
            
        response = redirect('main:homeView')
        
    return response