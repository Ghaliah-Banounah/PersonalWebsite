from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('add/', views.addPostView, name='addPostView'),
    path('blog/', views.blogView, name='blogView')
]