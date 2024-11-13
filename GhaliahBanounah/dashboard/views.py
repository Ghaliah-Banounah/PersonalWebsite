from django.shortcuts import render
from django.http import HttpRequest
from projects.models import Project
from interests.models import Interest
from posts.models import Post
from django.core.paginator import Paginator

# Dashboard home view 
def homeView(request: HttpRequest):
    projects = Project.objects.all().order_by('-createdAt')[0:2]
    interests = Interest.objects.all().order_by('-createdAt')[0:2]
    posts = Post.objects.all().order_by('-publishedAt')[0:2]

    return render(request, 'dashboard/dashboard.html', context={'projects': projects, 'interests': interests, 'posts': posts})

# Porjects dashoard  
def projectsDashView(request: HttpRequest):
    projects = Project.objects.all().order_by('-createdAt')

    if "search" in request.GET:
        projects = projects.filter(title__contains=request.GET["search"])

    if "orderby" in request.GET and request.GET["orderby"] == "latest":
        projects = projects.order_by('-createdAt')
    elif "orderby" in request.GET and request.GET["orderby"] == "oldest":
        projects = projects.order_by('createdAt')

    paginator = Paginator(projects, 5)
    pageNumber = request.GET.get('page', 1)
    page_obj = paginator.get_page(pageNumber)

    return render(request, 'dashboard/projectsDash.html', {"page_obj" : page_obj})

# Posts dashboard 
def postsDashView(request: HttpRequest):
    posts = Post.objects.all().order_by('-publishedAt')

    if "search" in request.GET:
        posts = posts.filter(title__contains=request.GET["search"])

    if "orderby" in request.GET and request.GET["orderby"] == "latest":
        posts = posts.order_by('-publishedAt')
    elif "orderby" in request.GET and request.GET["orderby"] == "oldest":
        posts = posts.order_by('publishedAt')

    paginator = Paginator(posts, 5)
    pageNumber = request.GET.get('page', 1)
    page_obj = paginator.get_page(pageNumber)

    return render(request, 'dashboard/postsDash.html', {"page_obj" : page_obj})

# Interests dahsboard 
def interestsDashView(request: HttpRequest):
    interests = Interest.objects.all().order_by('-createdAt')

    if "search" in request.GET:
        interests = interests.filter(title__contains=request.GET["search"])

    if "orderby" in request.GET and request.GET["orderby"] == "latest":
        interests = interests.order_by('-createdAt')
    elif "orderby" in request.GET and request.GET["orderby"] == "oldest":
        interests = interests.order_by('createdAt')

    paginator = Paginator(interests, 5)
    pageNumber = request.GET.get('page', 1)
    page_obj = paginator.get_page(pageNumber)

    return render(request, 'dashboard/interestsDash.html', {"page_obj" : page_obj})

