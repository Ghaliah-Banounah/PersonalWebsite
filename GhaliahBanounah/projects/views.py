from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ProjectForm
from .models import Project
from django.core.paginator import Paginator

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

#Project details view
def projectDetailsView(request: HttpRequest, projId:int):

    #Check if the ID is valid or display a 404
    try:
        project = Project.objects.get(pk=projId)
    except Exception:
        response = render(request, '404.html')
    else:
        response = render(request, 'projects/projectDetails.html', context={"project":project})
    
    return response

def displayProjectsView(request: HttpRequest):

    projects = Project.objects.all().order_by('-createdAt')

    paginator = Paginator(projects, 4)
    pageNumber = request.GET.get('page', 1)
    page_obj = paginator.get_page(pageNumber)

    response = render(request, 'projects/displayProjects.html', context={'page_obj': page_obj})

    return response