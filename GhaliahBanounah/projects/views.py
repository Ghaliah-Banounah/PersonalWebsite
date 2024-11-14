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
            
        response = redirect('dashboard:homeView')
        
    return response

# Update project
def updateProjectView(request: HttpRequest, projId:int):

    try:
        project = Project.objects.get(pk=projId)
    except Exception:
        response = render(request, '404.html')
    else:
        response = render(request, 'projects/updateProject.html', context={"project":project})
        if request.method == "POST":
            #Update existing project
            projectData = ProjectForm(request.POST, request.FILES, instance=project)
            if projectData.is_valid():
                projectData.save()

            response = redirect('dashboard:projectsDashView')

    return response


#Delete project view
def deleteProjectView(request: HttpRequest, projId:int):

    try:
        project = Project.objects.get(pk=projId)
    except Exception:
        response = render(request, '404.html')
    else:
        project.delete()
        response = redirect('dashboard:projectsDashView')
    return response

def displayProjectsView(request: HttpRequest):

    projects = Project.objects.all().order_by('-createdAt')
    response = render(request, 'projects/displayProjects.html', context={'projects': projects})

    return response