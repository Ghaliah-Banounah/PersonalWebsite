from django.shortcuts import render, redirect
from django.http import HttpRequest
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