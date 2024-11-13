from django.urls import path
from . import views
from projects import views as projectViews
from interests import views as interestViews
from posts import views as postViews

app_name = "dashboard"

urlpatterns = [
    path("", views.homeView, name="homeView"),
    
    path("projects/", views.projectsDashView, name="projectsDashView"),
    path('projects/add/', projectViews.addProjectView, name='addProjectView'),

    path("posts/", views.postsDashView, name="postsDashView"),
    path('posts/add/', postViews.addPostView, name='addPostView'),

    path("interests/", views.interestsDashView, name="interestsDashView"),
    path('interests/add/', interestViews.addInterestView, name='addInterestView'),
]