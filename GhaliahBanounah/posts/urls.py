from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('blog/', views.blogView, name='blogView'),
    path('details/<int:postid>', views.postDetailsView, name='postDetailsView'),
]