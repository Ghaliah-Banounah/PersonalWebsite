from django.shortcuts import render, redirect
from django.http import HttpRequest
from interests.models import Interest
from projects.models import Project
from posts.models import Post

#Home view
def homeView(request: HttpRequest):

    projects = Project.objects.all().order_by('-createdAt')[0:2]
    interests = Interest.objects.all().order_by('-createdAt')[0:2]
    posts = Post.objects.all().order_by('-publishedAt')[0:2]

    return render(request, 'main/home.html', context={'interests': interests, 'projects': projects, 'posts': posts})

#Mode change view
def modeView(request: HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))
    
    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")
        
    return response