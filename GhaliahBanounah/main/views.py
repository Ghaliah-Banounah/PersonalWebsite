from django.shortcuts import render, redirect
from django.http import HttpRequest
from interests.models import Interest
from projects.models import Project
from posts.models import Post
from .forms import ContactForm
from django.core.mail import send_mail
from GhaliahBanounah import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime

#Home view
def homeView(request: HttpRequest):

    projects = Project.objects.all().order_by('-createdAt')[0:2]
    interests = Interest.objects.all().order_by('-createdAt')[0:2]
    posts = Post.objects.all().order_by('-publishedAt')[0:2]

    return render(request, 'main/home.html', context={'interests': interests, 'projects': projects, 'posts': posts})

#Contact view 
def contactView(request: HttpRequest):

    contactData = ContactForm()

    response = render(request, 'main/contact.html')
    if request.method == "POST":

        contactData = ContactForm(request.POST)
        if contactData.is_valid():
            contactData.save()

            subject = "Regarding Your Message"
            fromEmail = settings.DEFAULT_FROM_EMAIL
            to = request.POST['email']
            htmlContent = render_to_string('main/mailTemplate.html', {'reciever': request.POST, 'sentAt': datetime.strftime( datetime.now() , "%d/%m/%Y, %H:%M:%S")})
            textContent = strip_tags(htmlContent)
            send_mail(subject, textContent, fromEmail, [to], html_message=htmlContent, fail_silently=False)
        print(contactData.errors)
            
    return response

#Mode change view
def modeView(request: HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))
    
    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")
        
    return response