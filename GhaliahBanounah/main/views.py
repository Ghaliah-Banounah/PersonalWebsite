from django.shortcuts import render, redirect
from django.http import HttpRequest
from interests.models import Interest

#Home view
def homeView(request: HttpRequest):

    interests = Interest.objects.all().order_by('-createdAt')[0:3]

    return render(request, 'main/home.html', context={'interests': interests})

#Mode change view
def modeView(request: HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))
    
    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")
        
    return response