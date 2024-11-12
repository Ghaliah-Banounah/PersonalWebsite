from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Post
from .forms import PostForm

# Add post
def addPostView(request: HttpRequest):

    postData = PostForm()

    response = render(request, 'posts/addPost.html')
    
    if request.method == "POST":
        postData = PostForm(request.POST, request.FILES)
        if postData.is_valid():
            postData.save()
            
        response = redirect('main:homeView')
        
    return response

def blogView(request: HttpRequest):

    posts = Post.objects.all().order_by('-publishedAt')
    response = render(request, 'posts/blog.html', context={'posts': posts})


    return response