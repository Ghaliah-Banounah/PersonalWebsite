from django.db import models

class Project(models.Model):

    title = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='images/', default='images/default.jpg')
    description = models.TextField()
    challenges = models.TextField()
    pathTo = models.CharField(max_length=515)
    createdAt = models.DateTimeField(auto_now_add=True)