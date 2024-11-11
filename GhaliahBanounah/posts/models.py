from django.db import models

class Post(models.Model):
    
    title = models.CharField(max_length=512)
    content  = models.TextField()
    picture = models.ImageField(upload_to='images/', default='images/default.jpg')
    isPublished = models.BooleanField(default=True)
    publishedAt = models.DateTimeField(auto_now=True)