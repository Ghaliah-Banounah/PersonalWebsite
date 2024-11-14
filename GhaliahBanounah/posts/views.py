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
            
        response = redirect('dashboard:homeView')
        
    return response

# Update post
def updatePostView(request: HttpRequest, postid:int):

    try:
        post = Post.objects.get(pk=postid)
    except Exception:
        response = render(request, '404.html')
    else:
        response = render(request, 'posts/updatePost.html', context={"post":post})
        if request.method == "POST":
            #Update existing post
            postData = PostForm(request.POST, request.FILES, instance=post)
            if postData.is_valid():
                postData.save()

            response = redirect('dashboard:postsDashView')

    return response

#Post details view
def postDetailsView(request: HttpRequest, postid:int):

    #Check if the ID is valid or display a 404
    try:
        post = Post.objects.get(pk=postid)
    except Exception:
        response = render(request, '404.html')
    else:
        response = render(request, 'posts/postDetails.html', context={"post":post})
    
    return response

#Delete post view
def deletePostView(request: HttpRequest, postid:int):

    try:
        post = Post.objects.get(pk=postid)
    except Exception:
        response = render(request, '404.html')
    else:
        post.delete()
        response = redirect('dashboard:postsDashView')
    return response

def blogView(request: HttpRequest):

    posts = Post.objects.all().order_by('-publishedAt')
    response = render(request, 'posts/blog.html', context={'posts': posts})


    return response