from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path('add/', views.addProjectView, name='addProjectView'),
    path('display/', views.displayProjectsView, name='displayProjectsView')
]