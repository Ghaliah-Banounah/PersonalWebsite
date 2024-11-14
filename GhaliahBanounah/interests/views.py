from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import InterestForm
from .models import Interest

# Add interest
def addInterestView(request: HttpRequest):

    interestData = InterestForm()

    response = render(request, 'interests/addInterest.html')
    
    if request.method == "POST":
        interestData = InterestForm(request.POST, request.FILES)
        if interestData.is_valid():
            interestData.save()
            
        response = redirect('dashboard:homeView')
        
    return response

# Update interest
def updateInterestView(request: HttpRequest, interId:int):

    try:
        interest = Interest.objects.get(pk=interId)
    except Exception:
        response = render(request, '404.html')
    else:
        response = render(request, 'interests/updateInterest.html', context={"interest":interest})
        if request.method == "POST":
            #Update existing interest
            interestData = InterestForm(request.POST, request.FILES, instance=interest)
            if interestData.is_valid():
                interestData.save()

            response = redirect('dashboard:interestsDashView')

    return response

def displayInterestsView(request: HttpRequest):

    interests = Interest.objects.all().order_by('-createdAt')

    response = render(request, 'interests/displayInterests.html', context={'interests': interests})

    return response