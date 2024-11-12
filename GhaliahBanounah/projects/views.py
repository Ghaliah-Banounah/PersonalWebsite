from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ProjectForm
from .models import Project

# Add project
def addProjectView(request: HttpRequest):

    projectData = ProjectForm()

    response = render(request, 'projects/addProject.html')
    
    if request.method == "POST":
        projectData = ProjectForm(request.POST, request.FILES)
        if projectData.is_valid():
            projectData.save()
            
        response = redirect('main:homeView')
        
    return response

def displayProjectsView(request: HttpRequest):

    projects = Project.objects.all().order_by('-createdAt')
    response = render(request, 'projects/displayProjects.html', context={'projects': projects})

    return response