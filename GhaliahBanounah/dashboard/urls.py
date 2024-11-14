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
    path('projects/update/<int:projId>', projectViews.updateProjectView, name='updateProjectView'),
    # path('projects/delete/<int:projId>', projectViews.updateProjectView, name='updateProjectView'),

    path("posts/", views.postsDashView, name="postsDashView"),
    path('posts/add/', postViews.addPostView, name='addPostView'),
    path('posts/update/<int:postid>', postViews.updatePostView, name='updatePostView'),
    # path('posts/delete/<int:postid>', postViews.updatePostView, name='updatePostView'),

    path("interests/", views.interestsDashView, name="interestsDashView"),
    path('interests/add/', interestViews.addInterestView, name='addInterestView'),
    path('interests/update/<int:interId>', interestViews.updateInterestView, name='updateInterestView'),
    # path('interests/delete/<int:interId>', interestViews.updateInterestView, name='updateInterestView'),
]