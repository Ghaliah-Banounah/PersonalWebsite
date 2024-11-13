from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.homeView, name="homeView"),
    path("projects/", views.projectsDashView, name="projectsDashView"),
    path("posts/", views.postsDashView, name="postsDashView"),
    path("interests/", views.interestsDashView, name="interestsDashView"),
]